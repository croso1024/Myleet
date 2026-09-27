"""
    題意 :
    給定二元樹的根節點 root,判斷它是不是一棵高度平衡的二元樹。

    高度平衡的定義:每一個節點的左右子樹高度差都不超過 1,
    而且左右子樹各自也必須平衡。空樹視為平衡。

    LeetCode 110 · Easy
    URL : https://leetcode.com/problems/balanced-binary-tree/

    Example :
    root = [3,9,20,null,null,15,7]       -> True
    root = [1,2,2,3,3,null,null,4,4]     -> False
    root = []                            -> True

    Constraint :
    節點數量範圍為 [0, 5000]
    -10^4 <= Node.val <= 10^4

    思路 :
    Post-order 去檢查左右子樹的深度,
    得到左右子樹的深度後 , 就可在當前節點評斷是否 height-balanced , 
    完成後回傳當前子樹的深度

    複雜度 : Time O(N) / Space O(H)

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        is_balanced = True 

        def _recursive_traverse_for_balanced_judge(node:TreeNode): 
            nonlocal is_balanced
            # 空節點視為沒有高度
            if node is None : return 0 
            
            # early stop 
            if not is_balanced : return 0 

            depth_of_left_subtree = _recursive_traverse_for_balanced_judge(node.left)
            depth_of_right_subtree = _recursive_traverse_for_balanced_judge(node.right ) 

            # 當左右子樹的高度差 > 1 
            if abs(depth_of_left_subtree - depth_of_right_subtree) > 1 : 
                is_balanced = False 
            
            # 回傳當前樹的深度 : 
            return 1 + max(depth_of_left_subtree , depth_of_right_subtree) 
        
        _recursive_traverse_for_balanced_judge(root)

        return is_balanced


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

    # (level-order list, 是否高度平衡)
    # [1,2,2,3,None,None,3,4,None,None,4] 的 root 兩側等高,不平衡發生在較深的節點
    test_set = [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),                                      # 邊界:空樹
        ([1], True),                                     # 邊界:只有 root
        ([1, 2, 2, 3, None, None, 3], True),             # 高度差剛好為 1
        ([1, 2, None, 3], False),                        # root 的高度差為 2
        ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),  # root 平衡,子樹不平衡
        ([-10000, 10000], True),                         # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.isBalanced(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
