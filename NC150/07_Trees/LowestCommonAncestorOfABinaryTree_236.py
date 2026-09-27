"""
    題意 :
    給定一棵一般二元樹的根節點 root,以及樹中兩個不同的節點 p、q。
    回傳 p 與 q 的最低共同祖先(LCA)。

    LCA 是同時把 p、q 當成後代的最低節點。節點可以是自己的後代,
    所以若 p 是 q 的祖先,答案就是 p。節點值全部唯一,p 與 q 一定都在樹上。

    這題是 CORE_LIST 的外掛 P0,不在 NeetCode 150 的 15 題 Trees 裡。
    NC150 收的是 BST 版 235;236 才是面試常考的一般二元樹版本,而且是 235 的超集。

    LeetCode 236 · Medium
    URL : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

    Example :
    root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 -> 3
    root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 -> 5
    root = [1,2],                         p = 1, q = 2 -> 1

    Constraint :
    節點數量範圍為 [2, 10^5]
    -10^9 <= Node.val <= 10^9
    所有 Node.val 都不相同
    p != q
    p 與 q 都存在於樹中

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
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    c = Solution()

    # (level-order list, p 的值, q 的值, LCA 的值)
    # 節點值唯一,測資用值找回節點再比較答案的值
    tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    test_set = [
        (tree, 5, 1, 3),                                 # 分屬左右子樹
        (tree, 5, 4, 5),                                 # p 是 q 的祖先
        ([1, 2], 1, 2, 1),                               # LCA 是 root
        (tree, 7, 4, 2),                                 # 兩葉節點,LCA 在較深處
        (tree, 6, 4, 5),                                 # 一側較深、一側較淺
        (tree, 0, 8, 1),                                 # 兄弟節點
        (tree, 7, 8, 3),                                 # 跨過 root
        ([0, -(10**9), 10**9], -(10**9), 10**9, 0),      # 邊界:數值上下限
    ]

    for values, p_val, q_val, expected in test_set:
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result_node = c.lowestCommonAncestor(root, p, q)
        result = None if result_node is None else result_node.val
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(
            f"{status} | p={p_val} q={q_val} | expected={expected} | got={result}"
        )
