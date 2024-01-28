""" 
    思路 :  
        題目給定組array : equation , values , queries 
        equation[i] = [Ai,Bi] , Ai,Bi各自是一個字符表示某個變數 , 
        value[i] 則代表 Ai/Bi的結果 
        現在要回答所有queries[i] = [Ci,Di] , 即要求 Ci/Di , 如果是無法計算的就可以return 0
        
        把這一題當作一個類似graph的結構去找 a/b = 2 , 視為 a->b = 2 , b->a = 1/2  
        如果 b/c = 3 , 則a->c 即 a->b x b->c = 6  , c->a = 1/6 , 如果兩端有哪個是不存在於graph的 , 則是-1 
        
        現在問題在於要怎麼去建構這張graph , 可以滿足我們最終需要能夠取得graph中任意兩個node的距離

        我認為的理想作法可能是dijkstra , 但這一題看起來也可以一般的DFS ( maybe in every queries !? )

"""

""" 
    解法一. 
        基於Dict去存每一個節點的鄰居以及到達他的cost , 在建構過程是雙向的 , 建構完之後針對每個query都用DFS 
        因為題目告訴我們不會矛盾 , 因此只要DFS有解 , 就會是正確的除值 , 若DFS找不到就是-1
        
        這個解法可以過測資 , 速度不太好但沒有到很慘 , 反而是空間不太好
"""
from typing import List 
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Step.1 建立Dict graph 
        graph = dict() 
        
        for idx ,  (src , dst) in  enumerate(equations): 
            if src in graph: 
                #graph[src][dst]代表從src到dst的距離 , 即src/dst
                graph[src][dst] = values[idx]                
            else : 
                graph[src] = {dst : values[idx]}

            if dst in graph: 
                graph[dst][src] =  1 / values[idx]
            else : 
                graph[dst] = {src: 1/ values[idx]}
                
        
        # step2. 針對每一個query用DFS去找 
        sol = [] 
        for idx , (src,dst) in enumerate(queries): 

            if not src in graph or not dst in graph : 
                sol.append(-1.0)
                continue
            
            # 每一個DFS , 初始化stack , visited set 
            stack = [] 
            visited = set() 
            # stack保存 (node,acc) , 用來keep累計的值
            stack.append( (src,1) )
            visited.add(src) 
            find = False 
            while stack : 
                
                (node , acc) = stack.pop() 

                if node == dst : 
                    sol.append(acc)
                    find = True 
                    break 
                
                for neighbor in graph[node] : 
                    if not neighbor in visited : 
                        visited.add(neighbor)
                        stack.append( (neighbor ,  acc * graph[node][neighbor] )  )
                
            if not find : 
                sol.append(-1.0)
                        
            
        return sol 



equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"] ]
S = Solution()
print(S.calcEquation(equations ,values , queries))
            
            
            
                


                