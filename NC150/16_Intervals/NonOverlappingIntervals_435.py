"""
    題意 :
    給定一組區間 intervals,其中 intervals[i] = [starti, endi]。
    回傳最少要移除幾個區間,才能讓剩下的區間彼此都不重疊。

    只在端點相接的兩個區間不算重疊,例如 [1,2] 與 [2,3]。

    LeetCode 435 · Medium
    URL : https://leetcode.com/problems/non-overlapping-intervals/

    Example :
    intervals = [[1,2],[2,3],[3,4],[1,3]] -> 1
    intervals = [[1,2],[1,2],[1,2]]       -> 2
    intervals = [[1,2],[2,3]]             -> 0

    Constraint :
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4

    思路 :
    回傳至少要移除幾個區間才能不重疊!? 
    預期先 Sort , 按照(start,end)去排序. 
    這樣 , 按照排序完成的結果去走,可以知道下一個Interval的起始點序列是單調遞增的. 

    每一次檢查新的 Interval , 去看有沒有和當前自己身上的重疊 , 有的話就砍掉 end 比較長的,確保對後續影響更小.
    在砍掉 end 較長的情況下,又已知下一個 Interval 的起始一定更後面. 
    Case.1 
    |----| (i1)
      |-----|  (i2) 
    這時候砍掉 i2 , 因為i2對後面影響更大. 下一個 interval.start 必然 >= i2.start 
    Case.2 
    |----| (i1)
     |--|  (i2) , 砍掉 i1 , 同樣是因為 i1 對後面影響更大, 下一個 interval.start 必然 >= i2.start 
    按照這個思路 , 逐步添加與移除即可


    複雜度 : Sorting , 加上走一輪 O(NLogN) , 空間則僅有常數的額外儲存 O(1)

    Trade-off :

"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort() 

        delete_count = 0
        cur = intervals[0] 

        for i in range(1,len(intervals)) : 
            next = intervals[i] 

            # 如果 next 與 當前完全沒有重疊(允許端點相接),那直接過.
            if next[0] >= cur[1] : 
                cur = next
                continue

            # 否則就是有重疊, 檢查誰 end 短就留誰. 
            delete_count += 1 
            if next[1] < cur[1] : 
                cur = next 
        
        return delete_count

if __name__ == "__main__":
    c = Solution()

    # (intervals, 預期, 說明)
    # 每次呼叫都複製 intervals,實作改到測資本身不會留到下一題
    test_set = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1, "官方範例:移掉 [1,3] 即可"),
        ([[1, 2], [1, 2], [1, 2]], 2, "官方範例:三個完全相同的區間"),
        ([[1, 2], [2, 3]], 0, "官方範例:端點相接不算重疊"),
        ([[1, 5]], 0, "邊界:只有一個區間"),
        ([[5, 6], [1, 2], [3, 4]], 0, "彼此不重疊,輸入沒有排序"),
        ([[1, 10], [2, 3], [4, 5], [6, 7]], 1, "一個長區間蓋住三個短區間"),
        ([[1, 2], [1, 3], [1, 4]], 2, "起點相同、終點不同"),
        ([[1, 3], [2, 4], [3, 5], [4, 6]], 2, "相鄰兩兩重疊的一串"),
        ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2, "五個區間交錯重疊"),
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2, "長短混合,輸入順序打亂"),
        ([[-3, -1], [-2, 0], [0, 2]], 1, "含負數座標"),
    ]

    for intervals, expected, note in test_set:
        result = c.eraseOverlapIntervals([interval[:] for interval in intervals])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={intervals} | expected={expected} | got={result}")
