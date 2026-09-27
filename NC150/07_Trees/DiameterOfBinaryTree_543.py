"""
    題意 :
    給定二元樹的根節點 root,回傳這棵樹的直徑(diameter)。

    直徑是任意兩節點之間的最長路徑長度,以邊上的數量計算。
    這條路徑可以經過 root,也可以完全落在某一側子樹。

    LeetCode 543 · Easy
    URL : https://leetcode.com/problems/diameter-of-binary-tree/

    Example :
    root = [1,2,3,4,5] -> 3
    root = [1,2]       -> 1

    Constraint :
    節點數量範圍為 [1, 10^4]
    -100 <= Node.val <= 100

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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

    # (level-order list, 直徑的邊數)
    # [1,2,None,3,4,5,None,None,6] 的最長路徑在節點 2,不經過 root
    test_set = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),                                        # 邊界:只有 root,沒有邊
        ([1, 2, 3], 2),                                  # 路徑經過 root
        ([1, 2, None, 3, None, 4], 3),                   # 左斜鏈,四個節點三條邊
        ([1, None, 2, None, 3], 2),                      # 右斜鏈
        ([1, 2, None, 3, 4, 5, None, None, 6], 4),       # 直徑不在 root
        ([1, 2, 3, 4, 5, 6, 7], 4),                      # 滿二元樹,葉到葉
        ([-100, 0, 100], 2),                             # 邊界:數值上下限,直徑與值無關
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.diameterOfBinaryTree(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
