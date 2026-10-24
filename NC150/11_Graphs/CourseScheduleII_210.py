"""
    題意 :
    總共有 numCourses 門課,編號從 0 到 numCourses - 1。
    prerequisites[i] = [ai, bi] 表示要先修完 bi,才能修 ai。

    回傳一種可以把所有課修完的順序。
    有多種合法順序時,回傳任何一種都可以。
    先修關係若形成環,就無法修完,回傳空 list。

    LeetCode 210 · Medium
    URL : https://leetcode.com/problems/course-schedule-ii/

    Example :
    numCourses = 2, prerequisites = [[1,0]]                 -> [0,1]
    numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] -> [0,1,2,3]
    numCourses = 1, prerequisites = []                      -> [0]

    Constraint :
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    每一對先修關係都不重複

    思路 :
    這一題用BFS, 同時記錄下每一門課的相依課程數. 只有所有先修都完成的,才能加入修習.
    同時需要一個Array把修習紀錄加入陣列. 
    如果全部都能修完就回傳該陣列,否則回傳空陣列. 

    時間複雜度 , 設課程數為N : 
    - 建構修課關係圖 , 已知 Prerequisites 為 N^2 , 需要 O(N^2) 時間建圖
    - 紀錄每一堂課的相依關係 (修完後可以修哪些) , Worse Case O(N^2) 空間 
    - BFS 開始修課 , O(N)時間


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List,Dict,Set
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # prerequisites_map : { course_i : [ course that require course_i ] }
        # prerequisites_count : {course_i : amount of prerequest course }
        prerequisites_map : Dict[int , Set[int]] = {} 
        prerequisites_count : Dict[int , int] = {} 
        
        # bi 修完才能修 ai 
        for ai , bi in prerequisites : 

            if bi not in prerequisites_map : prerequisites_map[bi] = set() 
            prerequisites_map[bi].add(ai) 

            if ai not in prerequisites_count : prerequisites_count[ai] = 0 
            prerequisites_count[ai] += 1 
        
        # BFS , 只能從沒有任何先修的開始上
        
        queue = deque([i for i in range(numCourses) if i not in prerequisites_count])
        course_path = [] 

        while queue : 
            # 可以上的課程
            course = queue.popleft()
            course_path.append(course) 
            # 看一下能解鎖哪些課程
            # 如果某堂課的先修全部完成了 , 就可以加入待修清單
            for next_course in prerequisites_map.get(course,[]): 
                if prerequisites_count[next_course] == 1 : 
                    del prerequisites_count[next_course]
                    queue.append(next_course)
                else : 
                    prerequisites_count[next_course] -= 1 
        
        # 如果所有課程都能修的到 , 就回傳修課軌跡,否則回傳空Array 
        return course_path if len(course_path) == numCourses else [] 


def is_valid_order(num_courses, prerequisites, order):
    """有解時,任一滿足先修關係的排列都算對。"""
    if order is None or len(order) != num_courses:
        return False
    if sorted(order) != list(range(num_courses)):
        return False
    index = {course: i for i, course in enumerate(order)}
    for course, prereq in prerequisites:
        if index[prereq] >= index[course]:
            return False
    return True


if __name__ == "__main__":
    c = Solution()

    # ((numCourses, prerequisites), 一種合法順序, 說明)
    # 預期為 [] 表示無解,必須回傳空 list。
    # 其餘情況任一合法順序都算對,不必和範例順序相同。
    test_set = [
        ((2, [[1, 0]]), [0, 1], "官方範例:先修 0 再修 1"),
        (
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
            [0, 1, 2, 3],
            "官方範例:0 分岔到 1 和 2,兩者都要在 3 之前",
        ),
        ((1, []), [0], "官方範例:只有一門課"),
        ((2, [[1, 0], [0, 1]]), [], "兩門課互相先修"),
        ((3, [[1, 0], [2, 1]]), [0, 1, 2], "一條鏈:0 -> 1 -> 2"),
        ((3, []), [0, 1, 2], "沒有任何先修,三種排列都合法"),
        ((2, []), [0, 1], "兩門課彼此獨立"),
        ((3, [[0, 1], [1, 0]]), [], "兩門課成環,第三門課無關"),
        ((3, [[1, 0], [2, 1], [0, 2]]), [], "三門課成環"),
        (
            (4, [[1, 0], [2, 1], [3, 2]]),
            [0, 1, 2, 3],
            "四門課一條鏈,只有一種順序",
        ),
    ]

    for args, expected, note in test_set:
        num_courses, prerequisites = args
        result = c.findOrder(num_courses, [edge[:] for edge in prerequisites])
        if expected == []:
            passed = result == []
        else:
            passed = is_valid_order(num_courses, prerequisites, result)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={args}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
