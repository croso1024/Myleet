"""
    題意 :
    給定一個有 n 個節點的網路,節點編號 1 到 n。
    times[i] = (ui, vi, wi) 表示一條「有向邊」:訊號從 ui 傳到 vi 需要 wi 單位時間。

    現在從節點 k 發出訊號,回傳「所有節點都收到訊號」所需的最短時間。
    若有任何節點收不到訊號,回傳 -1。

    LeetCode 743 · Medium
    URL : https://leetcode.com/problems/network-delay-time/

    Example :
    times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 -> 2
    times = [[1,2,1]], n = 2, k = 1                 -> 1
    times = [[1,2,1]], n = 2, k = 2                 -> -1

    Constraint :
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    所有 (ui, vi) 組合互不重複(沒有重邊)

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (times, n, k, 預期, 說明)
    # 每次呼叫都複製 times,實作改到測資本身不會留到下一題
    test_set = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2, "官方範例:從 2 出發,最遠的 4 要 2"),
        ([[1, 2, 1]], 2, 1, 1, "官方範例:單一條邊"),
        ([[1, 2, 1]], 2, 2, -1, "官方範例:有向邊,反方向傳不過去"),
        (
            [[1, 2, 10], [1, 3, 1], [3, 2, 1]],
            3,
            1,
            2,
            "陷阱:直達邊較慢,繞路 1->3->2 才是最短",
        ),
        (
            [[1, 2, 1], [1, 3, 4], [2, 3, 1], [3, 4, 1]],
            4,
            1,
            3,
            "陷阱:3 先以距離 4 進 heap,後來被 2 更新成 2,舊的那筆要跳過",
        ),
        (
            [[1, 2, 3], [1, 3, 5], [1, 4, 2]],
            4,
            1,
            5,
            "星狀圖:答案是最短距離的最大值,不是總和",
        ),
        ([[1, 2, 1], [2, 3, 1]], 4, 1, -1, "節點 4 完全孤立,沒有任何邊"),
        ([[1, 2, 1], [3, 2, 1]], 3, 1, -1, "節點 3 只有出邊,從 1 到不了"),
        ([[1, 2, 1], [2, 3, 1], [3, 1, 1]], 3, 1, 2, "圖中有環,不能無限繞圈"),
        ([[1, 2, 0], [2, 3, 0]], 3, 1, 0, "邊界:權重為 0,全部瞬間收到"),
        (
            [[3, 1, 5], [3, 2, 2], [2, 1, 2]],
            3,
            3,
            4,
            "起點不是 1:3->2->1 比 3->1 快",
        ),
        (
            [[1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100]],
            5,
            1,
            400,
            "邊界:權重上限的長鏈",
        ),
    ]

    for times, n, k, expected, note in test_set:
        result = c.networkDelayTime([edge[:] for edge in times], n, k)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       n={n} k={k} times={times}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
