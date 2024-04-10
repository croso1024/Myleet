""" 
    題意:
        給定一組有向圖 , 要求我們至少要從幾個節點出發才能走到所有的節點,
    
    思路:
        這一題的概念我認為和拓撲排序有些類似 , 即一個完整的可訪問順序 ,
        我認為先build graph出來,並且先標記那些沒有任何indegree的節點,因為這些節點勢必都要被拜訪過,
        接著走dfs展開把當前節點能到達的節點都標記起來 , 題目已經給定必然有解,所以不考慮cycle的問題 
        
        --- 
        我的原本寫法是OK的 , 但其實寫到後面就有感覺好像可以直接計算有多少節點是沒有in-degree就是答案 ,
        確實提交後發現我的原本寫法可以過 , 不過上面的作法是更快速的.
        稍微想一下,所有沒有任何入度的節點就是必需要用到的節點,因為其他所有節點都有入度 , 可以從其他節點到達
        不過這個思路是因為題目給定了"必有解且唯一解" ,  , 不然若有 0->1 , 1->0 則答案可以是[0]或[1].
        
        若沒有這個限制,我寫的架構仍然可以透過visited set處理這些問題,並返回一個滿足條件的解

"""
from typing import List 
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        # step1. build graph 
        # graph[i] : represent the nodes can reach from node i 
        graph = [ [] for i in range(n) ]
        indegree_node = set()
        for (src , dst) in edges : 
            graph[src].append(dst)
            indegree_node.add(dst) 
        
        visited = set() 
        sol = []
        
        
        def dfs(node):
            
            for neighbor in graph[node] : 
                if not neighbor in visited : 
                    visited.add(neighbor)                
                    dfs(neighbor) 
            
        for i in range(n): 
            
            # 代表這個節點勢必要從這邊開始展開 
            if not i in indegree_node :
                sol.append(i) 
                dfs(i) 
        
        return sol 
                
                
            
        