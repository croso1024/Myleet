"""
    題意 :
    給定一個包含 n 個節點的無向圖（節點編號 0 到 n - 1），以及邊列表 edges，
    其中 edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條無向邊。

    回傳這張圖中連通分量（connected components）的總數。

    LeetCode 323 · Medium
    URL : https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

    Example :
    n = 5, edges = [[0,1],[1,2],[3,4]]          -> 2
    n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]    -> 1

    Constraint :
    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    沒有重複的邊

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    c = Solution()

    # (n, edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        (5, [[0, 1], [1, 2], [3, 4]], 2, "官方範例:{0,1,2} 與 {3,4} 共 2 個分量"),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1, "官方範例:全部串成 1 個分量"),
        (1, [], 1, "單一節點無邊,共 1 個分量"),
        (4, [], 4, "完全無邊,每個節點各自為獨立分量"),
        (
            6,
            [[0, 1], [1, 2], [3, 4]],
            3,
            "包含孤立節點 5,共有 {0,1,2}, {3,4}, {5}",
        ),
        (
            4,
            [[0, 1], [1, 2], [2, 0]],
            2,
            "分量內有環:多餘的邊不應重複減少分量數,答案應為 {0,1,2} 與 {3}",
        ),
        (
            4,
            [[0, 1], [2, 3], [1, 2]],
            1,
            "先各自連通後再由橋邊 [1,2] 合併為單一分量",
        ),
        (5, [[0, 4]], 4, "只有一條邊連接頭尾,其餘 3 點各自獨立"),
    ]

    for n, edges, expected, note in test_set:
        result = c.countComponents(n, [edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
