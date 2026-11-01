"""
    題意 :
    給定若干會議的時間區間 intervals,其中 intervals[i] = [starti, endi]。
    回傳要讓所有會議都能召開,最少需要幾間會議室。

    一場會議的結束時間到了,那間會議室就可以給下一場用。
    結束時刻與下一場的開始時刻相同,算同一間可以接上,不需要多開一間。

    LeetCode 253 · Medium
    URL : https://leetcode.com/problems/meeting-rooms-ii/
    ※ 此題在 LeetCode 為 Premium 鎖定題。
      題意採用 NeetCode 的通用敘述。
    免費可練 : https://neetcode.io/problems/meeting-schedule-ii

    Example :
    intervals = [[0,30],[5,10],[15,20]] -> 2
    intervals = [[7,10],[2,4]]          -> 1

    Constraint :
    1 <= intervals.length <= 10^4
    0 <= starti < endi <= 10^6

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (intervals, 預期, 說明)
    test_set = [
        (
            [[0, 30], [5, 10], [15, 20]],
            2,
            "官方範例",
        ),
        ([[7, 10], [2, 4]], 1, "官方範例"),
        ([[1, 5]], 1, "邊界:只有一場"),
        ([[1, 5], [5, 10]], 1, "結束時刻等於下一場開始"),
        ([[1, 5], [2, 6], [3, 7]], 3, "三場時間重疊"),
        (
            [[1, 10], [2, 3], [4, 5], [6, 7]],
            2,
            "一場較長,三場較短",
        ),
        ([[9, 10], [4, 9], [4, 17]], 2, "輸入未排序"),
        ([[1, 2], [2, 3], [3, 4]], 1, "三場首尾相接"),
        (
            [[0, 30], [5, 10], [15, 20], [5, 15]],
            3,
            "四場會議",
        ),
        ([[13, 15], [1, 13]], 1, "前一場結束時刻等於後一場開始"),
        ([[1, 2], [1, 2], [1, 2]], 3, "三場時間完全相同"),
        ([[8, 10], [1, 3], [2, 6]], 2, "輸入未排序"),
    ]

    for intervals, expected, note in test_set:
        result = c.minMeetingRooms(intervals)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={intervals} | expected={expected} | got={result}")
