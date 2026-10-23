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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass


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
