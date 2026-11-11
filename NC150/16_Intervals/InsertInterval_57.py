"""
    題意 :
    給定一組已經依起點升序排好、彼此不重疊的區間 intervals。
    intervals[i] = [starti, endi]。
    另給一個新區間 newInterval = [start, end]。

    把 newInterval 插進去,維持起點升序,並且合併有重疊的區間。
    只在端點相接也算要合併,例如 [1,5] 與 [5,7] 合併成 [1,7]。
    不用改原本的 intervals,回傳插入並合併後的新陣列。

    LeetCode 57 · Medium
    URL : https://leetcode.com/problems/insert-interval/

    Example :
    intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        -> [[1,2],[3,10],[12,16]]

    Constraint :
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^5
    intervals 已依 starti 升序,且彼此不重疊
    newInterval.length == 2
    0 <= start <= end <= 10^5

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        pass


if __name__ == "__main__":
    c = Solution()

    # (intervals, newInterval, 預期, 說明)
    # 每次呼叫都複製輸入,實作改到測資本身不會留到下一題
    test_set = [
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
            "官方範例:重疊前段,後段保持不變",
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
            "官方範例:一次蓋過中間三個區間",
        ),
        ([], [5, 7], [[5, 7]], "邊界:原本沒有任何區間"),
        ([[1, 5]], [2, 3], [[1, 5]], "新區間完全落在既有區間裡面"),
        ([[1, 5]], [6, 8], [[1, 5], [6, 8]], "接在最後,中間有空隙"),
        ([[1, 5]], [0, 0], [[0, 0], [1, 5]], "插到最前面,沒有重疊"),
        ([[1, 5]], [0, 3], [[0, 5]], "與第一個區間的前段重疊"),
        ([[1, 5]], [5, 7], [[1, 7]], "端點相接,要合併"),
        (
            [[1, 3], [6, 9]],
            [4, 5],
            [[1, 3], [4, 5], [6, 9]],
            "插進空隙,不與前後重疊",
        ),
        ([[1, 5], [6, 8]], [0, 9], [[0, 9]], "新區間蓋過全部"),
        ([[3, 5], [6, 9]], [1, 2], [[1, 2], [3, 5], [6, 9]], "插到最前面且沒有碰到"),
    ]

    for intervals, new_interval, expected, note in test_set:
        result = c.insert(
            [interval[:] for interval in intervals],
            new_interval[:],
        )
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       intervals={intervals} | new={new_interval}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
