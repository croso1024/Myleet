"""
    題意 :
    總共有 numCourses 門課,編號從 0 到 numCourses - 1。
    prerequisites[i] = [ai, bi] 表示要先修完 bi,才能修 ai。

    若能把所有課都修完,回傳 True,否則回傳 False。
    先修關係若形成環,就無法修完。

    LeetCode 207 · Medium
    URL : https://leetcode.com/problems/course-schedule/

    Example :
    numCourses = 2, prerequisites = [[1,0]]     -> True
    numCourses = 2, prerequisites = [[1,0],[0,1]] -> False

    Constraint :
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    每一對先修關係都不重複

    思路 :
    這一題是 graph 的經典題型. 我還記得以前的解法是需要處理所有課程的待修. 
    一旦某堂課的待修全部完成,才能把該堂課丟回BFS的待搜索空間. 
    
    但這題看起來相當於在圖中尋找環.預期應該要先用 O(P) 建立一次所有節點之間的相依關係圖. 
    當中儲存每一個節點還有多少先修課程才能上. 之後開始走BFS. 如果某堂課先修剩下0堂就可以上. 上完之後,需要知道這堂課是其他哪堂的先修.去扣該堂剩餘的先修數.
    若該堂課的剩餘先修數扣到0, 則能進入BFS. 

    如果全部走訪完. 有任何還沒修到的課程就相當無法完成

    

    

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List , Dict 
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        edge_map : Dict[int , List[int]] = {i : [] for i in range(numCourses)}
        prerequisites_tracker : Dict[int , int] = {i : 0 for i in range(numCourses)} 
        
        
        # pre-fill edge / tracker : 
        for edge in prerequisites : 

            ai , bi = edge 

            # bi is ai's prerequest 
            # edge_map[ai].append(bi)
            edge_map[bi].append(ai) 

            prerequisites_tracker[ai] += 1 
            
        

        # 一開始能上的只有沒有任何先修的課程
        availble_course = deque([course for course in range(numCourses)  if prerequisites_tracker[course] == 0])
        took_course = set(availble_course)
        

        # 只要還有可以上的課程. 
        while availble_course : 
            
            course = availble_course.popleft() 

            for neighbor in edge_map[course] :  

                # 每一個相鄰課程. 如果上完當前課程之後就解鎖全必修,那就可以上. 
                prerequisites_tracker[neighbor] -= 1 

                if prerequisites_tracker[neighbor] == 0 : 
                    took_course.add(neighbor) 
                    availble_course.append(neighbor) 
                
                # 如果上完當前課程還無法解鎖他的全必修,那只能繼續等
                else : 
                    pass 
        
        # 走完所有可以上的課程後, 如果上的課程數等於總課程數則為 True 
        return len(took_course) == numCourses






if __name__ == "__main__":
    c = Solution()

    # ((numCourses, prerequisites), 預期, 說明)
    test_set = [
        ((2, [[1, 0]]), True, "官方範例:先修 0 再修 1"),
        ((2, [[1, 0], [0, 1]]), False, "官方範例:兩門課互相先修"),
        ((1, []), True, "邊界:只有一門課,沒有先修"),
        ((3, []), True, "沒有任何先修關係"),
        ((3, [[1, 0], [2, 1]]), True, "一條鏈:0 -> 1 -> 2"),
        (
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            True,
            "兩條先修路徑在 3 會合",
        ),
        ((3, [[0, 1], [1, 0]]), False, "兩門課成環,第三門課無關"),
        ((3, [[1, 0], [2, 1], [0, 2]]), False, "三門課成環"),
        ((2, []), True, "兩門課彼此獨立"),
        (
            (5, [[1, 0], [2, 0], [3, 1], [4, 3]]),
            True,
            "0 分岔到 1 和 2,1 再接到 3、4",
        ),
    ]

    for args, expected, note in test_set:
        result = c.canFinish(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={args} | expected={expected} | got={result}")
