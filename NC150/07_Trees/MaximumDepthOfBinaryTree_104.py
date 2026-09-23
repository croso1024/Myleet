"""
    題意 :
    給定二元樹的根節點 root,回傳這棵樹的最大深度。
    最大深度定義為:從 root 走到最遠葉節點,沿路上的節點總數。

    LeetCode 104 · Easy
    URL : https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Example :
    root = [3,9,20,null,null,15,7] -> 3
    root = [1,null,2]              -> 2

    Constraint :
    節點數量範圍為 [0, 10^4]
    -100 <= Node.val <= 100

    思路 :
    Naive 的練手題 , 往下遞迴去挖. 然後一個指標去評估即可.
    時間複雜度 O(N) , 每個節點評估一次. 
    空間複雜度 O(1)

    可以用 DFS/BFS , 也能走 Tree recursive 


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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_depth : int = 0 
        # DFS 遞回
        def _recursive( node : TreeNode , cur_depth: int):
            nonlocal max_depth
            if node is None : return None
            max_depth = max(max_depth , cur_depth)
            if node.left : 
                _recursive(node=node.left , cur_depth=cur_depth+1)
            if node.right :
                _recursive(node=node.right , cur_depth=cur_depth+1)

        _recursive(root , 1)

        return max_depth


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

    # (level-order list, 預期深度)
    test_set = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),                                     # 邊界:空樹
        ([1], 1),                                    # 邊界:只有 root
        ([1, 2, None, 3, None, 4], 4),               # 一路往左歪
        ([1, None, 2, None, 3], 3),                  # 一路往右歪
        ([-100, 0, 100], 2),                         # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.maxDepth(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
