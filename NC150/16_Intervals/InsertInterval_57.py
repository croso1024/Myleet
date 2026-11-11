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
    已知題目給定的區間都已經按照 start 進行了升序排列且彼此不重疊，把這個事實畫在圖紙上來對照
    不重疊這件事就徹底消除了下一段區間的 start 會不會落在前一段區間之內的問題.
    現在要插入一段新區間. 我的想法是定位新區間的 start / end 會分別影響到原有的哪些區間.

    應該可以用兩次 Binary Search 去找到新區間的影響範圍



    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals : return newInterval

        if newInterval[1] < intervals[0][0] : 
            return newInterval + intervals
        elif newInterval[0] > intervals[-1][1] : 
            return intervals + newInterval
        
        new_start , new_end = newInterval
        result = []
        
        hook = None
        inserted = False
        
        for i in range(len(intervals)): 
            # print(f"Round : {i} result : {result} , hook : {hook}")

            start,end = intervals[i] 
            if inserted : result.append([start,end])

            # 判斷與 new interval 是否有重疊. 
            if hook is None and not ( start <= new_end and new_start <= end ) : 
                # 沒有重疊 , 且 hook 為空就直接 append 
                result.append([start,end]) 
            # hook 目前是空的 , 但有重疊發生, 則設置好 Hook , 且為重疊區間繼續迭代
            elif hook is None : 
                hook = ( min(start , new_start) , max(end,new_end)) 
            
            # hook 存在 , 比較新區間有沒有要跟 Hook 合併 , 若有 , 則繼續擴大hook , 沒有則可以將 hook 貼進並把剩下的回傳了
            elif  end >= hook[0] and start <= hook[1] : 
                hook = ( min(start , hook[0]) , max(end,hook[1]))  
            
            else : 
                result.append([hook[0],hook[1]]) 
                result.append([start,end])
                inserted = True
            
            # print(f"After Round{i} : results {result} hook : {hook}")

        if not inserted  and hook is not None : 
            result.append([hook[0],hook[1]])

        return result


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
