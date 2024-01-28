from typing import List 
""" 
    思路: 
    
        這一題蠻玄幻的, 給定一組字串list strs , 當中每個字串都是0和1組成 , 接著給定常數m,n 
        題目要求從strs中進可能選出最多元素 , 但這些元素內的 0數量總和不超過m , 1不超過n
        
        這一題的敘述讓我覺得有一點類似背包問題 , 每一個item我都能選擇要拿或不拿 , 但是每個item都只有一個,不可重複拿
        並且每個物品都有兩個維度的重量 ,我想要盡可能拿到最多的物品

        按照背包問題的思路 , dp的表格應該規劃為 物品數量 x 背包重量 , 代表在 0-i個物品範圍 ,以及背包重k的情況下可以拿取的最大價值
        選擇某一物品 ,就相當於在 0-(i-1)個物品中 背包重k-(weight[i])的最大價值 + value[i]  

        ---------------------------------------------

        
        泛化到我們這一題的思路 , dp表格應該是 物品數量 x M x N , 一樣是代表在集合0-i的範圍 , 容量限制為M,N的情況下可以拿的最大價值 
        
        dp[i][u][v] 代表在 0-i的物品範圍內 , 重量1為u ,重量2為v的情況下可以取得的最大"數量" 
        
        # base case : 在重量為0的情況下 , 都不能拿
        
        # 到達第i件物品的最大數量 = ( 拿了第i件物品 or  不拿第i件物品 ) , 如果容量原因不能拿 , 那只能選擇不拿i件物品
        dp[i][u][v] =  dp[i-1][ u- U(i) ][ v-V(i) ]  + 1  or dp[i-1][u][v] 
        
        為了完成這些功能 ,我們還需要一個函式用來計算 0 ,1的數量
"""


""" 
    解法一. 基本上follow上面的思路 
        這一題最困難的地方在於思考DP推進時所需要用到的元素 , 但好在這一題是求極值問題 ,我們在初始化列表的時候將所有值歸為0
        接下來只要邏輯清晰就能夠順利解出
        
        下面的解法我額外建立了一個items陣列, 避免每次都要重算一個字串裡面有多少0,1 
        (但實際發現根本不用 , 每次在最外層迴圈開頭算一次就好,反正內迴圈也只會用到當前這個重量 )
        
        最終這個解的速度很差 , 空間還行 , 這個時間複雜度應該已經ok了 , 空間的話是有優化的餘地 
        --> 即我們都只保存前一frame的i , 因為在計算時只會用到i-1的範圍
"""
import numpy as np 
class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # 我們將字串內容抽象為重量 , weight(s)返回字串中有幾個0幾個1 
        def weight(s): 
            zero,one = 0 , 0 
            for i in s:  
                if i == "0" : zero += 1 
                else : one += 1 
            return zero , one
        
        # 建立一個3維DP  i , u ,v 對應 len(strs)+1 , (m+1) , (n+1) , 預設值為0包含了base-case
        # 注意這邊讓商品列表也從空的開始 , 讓下面推進dp順利進行
        dp = [
                [ [0 for v in range(n+1)]    for u in range(m+1) ]
                for i in range(len(strs)+1) 
            ]
        
        
        #　我們初始化一個items table,代表每一件物品的重量 , 避免一直重複call weight(s) 
        items = [(0,0)] + [  weight(s) for s in strs ]
        
        # 推進DP 
        # dp[i][u][v] : 商品範圍在0-i個 , 並且重量在u與v時可以裝的最大元素數量 , 只會用到0-(i-1)範圍以及重量小於等於的部份
        
        for i in range(1,len(strs)+1): 
            
            for u in range(m+1): 
                
                for v in range(n+1): 
                    # 如果裝不下的話 , 他就相當於沒有裝這個物品前的最大數量
                    if items[i][0] > u or items[i][1] > v : 
                        dp[i][u][v] = dp[i-1][u][v] 
                    
                    else : 
                        #到此就是u,v裝的下item了
                        
                        # 此時dp[i][u][v]的最大數量 = 
                        # ( 1 + 在沒有裝物品i前的最大價值 , 不裝物品i的最大價值 )
                        dp[i][u][v] = max( 1 + dp[i-1][ u- items[i][0] ][ v - items[i][1] ]  , dp[i-1][u][v] ,dp[i][u][v] )
                        
        # 最終答案在 dp[len(strs)-1][m][n] 
        return dp[len(strs)][m][n]


""" 
    解法二. 
        採用 str.count()方法來計算有多少字 , 而且因為只要用一次根本就不需要存起來
        另外做了狀態壓縮 ,我們只存一個frame的table ,
        
        這個解法計算速度有明顯上升 , 空間變得很好
"""
import numpy as np 
class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # 我們將字串內容抽象為重量 , weight(s)返回字串中有幾個0幾個1 
        def weight(s): 
            zero,one = 0 , 0 
            for i in s:  
                if i == "0" : zero += 1 
                else : one += 1 
            return zero , one
        
        # 這邊只存一個frame        
        dp = [ [0 for v in range(n+1)]    for u in range(m+1) ]
        
        #　我們初始化一個items table,代表每一件物品的重量 , 避免一直重複call weight(s) 
        
        # 推進DP 
        # dp[i][u][v] : 商品範圍在0-i個 , 並且重量在u與v時可以裝的最大元素數量 , 只會用到0-(i-1)範圍以及重量小於等於的部份
        
        for i in range(1,len(strs)+1): 
            
            zeros = strs[i-1].count("0")
            ones = strs[i-1].count("1") 
            new_dp = [ [0 for v in range(n+1)]  for u in range(m+1) ]
            
            for u in range(m+1): 
                
                for v in range(n+1): 
                    # 如果裝不下的話 , 他就相當於沒有裝這個物品前的最大數量
                    
                    if  zeros > u or ones > v : 
                        new_dp[u][v] = dp[u][v] 
                    
                    else : 
                        #到此就是u,v裝的下item了
                        
                        # 此時dp[i][u][v]的最大數量 = 
                        # ( 1 + 在沒有裝物品i前的最大價值 , 不裝物品i的最大價值 )
                        new_dp[u][v] = max( 1 + dp[ u- zeros ][ v - ones ]  , dp[u][v]  )

            dp = new_dp
            
        return dp[m][n]

S = Solution() 
test_case = ["10","0001","111001","1","0"]

print(S.findMaxForm(test_case , 5,3))