"""
    題意 :
    給定若干會議的時間區間 intervals,其中 intervals[i] = [starti, endi]。
    判斷一個人是否能「參加所有會議」,可以則回傳 True,否則回傳 False。

    兩場會議的時間若有重疊就無法同時參加。
    結束時刻與下一場的開始時刻相同,不算重疊。
    intervals 為空時,回傳 True。

    LeetCode 252 · Easy
    URL : https://leetcode.com/problems/meeting-rooms/
    ※ 此題在 LeetCode 為 Premium 鎖定題。
      題意採用 NeetCode 的通用敘述。
    免費可練 : https://neetcode.io/problems/meeting-schedule

    Example :
    intervals = [[0,30],[5,10],[15,20]] -> False
    intervals = [[7,10],[2,4]]          -> True

    Constraint :
    0 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti < endi <= 10^6

    思路 :
    看起來是問 , 所有區間是否有任何重疊.
    直覺想法是先依照 start_i 做排序 , 開始檢查區間是否重疊



    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) in [0,1] : return True 
        
        intervals.sort() 
        current_end = intervals[0][1]

        for i in range(1 , len(intervals)) : 
            
            start ,end = intervals[i]
            
            if current_end > start : return False 

            # start >= current_end , 直接承接下一個 end : end >= start >= current_end 
            current_end = end 

        return True 


if __name__ == "__main__":
    c = Solution()

    # (intervals, 預期, 說明)
    # 每次呼叫都複製 intervals,實作改到測資本身不會留到下一題
    test_set = [
        ([[0, 30], [5, 10], [15, 20]], False, "官方範例:[0,30] 與其他兩場重疊"),
        ([[7, 10], [2, 4]], True, "官方範例:輸入未排序,兩場不重疊"),
        ([[5, 8], [9, 15]], True, "NeetCode 範例:中間有空檔"),
        ([], True, "邊界:沒有任何會議"),
        ([[1, 2]], True, "邊界:只有一場會議"),
        ([[1, 5], [5, 10]], True, "邊界:前一場結束時刻 == 下一場開始時刻"),
        ([[1, 5], [4, 10]], False, "兩場有部分重疊"),
        ([[1, 10], [2, 3]], False, "一場完全包在另一場裡面"),
        ([[2, 3], [1, 10]], False, "包含關係,且內層的那場排在輸入前面"),
        ([[1, 2], [1, 3]], False, "兩場開始時間相同"),
        ([[1, 2], [1, 2]], False, "兩場完全相同"),
        ([[1, 2], [3, 4], [2, 3]], True, "輸入亂序,排好後首尾相接成一條鏈"),
        ([[1, 3], [2, 4], [5, 6]], False, "重疊發生在最前面兩場"),
        ([[1, 2], [3, 4], [5, 6], [4, 7]], False, "重疊發生在排序後的最後面"),
        ([[0, 1], [1, 1000000]], True, "邊界:涵蓋數值範圍的兩端,首尾相接"),
        ([[i, i + 1] for i in range(0, 10000)], True, "規模上限:10^4 場會議,依序首尾相接"),
    ]

    for intervals, expected, note in test_set:
        result = c.canAttendMeetings([iv[:] for iv in intervals])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        shown = intervals if len(intervals) <= 6 else f"<{len(intervals)} intervals>"
        print(f"       intervals={shown}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
