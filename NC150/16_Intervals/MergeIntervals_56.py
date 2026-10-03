"""
    題意 :
    給定若干區間 intervals,其中 intervals[i] = [starti, endi]。
    把所有重疊的區間合併,回傳合併後的區間。
    合併後的區間彼此不重疊,而且要蓋住原本的每一段。

    兩段只要有交集就算重疊,端點相接也算。
    例如 [1,4] 與 [4,5] 要合成 [1,5]。
    區間之間的順序不限,區間內部維持 [start, end]。

    LeetCode 56 · Medium
    URL : https://leetcode.com/problems/merge-intervals/

    Example :
    intervals = [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]                 -> [[1,5]]

    Constraint :
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


def canon(intervals: List[List[int]]):
    """區間彼此的順序不影響對錯;每段內部的 [start, end] 要保留。"""
    if intervals is None:
        return None
    return sorted(tuple(pair) for pair in intervals)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明) —— 只忽略區間彼此的順序
    test_set = [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
            "官方範例:前兩段重疊,後面兩段各自獨立",
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
            "官方範例:端點相接也要合併",
        ),
        ([[5, 8]], [[5, 8]], "邊界:只有一段"),
        ([[0, 0]], [[0, 0]], "邊界:起點終點都是 0"),
        (
            [[1, 2], [4, 5]],
            [[1, 2], [4, 5]],
            "完全沒有重疊",
        ),
        (
            [[4, 7], [1, 4]],
            [[1, 7]],
            "輸入未排序,端點相接",
        ),
        (
            [[1, 10], [2, 6], [3, 4]],
            [[1, 10]],
            "後段完全被前段包住",
        ),
        (
            [[1, 2], [2, 3], [3, 4]],
            [[1, 4]],
            "多段只在端點相接,串成一段",
        ),
        ([[1, 3], [1, 3]], [[1, 3]], "完全相同的兩段"),
        (
            [[1, 4], [0, 2], [3, 5]],
            [[0, 5]],
            "三段交錯,合成一段",
        ),
        (
            [[8, 10], [1, 3], [15, 18], [2, 6]],
            [[1, 6], [8, 10], [15, 18]],
            "官方範例打亂順序",
        ),
        (
            [[1, 4], [0, 0]],
            [[0, 0], [1, 4]],
            "點區間與後面的段不相交",
        ),
        (
            [[0, 10000], [1, 2]],
            [[0, 10000]],
            "邊界:數值上下限,短段被長段包住",
        ),
    ]

    for intervals, expected, note in test_set:
        result = c.merge(intervals)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
