from typing import List 

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 需要先修 bi 才能修 ai  , 返回是否能夠修完所有課程 -> detect是否有cycle 
        
        # 先建構完整的Graph , directed graph , 使用 adajency list , 紀錄每一個節點單向可到達的節點
        def buildGraph( edges ) : 
            
            graph = dict()
            
            for dst ,src in edges : 
                
                if src in graph: graph[src].append(dst) 
                else : graph[src] = [dst] 
            
            return graph 
        
        def dfs(node): 
            nonlocal graph , cycle 
            if not node in graph : return 
            in_stack[node] = True 
            visited.add(node) 
            for neighbor in graph[node] : 
                
                if in_stack[neighbor] : 
                    cycle = True 
                    
                elif not neighbor in visited :
                     
                    dfs(neighbor) 
            
            in_stack[node] = False                     
            return 
                
        
        # 單向圖 , 所以我不打算使用 visited set 來避免走回頭路 
        # in_stack , 用來紀錄說哪些節點目前正在stack中
        graph = buildGraph(prerequisites) 
        in_stack = [False for i in range(numCourses)]
        visited = set() 
        cycle = False 

        for i in range(numCourses): 
            
            dfs(i) 
            if cycle : break 
                    
        return not cycle 