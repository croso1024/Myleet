"""
    題意 :
    給定二元樹的根節點 root。
    若從 root 走到節點 X 的路徑上,沒有任何節點值大於 X,則 X 是 good node。
    回傳 good node 的數量。root 本身一定是 good node。

    LeetCode 1448 · Medium
    URL : https://leetcode.com/problems/count-good-nodes-in-binary-tree/

    Example :
    root = [3,1,4,3,null,1,5] -> 4
    root = [3,3,null,4,2]     -> 3
    root = [1]                -> 1

    Constraint :
    節點數量範圍為 [1, 10^5]
    -10^4 <= Node.val <= 10^4

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
    def goodNodes(self, root: Optional[TreeNode]) -> int:
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

    # (level-order list, good node 數量)
    test_set = [
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
        ([1], 1),                                        # 邊界:只有 root
        ([1, 2, 3], 3),                                  # 子節點都比 root 大,全部算
        ([-1, -2, -3], 1),                               # 子節點都更小,只剩 root
        ([3, 3], 2),                                     # 與 root 相等也算
        ([5, 4, 6, None, None, 3, 7], 3),                # 路徑上的最大值卡住較深節點
        ([-10000, 10000], 2),                            # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.goodNodes(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
