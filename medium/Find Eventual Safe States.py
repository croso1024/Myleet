"""
    Given a graph by adajency list , and define the node is a 'safe node' 
    if 'all path' start from the  node can directed to a terminal node(not any outgoint edge) .  
    we need to return an array contain all safe node in the graph , 

    basically i think a recursion approach is effective , 
    we use a hashtable to represent whether a node is 'safe' , 
    and use depth-first search to expand the tree , 
    update the node property when jump out the recursion
    
""" 
from typing import List 
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        table = [False for i in range(len(graph))] 
        visited = set() 
        def dfs(node): 
            if not graph[node]  : 
                table[node] = True 
                return 
            safe = True 
            for neighbor in graph[node]: 

                if not neighbor in visited : 
                    visited.add(neighbor) 
                    dfs(neighbor) 
                    if not table[neighbor] : safe = False 
                    
                elif not table[neighbor] : safe = False  

            table[node] = safe 
            return 

        for node in range(len(graph)): 
            if not node in visited : 
                visited.add(node)
                dfs(node) 

        return filter( lambda i : table[i] , list(range(len(graph)))   )                 

                        