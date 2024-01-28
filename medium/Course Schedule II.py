""" 
    思路: 
        這一題是基於Course schedule I的進階, 除了要知道是否可以修完全部的課之外,
        還要給出任意一條可以完成全部課程的修課順序 . 
        這一題我要嘗試使用DFS和BFS都來解 , 這類問題稱為"拓撲排序"
        
        
        DFS中求拓撲排序的概念相當絕 , 讓人叫絕的程度 , 透過post-order的位置來加入track 
        並將其反轉。
        
        概念上 :  
            post-order在二元樹中就是完成左右子樹後才會走到root , 對應於這一題具有依賴關係的Graph , 
            post-order在此可以對應成為 : 一個任務必須等待他所有的依賴任務都完成才可以執行 
            
            舉例來說  a課程需要先修b , b課程需要先修c , 這樣會是一個  c->b->a的關係 
            直接做post-order可能會得到 [a , b , c] , 將其反轉就是拓撲排序
        
        
        而對於BFS來說則更直接一點,被加入queue的時間點代表該堂課是可以修的 , 因此在相同時間點維護一個track就好
        
"""

""" 
    解法一. DFS , 一邊進行cycle的判斷一邊做拓撲排序
    
    --> 速度還不錯 , 空間就不太好了
"""

from typing import List 

class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        # 先建立Graph ,Adjaency list 
        # 注意我的graph的定義 , 是 bi -> ai 
        nextCourse = [ [] for i in range(numCourses) ]        
        for (ai, bi) in prerequisites: 
            nextCourse[bi].append(ai) 
        
        # 紀錄cycle的旗標 , 如果發現cycle就可以準備return答案了 
        cycle = False 
        # 紀錄完成的課程
        complete = set() 
        # 紀錄答案的軌跡
        track = [] 
        # 紀錄當前探尋的軌跡,用以判斷是否有cycle
        path = set()
        
        def DFS(node , path:set):

            nonlocal cycle , track 

            if node in path : 
                cycle = True 
                return 

            elif node in complete or cycle :
                return 
            
            # 在進入節點與離開節點部份操作path 
            complete.add(node)
            path.add(node)

            for neighbor in nextCourse[node]: 
                DFS(neighbor , path) 
            
            path.remove(node) 
            
            # 在post-order的部份進行track的增加 
            track.append(node)        
            
        
        # 使用for-loop走訪每一個節點進行DFS展開
        for i in range(numCourses): DFS(i , path)
        
        # 如果沒有cycle,那track就是解
        track.reverse()
        return track if not cycle else []
        
        
""" 
    解法二. BFS , 基於進入queue的時機點加入track 
    
    時間和DFS差不多 , 空間優勢很大
"""
from collections import deque
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # 先計算每一個節點的相依課程數量 , 以及建立adjacency list 
        preCourse = [0] * numCourses
        nextCourse = [ [] for i in range(numCourses) ]

        for (ai ,bi) in prerequisites: 
            preCourse[ai] += 1 
            nextCourse[bi].append(ai) # 相依關係是 bi->ai
            
        Queue = deque() 
        complete = set() 
        Track = [] 
        # 先把所有不用先修的加入queue ,track 
        for idx , course in enumerate(preCourse): 

            # 在課程中為0 , 實際意義為該節點沒有被任何其他節點"指向"
            # 所以在下面實際上出現在 nextCourse[..]的 , 都至少preCourse >=1 
            if course == 0 : 
                
                Queue.append(idx) 
                Track.append(idx) 
        
        while Queue: 
            
            cur_course = Queue.popleft() 
            complete.add(cur_course) 
            
            for neighbor in nextCourse[cur_course]: 
                
                if neighbor in complete : continue
                
                preCourse[neighbor] -= 1 
                
                if preCourse[neighbor] == 0 : 
                    Queue.append(neighbor) 
                    Track.append(neighbor) 
        
        return Track if len(complete) == numCourses else [] 
        
        