"""
    題意 :
    設計一組演算法,把一棵二元樹序列化成字串,再從該字串還原成原本的樹。

    序列化格式沒有限制,只要 deserialize(serialize(root)) 得到的樹
    與原本的結構、節點值相同即可。空樹必須能還原成空樹。

    LeetCode 297 · Hard
    URL : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

    Example :
    root = [1,2,3,null,null,4,5] -> [1,2,3,null,null,4,5]
    root = []                    -> []

    Constraint :
    節點數量範圍為 [0, 10^4]
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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """把二元樹編成一個字串。"""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """把 serialize 產生的字串還原成二元樹。"""
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
    codec = Codec()

    # 本題驗的是 round-trip。序列化格式不限定,
    # 還原後的 level-order 必須與原樹相同。
    test_set = [
        [1, 2, 3, None, None, 4, 5],
        [],                                              # 邊界:空樹
        [1],                                             # 邊界:只有 root
        [1, 2],                                          # 只有左子
        [1, None, 2],                                    # 只有右子
        [1, 2, 3, 4, 5, 6, 7],                           # 滿二元樹
        [-1000, None, 1000],                             # 邊界:數值上下限
        [1, 2, None, 3, None, 4],                        # 左斜鏈,null 的位置容易錯
    ]

    for values in test_set:
        root = build_tree(values)
        expected = tree_to_list(root)
        encoded = codec.serialize(root)
        restored = codec.deserialize(encoded)
        result = tree_to_list(restored)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
