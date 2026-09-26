"""
    題意 :
    給定一棵二元樹的前序走訪 preorder 與中序走訪 inorder。
    兩個陣列裡的值都不重複。依這兩份走訪結果重建這棵樹,並回傳根節點。

    LeetCode 105 · Medium
    URL : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

    Example :
    preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] -> [3,9,20,null,null,15,7]
    preorder = [-1],           inorder = [-1]         -> [-1]

    Constraint :
    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder 與 inorder 內的值皆唯一,且彼此對應同一棵樹

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    result: List[Optional[int]] = []
    queue: deque = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    c = Solution()

    # (preorder, inorder, 重建後的 level-order list)
    test_set = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),                              # 邊界:只有 root
        ([1, 2, 3], [3, 2, 1], [1, 2, None, 3]),         # 一路往左歪
        ([1, 2, 3], [1, 2, 3], [1, None, 2, None, 3]),   # 一路往右歪
        ([1, 2, 3], [2, 1, 3], [1, 2, 3]),               # 左右子都在
        ([-3000, 3000], [3000, -3000], [-3000, 3000]),   # 邊界:數值上下限
    ]

    for preorder, inorder, expected in test_set:
        result_root = c.buildTree(preorder, inorder)
        result = tree_to_list(result_root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(
            f"{status} | preorder={preorder} inorder={inorder} | "
            f"expected={expected} | got={result}"
        )
