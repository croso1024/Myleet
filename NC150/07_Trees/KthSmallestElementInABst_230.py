"""
    題意 :
    給定一棵二元搜尋樹的根節點 root,以及整數 k。
    回傳樹中第 k 小的節點值(k 從 1 開始算)。

    LeetCode 230 · Medium
    URL : https://leetcode.com/problems/kth-smallest-element-in-a-bst/

    Example :
    root = [3,1,4,null,2],         k = 1 -> 1
    root = [5,3,6,2,4,null,null,1], k = 3 -> 3

    Constraint :
    節點數量 n 的範圍為 1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    c = Solution()

    # (level-order list, k, 第 k 小的值)
    test_set = [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([1], 1, 1),                                     # 邊界:只有 root
        ([0], 1, 0),                                     # 邊界:節點值下限
        ([3, 1, 4, None, 2], 4, 4),                      # k = n,最大的那個
        ([5, 3, 6, 2, 4, None, None, 1], 1, 1),          # k = 1,最小的那個
        ([2, 1, 3], 2, 2),                               # 第 2 小落在 root
    ]

    for values, k, expected in test_set:
        root = build_tree(values)
        result = c.kthSmallest(root, k)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} k={k} | expected={expected} | got={result}")
