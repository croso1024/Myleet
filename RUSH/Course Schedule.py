from typing import List 


# cycle detection algorithms , we can implement it by DFS ,or BFS


# DFS solution 
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        canComplete = True 
        # build the graph first , 先修課程指向修完後才可修的
        graph = dict()
        havePrerequest = set()
        for (ai,bi) in prerequisites :
            if bi in graph: graph[bi].append(ai)  
            else : graph[bi] = [ai] 
            havePrerequest.add(ai) 
        
        # 標記已經走過得節點 
        visited = set() 
        
        # DFS , 只有在該node不在visited時才會加入 , 如果遇到一個已經存在於path的節點就代表無法全部修完
        def dfs(node ,path:set):
            
            nonlocal canComplete
            if not node in graph : return 
            for neighbor in graph[node] : 
                
                if neighbor in path:  
                    canComplete = False 
                    
                if not neighbor in visited :
                    
                    path.add(neighbor)
                    visited.add(neighbor)
                    dfs(neighbor , path) 
                    path.remove(neighbor) 
            
            return 
        
        for i in range(numCourses): 
            
            if not i in havePrerequest : 
                visited.add(i) 
                dfs(i , {i})                    

        if len(visited) == numCourses : 
            return canComplete
        else : 
            return False 
        

# DFS solution 
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build graph
        graph = {}
        for (ai ,bi) in prerequisites: 
            if bi in graph: graph[bi].append(ai)
            else : graph[bi] = [ai] 
        
        visited = set() 
        path = set() 
        canComplete = True 
        
        def dfs(node,path:set):
            nonlocal canComplete  
            
            if node in path : 
                canComplete = False 
                return 
            
            if not canComplete or node in visited : 
                return

            visited.add(node)
            if node in graph :  

                path.add(node)
                for neighbor in graph[node]: 
                    dfs(neighbor,path)
                path.remove(node)

            return             
            
        
        for i in range(numCourses): 
            
            dfs(i ,path) 
        
        return canComplete
        
        
# BFS solution 
from collections import deque 
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build graph and calculate the entre degree 
        graph = dict() 
        indegree = dict() 
        queue = deque() 
        visited = set() 
        
        for (ai,bi) in prerequisites :
            
            if bi in graph: graph[bi].append(ai)
            else : graph[bi] = [ai]

            if ai in indegree: indegree[ai] += 1 
            else : indegree[ai] = 1 
        
        
        for i in range(numCourses): 
            # 如果這個課程是有先修的就跳過
            if i in indegree : continue 
            
            queue.append(i) 
            visited.add(i)
            
            while queue : 
                size = len(queue) 
                
                for _ in range(size):
                    
                    node = queue.popleft() 

                    for neighbor in graph.get(node , []) : 
                        
                        indegree[neighbor] -= 1 

                        if indegree[neighbor] == 0 : 
                            
                            visited.add(neighbor)
                            queue.append(neighbor) 
        
        return len(visited) == numCourses