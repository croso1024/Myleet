"""
    題意 :
    給定兩棵二元樹的根節點 root 與 subRoot。
    若 root 中存在某個節點,以它為根的整棵子樹(含它所有的後代)與 subRoot
    結構相同、節點值也相同,回傳 True,否則回傳 False。

    root 自己整棵樹也算是 root 的子樹。

    LeetCode 572 · Easy
    URL : https://leetcode.com/problems/subtree-of-another-tree/

    Example :
    root = [3,4,5,1,2],                       subRoot = [4,1,2] -> True
    root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] -> False

    Constraint :
    root 的節點數量範圍為 [1, 2000]
    subRoot 的節點數量範圍為 [1, 1000]
    -10^4 <= root.val, subRoot.val <= 10^4

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
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
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

    # (root 的 level-order, subRoot 的 level-order, 預期, 說明)
    test_set = [
        ([3, 4, 5, 1, 2], [4, 1, 2], True, "官方範例:左子樹完全吻合"),
        (
            [3, 4, 5, 1, 2, None, None, None, None, 0],
            [4, 1, 2],
            False,
            "官方範例:節點 4 底下多了一個 0,不算相同",
        ),
        ([1], [1], True, "邊界:兩棵都只有 root,值相同"),
        ([1], [2], False, "邊界:兩棵都只有 root,值不同"),
        ([1, 2, 3], [1, 2, 3], True, "subRoot 就是整棵 root"),
        ([1, 2, 3], [1, 2], False, "root 多了右子節點,subRoot 沒有"),
        ([1, 2, 3], [1, 2, 3, 4], False, "subRoot 比 root 還大"),
        ([2, 1, 3], [1], True, "subRoot 對上 root 的葉節點"),
        ([1, 1], [1], True, "root 本身不吻合,但它的葉節點吻合"),
        ([1, 2, 3, 4, 5], [2, 4, 6], False, "結構相同,只有一個葉節點的值不同"),
        ([1, 2, 3, 4, 5], [2, 4, 5], True, "吻合的子樹在 root 的左子節點(非 root 本身)"),
        ([1, None, 1, None, 1], [1, None, 1], True, "右斜鏈,同值節點很多,吻合的是最下面兩個"),
        ([1, None, 1, None, 1], [1, 1], False, "右斜鏈對上左斜鏈,方向不同"),
        ([1, 1, None, 1], [1, 1], True, "左斜鏈,吻合的是最下面兩個"),
        ([10000, -10000], [-10000], True, "邊界:數值上下限"),
    ]

    for root_values, sub_values, expected, note in test_set:
        root = build_tree(root_values)
        sub_root = build_tree(sub_values)
        result = c.isSubtree(root, sub_root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(
            f"       root={root_values} subRoot={sub_values} | expected={expected} | got={result}"
        )
