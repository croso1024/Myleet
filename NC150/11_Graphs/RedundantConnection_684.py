"""
    題意 :
    一棵樹是連通、而且沒有環的無向圖。
    這張圖一開始是 n 個節點(編號 1 到 n)的樹,之後多加了一條原本不存在的邊。
    edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條邊。edges 的長度就是 n。

    回傳一條可以刪掉的邊,刪掉之後剩下的圖仍是一棵 n 個節點的樹。
    若有多條邊都可以刪,回傳在 edges 裡出現得最晚的那一條。

    LeetCode 684 · Medium
    URL : https://leetcode.com/problems/redundant-connection/

    Example :
    edges = [[1,2],[1,3],[2,3]]                 -> [2,3]
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]     -> [1,4]

    Constraint :
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= n
    沒有重複的邊
    給定的圖是連通的

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    c = Solution()

    # (edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3], "官方範例:三角形,最後一條邊成環"),
        (
            [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
            [1, 4],
            "官方範例:環在前四條,5 是掛在外面的葉子",
        ),
        ([[1, 2], [2, 3], [1, 3]], [1, 3], "三個節點,多餘的邊剛好是最後一條"),
        (
            [[1, 2], [2, 3], [1, 3], [3, 4]],
            [1, 3],
            "多餘的邊不是陣列最後一條,後面還有一條必須留的樹邊",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
            [4, 1],
            "四節點的環,答案是環上最晚出現的邊,不是整份輸入的最後一條",
        ),
        (
            [[1, 2], [1, 3], [1, 4], [2, 3]],
            [2, 3],
            "1 分岔到 2、3、4,只有 2 和 3 之間多了一條邊",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [2, 4], [4, 5]],
            [2, 4],
            "環在中段,左右各有一條必須留的邊",
        ),
        (
            [[2, 3], [1, 2], [1, 3], [1, 4], [4, 5]],
            [1, 3],
            "環上的三條邊不是依編號排,要回傳輸入裡最晚的那條",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [1, 4]],
            [1, 4],
            "四個節點剛好四條邊,整圈都在環上,答案是最後一條",
        ),
    ]

    for edges, expected, note in test_set:
        result = c.findRedundantConnection([edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
