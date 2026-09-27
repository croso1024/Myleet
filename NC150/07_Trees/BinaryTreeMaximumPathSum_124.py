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

    直觀覺得 Post-Order 去遞回,抓出每一個子樹當中 ,經過sub-root的最大路徑和.
    同時 keep 答案的變數持續更新
    全域最大路徑和 : 
    max(
        當前節點 + 左子樹最大路徑和,
        當前節點 + 右子樹最大路徑和,
        當前節點 + 右子樹最大路徑和 + 左子樹最大路徑和,
    )
    由於我們定義的最大路徑和是在問這顆子樹(包含自身)的最大路徑和 , 當前節點必須得參與. 
    如果真正的解不經過root , 那也應該在遞回過程中被更新為最大值.

    一個需要注意的是遞回過程中. 每一個節點的最大路徑應該定義成 : 
    max(
    當前節點,
    當前節點 + 左子樹最大路徑和,
    當前節點 + 右子樹最大路徑和,
    )
    而不包含 "當前節點 + 左子 + 右子" 這條,因為這條僅能在計算解答要求的路徑和時使用. ( 如果讓遞回傳遞了某個Subtree同時包含左右子樹的路徑和,
    就違反題目約束的Path定義 )

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maximum_sum = float("-inf")

        def _recursive_update_maximum(node:TreeNode): 
            nonlocal maximum_sum
            if node is None : return 0 
            maximum_of_left_subtree = _recursive_update_maximum(node.left)
            maximum_of_right_subtree = _recursive_update_maximum(node.right) 
            
            # 更新目前為止可以看到的路徑最大值. 
            maximum_sum = max(
                maximum_sum , 
                node.val , 
                node.val + maximum_of_left_subtree , 
                node.val + maximum_of_right_subtree , 
                node.val + maximum_of_left_subtree + maximum_of_right_subtree 
            )

            # 計算包含當前節點在內，這顆子樹從root出發的Path最大值 ( 不能左右都加 , 這違反我們定義的 "從該節點出發的最大Path" )
            maximum_sum_in_subtree = max(
                node.val , 
                node.val+maximum_of_left_subtree , 
                node.val+maximum_of_right_subtree
            )
            
            return maximum_sum_in_subtree
        
        _recursive_update_maximum(root)

        return maximum_sum
            




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
        ([5,4,8,11,None,13,4,7,2,None,None,None,1],48)
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.maxPathSum(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
