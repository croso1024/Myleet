""" 
    題意:   
        題目給定一張Graph並使用edges list來進行表示 , 想要問說從哪一條edge開始, 該edge就是多餘的,因為graph上所有節點都已經彼此相連
    思路:
        很明確的聯想到union-find的問題, 我們直接在這一題去實現一個union find set. 
        然後一條條edge加上去直到將所有node都連通 , 此時下一條edge開始就是多餘的
        
        -> 基本上就是這樣的思路 , 只是說題目給的edges有可能第i條是多餘的,但第i+1條是必須的 , 所以觸發return的條件變為
        連接該條edge後 union find的count數沒變就是冗於的edge

"""
from typing import List 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # union find , 需要實現union : 將兩個節點連接 / find : 尋找某個節點的root , 作為helper function / connect : 檢查兩個node是否有相連
        
        class UnionFind : 
            
            def __init__(self, nodes_num ):  
                
                # to record the root of every node 
                self.parent = [i for i in range(nodes_num+1)]  

                # keep track the union part in the graph 
                self.count =  nodes_num
                
            # 將兩個節點給連接起來
            def union(self, node1, node2):

                if self.connect(node1 , node2): return 
                
                root1 = self.find(node1)
                root2 = self.find(node2)
                
                self.parent[root2] = root1  
                
                self.count -= 1 
                return 
                
            
            # 尋找指定節點的root , 更重要的是同時進行路徑的壓縮
            def find(self, node) : 
                if self.parent[node] != node : 
                    
                    self.parent[node] = self.find(self.parent[node])
                
                return self.parent[node] 
            
            # 確認兩個節點目前是否相通
            def connect(self,node1 , node2 ): 
                root1 = self.find(node1)
                root2 = self.find(node2) 
                return root1 == root2 
            
        
        UF = UnionFind( nodes_num= len(edges) )            
        
        
        for idx , (u,v) in enumerate(edges): 

            print(f'idx:{idx} , u,v:{u,v}')
            
            before = UF.count            
            UF.union(u,v) 
            after = UF.count 
            
            if before == after : return [u,v]
        
        return -1 

S = Solution()
print(S.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))