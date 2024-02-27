from typing import List 

from collections import deque
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 如果能修完所有課程 , 找出修課順序 
        
        # 1. build Graph 
        # 2. 計算所有節點的in-degree , 代表其有多少先修 
        # 3. 把不需要先修的課程加入Queue , 開始展開BFS 
        # 4. 在探訪neighbor的過程 , 降低其in-degree值 , 代表修完了其中一堂先修 , 需要的先修數量-1 , 如果=0 ,加入Queue
        # 5. 依照從Queue拿出的順序 , 就是合法的拓撲排序 , 但最終要看這個排序len() ==? numCourse 代表是否修的完
        
        # 取得有向圖 , 以及每個節點的in-degree 
        def buildGraph(numCourses ,  edges) : 
            graph = dict() 
            indegree = [0 for i in range(numCourses)]
            for dst , src  in edges : 
                
                if src in graph : graph[src].append(dst)
                else : graph[src] = [dst]   
                
                # 目的地每次被提出來就是代表他有一個先修
                indegree[dst] += 1
            
            return graph , indegree
        
        
        graph , indegree = buildGraph(numCourses=numCourses , edges=prerequisites) 
        queue = deque()
        topo_sort = [] 
        # complete = set() 
        # 把所有不用先修的都先加入Queue 
        for i in range(len(indegree)) : 
            if indegree[i] == 0 : queue.append(i) 
                
        
        # 開始BFS
        while queue : 
            
            course = queue.popleft()
            # complete.add(course) 
            topo_sort.append(course)
            
            # 該堂課不會影響其他課程
            if not course in graph : continue 
            
            for next_course in graph[course] : 
                
                # if next_course in complete : continue 
                
                indegree[next_course] -= 1 
                if indegree[next_course] == 0 : 
                    queue.append(next_course)
        
        return topo_sort if len(topo_sort) == numCourses else [] 
                