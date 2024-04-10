from typing import List 

# BFS + in-degree calculate
from collections import deque
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build the graph 
        graph = dict() 
        havePrerequest = set()
        indegree = dict() 
        takeSeq = [] 
        
        for (ai,bi) in prerequisites: 
            
            if bi in graph: graph[bi].append(ai)
            else : graph[bi] = [ai] 
            if ai in indegree : indegree[ai] += 1 
            else : indegree[ai] = 1 
            havePrerequest.add(ai) 
        
        def BFS(course): 
            queue = deque() 
            queue.append(course) 
            takeSeq.append(course)
                        
            while queue : 
                
                size = len(queue) 
                
                for _ in range(size): 
                    
                    cur_course = queue.popleft() 
                    
                    for neighbor in graph.get(cur_course , []) : 
                        
                        if indegree[neighbor] == 1 : 
                            
                            indegree[neighbor] = 0
                            takeSeq.append(neighbor) 
                            queue.append(neighbor) 
                        
                        else : indegree[neighbor] -= 1 
            return 
        
        for course in range(numCourses):
            
            if not course in havePrerequest : 

                BFS(course) 
        
        return takeSeq if len(takeSeq) == numCourses else [] 
                    
        
        
# DFS post order solution 
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = dict() 
        path = set() 
        visited = set() 
        haveCycle = False 
        takeSeq = [] 
        
        for (ai,bi) in prerequisites: 
            if bi in graph : graph[bi] .append(ai)
            else : graph[bi] = [ai] 
        
        def dfs(node,path:set): 
            nonlocal haveCycle
            
            if node in path : 
                haveCycle = True 
                return 
            
            if node in visited or haveCycle : return 

            visited.add(node)
            path.add(node)

            for neighbor in graph.get(node , []): 
                
                dfs(neighbor , path) 
            
            path.remove(node)
            
            takeSeq.append(node)

            return 
        
        
        for i in range(numCourses):
            
            dfs(i , path)
        
        if haveCycle : return [] 
        else : 
            
            takeSeq.reverse()
            return takeSeq 
                        