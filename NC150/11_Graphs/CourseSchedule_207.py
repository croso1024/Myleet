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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


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
