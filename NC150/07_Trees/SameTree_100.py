"""
    題意 :
    給定兩棵二元樹的根節點 p 與 q,判斷它們是否相同。
    結構一樣、且對應節點的值也一樣,才算相同。

    LeetCode 100 · Easy
    URL : https://leetcode.com/problems/same-tree/

    Example :
    p = [1,2,3], q = [1,2,3] -> True
    p = [1,2],   q = [1,null,2] -> False
    p = [1,2,1], q = [1,1,2] -> False

    Constraint :
    兩棵樹的節點數量範圍都是 [0, 100]
    -10^4 <= Node.val <= 10^4

    思路 :
    寫一個遞迴同時走兩顆Tree , 每一個遞迴在回答當前子樹是否相同. 
    對單一節點來說就是回答節點是否存在且值相同

    複雜度 :
    - 時間複雜度 ,每個節點一次 O(N) 
    - 空間複雜度等同深度 , Worse case O(N)

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 若兩節點都為空,則該子樹相同,若只有單一節點存在則不同
        if p is None and q is None : return True 
        elif p is None or q is None : return False 

        # 兩節點都在,則比較值以及左右子樹

        p_val = p.val 
        q_val = q.val 
        if p_val != q_val : return False 
        

        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right , q.right)) 



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

    # (p 的 level-order, q 的 level-order, 預期, 說明)
    test_set = [
        ([1, 2, 3], [1, 2, 3], True, "官方範例:兩棵樹完全相同"),
        ([1, 2], [1, None, 2], False, "官方範例:子節點分別在左、右"),
        ([1, 2, 1], [1, 1, 2], False, "官方範例:結構相同但值不同"),
        ([], [], True, "邊界:兩棵都是空樹"),
        ([1], [1], True, "邊界:都只有 root,值相同"),
        ([1], [], False, "一棵有節點,另一棵是空樹"),
        ([], [1], False, "空樹對上只有 root"),
        ([1, 2, 3], [1, 2, 4], False, "只有一個葉節點的值不同"),
        ([1, 2, 3], [1, 3, 2], False, "左右子樹對調"),
        (
            [1, 2, 3, 4],
            [1, 2, 3, None, 4],
            False,
            "4 分別掛在左子與右子",
        ),
        ([-10000], [-10000], True, "邊界:數值下限"),
        ([10000, -10000], [10000, -10000], True, "邊界:數值上下限"),
        ([1, 2, None, 3], [1, 2, None, 3], True, "左斜鏈,兩棵相同"),
    ]

    for p_values, q_values, expected, note in test_set:
        p = build_tree(p_values)
        q = build_tree(q_values)
        result = c.isSameTree(p, q)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       p={p_values} q={q_values} | expected={expected} | got={result}")
