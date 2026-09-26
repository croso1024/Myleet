"""
    題意 :
    給定二元樹的根節點 root,判斷它是不是一棵合法的二元搜尋樹(BST)。

    合法 BST 的定義:
    - 左子樹的所有節點值都小於該節點
    - 右子樹的所有節點值都大於該節點
    - 左右子樹各自也必須是合法 BST
    相等的值不合法。比較時不能只看父節點,孫節點也必須落在祖先留下的範圍內。

    LeetCode 98 · Medium
    URL : https://leetcode.com/problems/validate-binary-search-tree/

    Example :
    root = [2,1,3]             -> True
    root = [5,1,4,null,null,3,6] -> False

    Constraint :
    節點數量範圍為 [1, 10^4]
    -2^31 <= Node.val <= 2^31 - 1

    思路 :
    走遞迴 , 但需要持續保持每一輪遞迴Sub-Tree的最大值/最小值 , 供Parent node做參考. 
    流程上走 Post-Order , 先確認左右子樹的最大/最小值範圍 , 再判斷與當前節點是否構成BST. 
    由於我們使用了一個區域變數來儲存結果，一旦遇到了不合理值的時候，我們就不再考慮後續的Traverse是否能返回正確的每個指數的最大值、最小值。



    複雜度 : 
    - 時間複雜度 :所有節點走一次 O(N) ,
    - 空間複雜度 : 每一個 Call 遞迴都要保持一組 min/max , 因此空間複雜度 O(h) , worse case下O(N)

    Trade-off :

"""

from collections import deque
from typing import List, Optional,Tuple 

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        is_invalid = False 

        def _isBST(node:TreeNode) -> Tuple[int,int] : 
            nonlocal is_invalid 

            if is_invalid : return (None,None) 
            if node is None : return (None , None) 

            left_min , left_max = _isBST(node.left) 
            right_min , right_max  = _isBST(node.right) 

            if left_max is not None and node.val <= left_max : 
                is_invalid = True 
            
            if right_min is not None and node.val >= right_min: 
                is_invalid = True 

            maximum_in_subtree = max(
                node.val,
                right_max if right_max is not None else float("-inf") 
            )

            minimum_in_subtree =  min(
                node.val,
                left_min if left_min is not None else float("inf")
            )
            
            # 回傳當前子樹最大/最小值
            return (minimum_in_subtree , maximum_in_subtree)
    
        _isBST(root) 

        return True if not is_invalid else False 


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

    # (level-order list, 是否為合法 BST)
    test_set = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),                                     # 邊界:只有 root
        ([5, 4, 6, None, None, 3, 7], False),            # 3 小於祖先 5,但大於父節點 6 的左側
        ([2, 2, 2], False),                              # 相等值不合法
        ([0, None, -1], False),                          # 右子比 root 小
        ([2147483647], True),                            # 邊界:INT_MAX
        ([-2147483648, None, 2147483647], True),         # 邊界:整數上下限,且仍是合法 BST
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.isValidBST(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
