""" 
    思路 : 
        這一題屬於東哥在圖論算法說明"環檢測算法"的範例，但一開始我以為這一題中，每一個課程最多只有一個先修,
        接著直接做了BFS , 想看最終能夠走到的節點數量與課程數量是否相等 -> 但因為同一堂課程可能有多個預修 ,所以這個方法失敗

        從東哥的思路 , 實際上這一題屬於檢查graph中有沒有cycle , 因為如果有循環依賴代表不可能修完所有課程 ,
        這一類檢測循環的算法在實務上有很大用途 -> 例如編譯器檢查import語法的循環依賴關係。
        
        實際上這一題需要用到類似回溯算法的框架 , 也就是"做選擇"與"撤銷選擇" , 用類似二元樹的架構
        保持一個在graph上游走的指標 
        
        因此這一題我們使用recursion來做DFS/BFS  , 除了visited矩陣避免重複訪問 , 還用一個Path陣列保存目前在樹中遊走的指標經過了哪些節點
"""

from typing import List 
from collections import deque

""" 
    解法一, 遞迴調用DFS , 在時間上不太好 , 空間上普通 , 但我覺得有蠻多可以優化的地方
"""
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #　第一步先建立一張graph,在這一題可以用adjaency list就好 
        graph = [  [] for i in range(numCourses)  ]
        #  ai的先修條件為bi
        for (ai , bi) in prerequisites: graph[bi].append(ai) 
        # 用一個hashset來保存已經看過的節點 
        visited = set() 
        # 預設答案為True,如果發現cycle才要改成false 
        solution = True
        
        # DFS 用來遍瀝整個graph , 同時我們在進出節點的部份操作path , 
        # 因為這一題不是要返回路徑,因此path我使用set , 這樣比較容易判斷是否出現了cycle
        def DFS(node , path:set): 
            nonlocal solution 
            # 進來後先看是不是有在path上 , 有就代表出現cycle , 答案為False了
            if node in path : solution = False 
            if node in visited or not solution : return 

            visited.add(node)
            path.add(node)
            
            for neighbor in graph[node] : 
                DFS(neighbor , path ) 
            
            path.remove(node)
            
            
        # 因為這張graph可能不會全部連接 , 需要用for-loop對每一個節點都調用過 
        for i in range(numCourses): DFS(i , set())

        return solution

""" 
    解法二, 遞迴調用DFS , 把path_set改為global varaible來操作
"""
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #　第一步先建立一張graph,在這一題可以用adjaency list就好 
        graph = [  [] for i in range(numCourses)  ]
        #  ai的先修條件為bi
        for (ai , bi) in prerequisites: graph[bi].append(ai) 
        # 用一個hashset來保存已經看過的節點 
        visited = set() 
        path_set = set() 
        # 預設答案為True,如果發現cycle才要改成false 
        solution = True
        
        # DFS 用來遍瀝整個graph , 同時我們在進出節點的部份操作path , 
        # 因為這一題不是要返回路徑,因此path我使用set , 這樣比較容易判斷是否出現了cycle
        def DFS(node , path:set): 
            nonlocal solution 
            # 進來後先看是不是有在path上 , 有就代表出現cycle , 答案為False了
            if node in path : solution = False 
            if node in visited or not solution : return 

            visited.add(node)
            path.add(node)
            
            for neighbor in graph[node] : 
                DFS(neighbor , path ) 
            
            path.remove(node)
            
        # 因為這張graph可能不會全部連接 , 需要用for-loop對每一個節點都調用過 
        for i in range(numCourses): DFS(i , path_set)

        return solution

""" 
    解法三. BFS
        這一題BFS解法很精妙 , 而且我覺得非常容易理解  , 基本上就是計算每一堂課所需要的先修課程數量 
        , 我們先將那些不需要先修的課程加入queue , 當我們從queue拿出節點 , 就去看他的鄰居
        
        把鄰居的先修數量 -1 後來看( 因為已經修完我們所在節點的課 ) : 
        如果鄰居的先修數量==0 -> 加入隊列
        如果鄰居的先修數量>0  , 就繼續
        以這樣的方式走訪完後 , 節點的數量等於課程數量就是true 
        
        這個解法在速度與空間上都比DFS更好
        
        
        note : 實際上這一題甚至不需要complete set , 因為只有preCourse == 0 才會被加入 , 所有節點只會有一次==0
""" 


from collections import deque
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        # 先建立每一堂課需要的先修課程數量
        preCourse = [ 0 for i in range(numCourses)  ]
        # 以及每一堂課修完後可以去修的(maybe修完這門還不夠)
        nextCourse = [ [] for i in range(numCourses)  ]
        for (ai ,bi) in prerequisites:
            # 課程ai的先修是bi 
            preCourse[ ai ] += 1 
            nextCourse[ bi ].append(ai)
        
        queue = deque() 
        # 把所有不需要先修的課程加入queue
        for idx, course in enumerate(preCourse): 
            if course == 0 : queue.append(idx)
        
        # complete set 用來紀錄已經完成的課程
        complete = set() 
        
        # 走BFS
        while queue : 
            
            cur_course = queue.popleft()
            complete.add(cur_course) 
            
            for neighbor in nextCourse[cur_course]: 

                if neighbor in complete : continue
                
                preCourse[neighbor] -= 1 
                if preCourse[neighbor] == 0 :    
                    queue.append(neighbor)
        
        return len(complete) == numCourses
                    
            
