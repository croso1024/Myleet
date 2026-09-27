"""
    題意 :
    給定二元樹的根節點 root,回傳任意非空路徑的最大路徑和。

    路徑是一串相鄰節點,每個節點最多出現一次,不必經過 root。
    路徑和是路徑上所有節點值的總和。節點值可以是負的,
    所以最優路徑有時只包含單一節點。

    LeetCode 124 · Hard
    URL : https://leetcode.com/problems/binary-tree-maximum-path-sum/

    Example :
    root = [1,2,3]                    -> 6
    root = [-10,9,20,null,null,15,7]  -> 42

    Constraint :
    節點數量範圍為 [1, 3 * 10^4]
    -1000 <= Node.val <= 1000

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
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

    # (level-order list, 最大路徑和)
    test_set = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),                                      # 邊界:只有一個負數節點
        ([0], 0),                                        # 單一節點為 0
        ([2, -1], 2),                                    # 負子節點不該被接上
        ([1, -2, 3], 4),                                 # 走 1 -> 3,丟掉 -2
        ([-2, -1], -1),                                  # 全負數,取較大的單一節點
        ([-1, None, 10], 10),                            # 單邊延伸後總和更小
        ([5, 4, 8], 17),                                 # 路徑經過 root
        ([1000, -1000, 1000], 2000),                     # 邊界:數值上下限
        ([-1000], -1000),                                # 邊界:最小節點值
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.maxPathSum(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
