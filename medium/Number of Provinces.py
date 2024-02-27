"""
    題意:
        給定n座city , 以及一個代表其連接性的matrix. 
        要求總共有'幾塊' city group 
        
    思路:    
        union-find , 或BFS記數字 
        我這邊做union-find algorithms , 因為這一題只要回傳最後剩下幾塊
"""


""" 
    解法一. Union-Find , 速度跟空間都超級優
"""
from typing import List 
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        class union_find : 
            
            def __init__(self , nodes_num) :
                self.nodes_num = nodes_num 
                self.parent = [ i for i in range(self.nodes_num)] 
                # represent the amount of province 
                self.groups = nodes_num 
                
            # union two node 
            def union(self,node1,node2):
                root1 = self.find(node1) 
                root2 = self.find(node2)
                
                if root1 != root2:
                    
                    self.parent[root2] = root1 
                    self.groups -= 1 
                    
                return None 
            
            # find the root of the given node
            def find(self,node):
                if self.parent[node] == node : return node 
                self.parent[node] = self.find(self.parent[node])
                return self.parent[node]
            
            # check the node1 and node2 in same have connection?
            def connect(self,node1,node2):
                root1 = self.find(node1) 
                root2 = self.find(node2) 
                return root1 == root2 
        
        union_find_set = union_find(  len(isConnected)  )  
        
        for i in range(len(isConnected)): 
            
            for j in range(i+1 , len(isConnected)): 
                
                if isConnected[i][j] == 1 : 
                    union_find_set.union( i , j ) 
        
        
        return union_find_set.groups 
        

""" 
    解法二: BFS
"""

from collections import deque 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        queue = deque() 
        visited = set() 
        groups = 0 
        
        
        for i in range(len(isConnected)): 
            
            if i not in visited:  
                groups += 1  
                
                queue.append(i) 
                visited.add(i) 
                
                while queue : 
                    
                    size = len(queue)

                    for _ in range(size) :
                        
                        node = queue.popleft() 
                        
                        # check all neighbor of the node 
                        for neighbor , connection  in enumerate(isConnected[node]) :
                            
                            if connection and not neighbor  in visited : 

                                visited.add(neighbor)
                                queue.append(neighbor)
        
        return groups
                
        
        
    
    
    
    

S = Solution() 
print(S.findCircleNum( [[1,0,0],[0,1,0],[0,0,1]] ))