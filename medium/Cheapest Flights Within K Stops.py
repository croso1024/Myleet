
""" 
    思路 : 
        這一題會給一張Graph , 描述每個節點間的連接關係
        我們要找的是從src -> dst , 在允許只有k個中繼點的情況下的最短路徑, 
        
        題目給定了node數量 n < 100 , edge數量則最多因為全連接是約 n^2/2 . 
        
        這一題直接看上去很直覺的是要走Backtrack能解, 我們先通過走一個 O(n^2)級別的來建立一個distance matrix. 
        然後去建立一個已經走過得節點清單後就可以走backtrack , 去看在k步之內是否可以到達終點。
        --> 這個思路可行 , 但受到time complexity限制過不了大的測資
        
        另一個思路可以想到走DFS或BFS , 畢竟這是一題Graph題 , 透過BFS去限制擴展的次數就可以找到k個中繼點內最短的路徑 
        -->  因為這一題有cost存在 , 因此BFS的queue要更換成priority queue , 也就是heap , 優先去找cost低的鄰居
        但heapq實做的話會需要自己去定義節點之間比大小的函數 , 或著說要新增class來做
        
"""

from typing import List 

""" 
    解法一. back track先上看看 , 確認我的思路是ok的 
    --> 這個解法確實OK , 但也如預期在實際的測資會超時 , 使用Backtrack暴力展開 , worse case可能是階層級
"""

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # create distance matrix : n x n 
        dist_matrix = [ [ None for i in range(n)] for j in range(n) ]
        
        # fill the distance matrix with directed edge , if None : no connect of the two city 
        for (i,j , cost) in flights: 
            dist_matrix[i][j] = cost 
        
        # best solution cost 
        best = float('inf') 
        vistied = set() 
        # backtrack函數留當前所在節點 , k , 累積cost和已經拜訪過的節點set作為參數 , distance matrix用外部的 
        def backtrack( city ,  vistied:set, k , acc_cost): 
            nonlocal best 
            # Arrival the dst before k==0 or just k==0 : update the best solution 
            if city == dst : best = min(acc_cost , best)

            # k<0 , and not yet arrival : return   (k==0又還沒到終點 ,那就是要看下一步能不能到 , 因此k<0才是真的沒希望)
            elif k < 0 : return 
                
            for node in range(n): 
                # 如果可以到達且又是還沒拜訪過得就可以去看看
                if not dist_matrix[city][node] is None and not node in vistied : 
                    vistied.add(node) 
                    backtrack( node , vistied , k-1 , acc_cost+dist_matrix[city][node]  )
                    vistied.remove(node)

        backtrack(src , vistied=vistied , k = k , acc_cost=0  )
        
        return best if not best == float("inf") else -1 


""" 
    解法二. 改用Dynamic programming . 問題在於要如何定義DP函數
    
    我的想法可能是按照k來推進 , k step到達dst的最短路徑會等於 min ( k-1到達離dst最近neighbor的路徑 + neighbor->dst , k-1步到達dst的路徑  )
    所以dp應該是一個二維陣列  city x k , 
    
    dp[i][j] 表示在i步到達city : j的最短距離 

    base case : 
        dp[:][src] = 0  , dp初始化為float('inf') 表示到達不了
    
    dp[i][j] = min ( dp[i-1][j的鄰居] + dist[鄰居][j] ,  dp[i-1][j]  )   
    
    這樣我們要找的目標就是 dp[k+1][dst] , 因為總共k+1步
    
    這個解法算是自己領領悟出來 , 但需要三層迴圈 , time complexity 大約是 O(N^2*K) ~ O(N^3) 
"""


class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dp = [[ float('inf') for i in range(n) ] for j in range(k+2)]

        dist_matrix = [ [ None for i in range(n)] for j in range(n) ]
        for (i,j , cost) in flights: dist_matrix[i][j] = cost 
            
        # base case , 起始點在任何步數的最低cost都是0 , 
        
        for i in range(k+2): dp[i][src] = 0 
        
        # 外層推進主要狀態 , 這裡應該是k , 但我把他寫在內層了,不過沒差
        for  step in range(1,k+2): 
            # 內層尋訪所有city 
            for city1 in range(n): 
                for city2 , cost in enumerate(dist_matrix[city1]) : 
                    # city1 和 city2是連接的 , 其關係是city1可以前進到city2
                    if not cost is None  : 
                        dp[step][city2] = min( dp[step-1][city1] + cost , dp[step-1][city2] , dp[step][city2] ) 
                        
        return dp[k+1][dst] if dp[k+1][dst] != float('inf') else -1 
    
""" 
    解法三: 東哥版使用DP的作法 , 採用top-down的解法加memo , 和我的backtrack方法很接近 , 就是加入了memo來加速
"""

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        memo = dict() 
        dist_matrix = [ [ None for i in range(n)] for j in range(n) ]
        for (i,j , cost) in flights: dist_matrix[i][j] = cost 

        # dp函數的定義是,找到目標節點在k步內的最短路徑
        def dp( dst , k ,memo ): 
            # base case : dst = src 
            if dst == src : return 0 
            # 如果k < 0了說明到達不了這個節點
            elif k<0 : return float('inf') 
            
            elif (dst,k) in memo : return memo[(dst,k)] 
            
            best = float("inf")
            # 往下展開,目標是所有可以"到達"(注意是到達) dst的節點 
            for node in range(n) : 
                if not dist_matrix[node][dst] is None :
                    best = min(best , dp(node , k-1 , memo) + dist_matrix[node][dst] )
                
            memo[(dst,k)] = best 
            
            return best 
            
            
        sol = dp(dst , k , memo) 
        
        return sol if sol != float('inf') else -1 
        
