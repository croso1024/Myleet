"""
    題意 :
    給定二元樹的根節點 root,將這棵樹左右翻轉(每個節點的左右子樹對調),
    並回傳翻轉後的根節點。

    LeetCode 226 · Easy
    URL : https://leetcode.com/problems/invert-binary-tree/

    Example :
    root = [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root = [2,1,3]         -> [2,3,1]
    root = []              -> []

    Constraint :
    節點數量範圍為 [0, 100]
    -100 <= Node.val <= 100

    思路 :
    這題很 Naive , 走PostOrder 去遞回反轉子樹即可.

    複雜度 : 
    - 每一個節點走過一次 , Time O(N)
    - 僅需常數儲存空間 Space O(C) 

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def _invert_tree(node : TreeNode) : 
            if node is None : return None 

            # Post-Order Trverse 

            inverted_left_sub_tree = _invert_tree(node.left) 
            inverted_right_sub_tree = _invert_tree(node.right)  

            node.left = inverted_right_sub_tree
            node.right = inverted_left_sub_tree

            return node 

        return _invert_tree(root) 
            


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

    # (level-order list, 翻轉後的 level-order list)
    test_set = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),                                        # 邊界:空樹
        ([1], [1]),                                      # 邊界:只有 root
        ([1, 2], [1, None, 2]),                          # 只有左子,翻成只有右子
        ([1, None, 2], [1, 2]),                          # 只有右子,翻成只有左子
        ([-100, 0, 100], [-100, 100, 0]),                # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result_root = c.invertTree(root)
        result = tree_to_list(result_root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
