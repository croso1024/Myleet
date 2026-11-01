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
    先依開始時間排序,然後用一個 min-heap 記「目前每一間已分配的會議室,何時會空出來」。
    heap 裡放的是結束時間,堆頂就是最早空出來的那一間。

    掃到一場新會議時:
    - 若最早空出來的時間 <= 這場的開始時間,那間可以續用,先彈出再放進這場的結束時間。
    - 否則所有已開的房間都還在開會,必須新開一間,直接把結束時間推進去。

    最後 heap 的大小就是開過的房間數。
    房間只在可以續用時回收,所以這個大小就是最少需要的間數,不必另外記一個最大值。

    複雜度 :
    時間複雜度 O(n log n),排序 O(n log n),每場會議最多一次 heap push / pop。
    空間複雜度 O(n),最壞情況所有會議互相重疊,heap 裡有 n 個結束時間。

    Trade-off :
    掃描線也可以做:把每個 start 記成 +1、每個 end 記成 -1,依時間排序。
    同一時刻要先處理結束、再處理開始,這樣首尾相接才不會多算一間。
    掃完整條線,同時進行的會議數的峰值就是答案。
    和 heap 解的複雜度相同。heap 解比較直接對應「哪一間房間可以續用」。

"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        ordered = sorted(intervals, key=lambda interval: interval[0])
        # 每一間已開會議室的結束時間。堆頂是最早會空出來的那一間。
        free_at = []

        for start, end in ordered:
            if free_at and free_at[0] <= start:
                heapq.heappop(free_at)
            heapq.heappush(free_at, end)

        return len(free_at)


if __name__ == "__main__":
    c = Solution()

    # (intervals, 預期, 說明)
    test_set = [
        (
            [[0, 30], [5, 10], [15, 20]],
            2,
            "官方範例:第二場和第三場可以共用一間,第一場貫穿全程",
        ),
        ([[7, 10], [2, 4]], 1, "官方範例:兩場完全錯開"),
        ([[1, 5]], 1, "邊界:只有一場"),
        ([[1, 5], [5, 10]], 1, "結束時刻等於下一場開始,同一間可以接上"),
        ([[1, 5], [2, 6], [3, 7]], 3, "三場彼此都重疊"),
        (
            [[1, 10], [2, 3], [4, 5], [6, 7]],
            2,
            "長會議蓋住後面三場,短會議彼此不重疊",
        ),
        ([[9, 10], [4, 9], [4, 17]], 2, "輸入未排序,兩場同時開始"),
        ([[1, 2], [2, 3], [3, 4]], 1, "三場首尾相接,一間就夠"),
        (
            [[0, 30], [5, 10], [15, 20], [5, 15]],
            3,
            "時刻 5 同時有三場在進行",
        ),
        ([[13, 15], [1, 13]], 1, "前一場在 13 結束,後一場在 13 開始"),
        ([[1, 2], [1, 2], [1, 2]], 3, "完全相同的三場"),
        ([[8, 10], [1, 3], [2, 6]], 2, "後兩場重疊,第一場可以跟其中一場錯開"),
    ]

    for intervals, expected, note in test_set:
        result = c.minMeetingRooms(intervals)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={intervals} | expected={expected} | got={result}")
