"""
    題意 :
    給定 n 個節點（編號 0 到 n - 1）以及無向邊列表 edges，
    其中 edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條無向邊。

    判斷這些邊所構成的圖是否為一棵「有效的樹 (valid tree)」。
    有效的樹必須同時滿足：
    1. 所有節點連通（只有 1 個連通分量）
    2. 圖中沒有環（acyclic）

    LeetCode 261 · Medium
    URL : https://leetcode.com/problems/graph-valid-tree/

    Example :
    n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]            -> True
    n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]      -> False

    Constraint :
    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    沒有重複的邊

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    c = Solution()

    # (n, edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True, "官方範例:連通且無環的樹"),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            False,
            "官方範例:有環 (1-2-3),不是樹",
        ),
        (1, [], True, "單一節點且無邊,本身就是一棵樹"),
        (2, [], False, "兩個節點但無邊,不連通"),
        (4, [[0, 1], [2, 3]], False, "邊數不足且分成兩個連通分量"),
        (
            4,
            [[0, 1], [1, 2], [0, 2]],
            False,
            "陷阱:邊數剛好 n-1,但 0-1-2 成環且節點 3 孤立",
        ),
        (5, [[0, 1], [0, 2], [0, 3], [0, 4]], True, "星狀圖,連通無環"),
        (4, [[0, 1], [1, 2], [2, 3]], True, "鏈狀圖,連通無環"),
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False, "四節點四條邊構成環"),
    ]

    for n, edges, expected, note in test_set:
        result = c.validTree(n, [edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
