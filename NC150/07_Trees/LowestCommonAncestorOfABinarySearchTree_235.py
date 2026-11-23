"""
    題意 :
    給定一棵二元搜尋樹(BST)的根節點 root,以及樹中兩個不同的節點 p、q。
    回傳 p 與 q 的最低共同祖先(LCA)。

    LCA 是同時把 p、q 當成後代的最低節點。節點可以是自己的後代,
    所以若 p 是 q 的祖先,答案就是 p。節點值全部唯一,p 與 q 一定都在樹上。

    LeetCode 235 · Medium
    URL : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    Example :
    root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 -> 6
    root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 -> 2
    root = [2,1],                         p = 2, q = 1 -> 2

    Constraint :
    節點數量範圍為 [2, 10^5]
    -10^9 <= Node.val <= 10^9
    所有 Node.val 都不相同
    p != q
    p 與 q 都存在於 BST 中

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

    # (BST 的 level-order, p 的值, q 的值, LCA 的值, 說明)
    # 節點值唯一,測資用值找回節點再比較答案的值
    bst = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    test_set = [
        (bst, 2, 8, 6, "官方範例:分屬 root 左右兩側"),
        (bst, 2, 4, 2, "官方範例:p 是 q 的祖先"),
        ([2, 1], 2, 1, 2, "官方範例:只有兩個節點"),
        (bst, 8, 2, 6, "p、q 順序對調(p > q)"),
        (bst, 5, 3, 4, "p > q,LCA 在較深處"),
        (bst, 3, 5, 4, "兩個葉節點,同一個父節點"),
        (bst, 0, 5, 2, "跨過左子樹中的 2"),
        (bst, 7, 9, 8, "右子樹中的兩個葉節點"),
        (bst, 0, 9, 6, "最左與最右的葉節點"),
        (bst, 3, 9, 6, "一側較深、一側較淺,跨過 root"),
        (bst, 6, 9, 6, "p 就是 root"),
        (bst, 4, 3, 4, "q 是 p 的子節點"),
        ([2, None, 3], 2, 3, 2, "右斜鏈,p 是 root"),
        ([5, 4, None, 3, None, 2], 2, 4, 4, "左斜鏈,LCA 在中間"),
        ([0, -(10**9), 10**9], -(10**9), 10**9, 0, "邊界:數值上下限"),
    ]

    for values, p_val, q_val, expected, note in test_set:
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result_node = c.lowestCommonAncestor(root, p, q)
        result = None if result_node is None else result_node.val
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       p={p_val} q={q_val} | expected={expected} | got={result}")
