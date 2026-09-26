"""
    題意 :
    給定二元樹的根節點 root,判斷它是不是一棵合法的二元搜尋樹(BST)。

    合法 BST 的定義:
    - 左子樹的所有節點值都小於該節點
    - 右子樹的所有節點值都大於該節點
    - 左右子樹各自也必須是合法 BST
    相等的值不合法。比較時不能只看父節點,孫節點也必須落在祖先留下的範圍內。

    LeetCode 98 · Medium
    URL : https://leetcode.com/problems/validate-binary-search-tree/

    Example :
    root = [2,1,3]             -> True
    root = [5,1,4,null,null,3,6] -> False

    Constraint :
    節點數量範圍為 [1, 10^4]
    -2^31 <= Node.val <= 2^31 - 1

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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

    # (level-order list, 是否為合法 BST)
    test_set = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),                                     # 邊界:只有 root
        ([5, 4, 6, None, None, 3, 7], False),            # 3 小於祖先 5,但大於父節點 6 的左側
        ([2, 2, 2], False),                              # 相等值不合法
        ([0, None, -1], False),                          # 右子比 root 小
        ([2147483647], True),                            # 邊界:INT_MAX
        ([-2147483648, None, 2147483647], True),         # 邊界:整數上下限,且仍是合法 BST
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.isValidBST(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
