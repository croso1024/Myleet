"""
    題意 :
    給定二元樹的根節點 root,回傳這棵樹的直徑(diameter)。

    直徑是任意兩節點之間的最長路徑長度,以邊上的數量計算。
    這條路徑可以經過 root,也可以完全落在某一側子樹。

    LeetCode 543 · Easy
    URL : https://leetcode.com/problems/diameter-of-binary-tree/

    Example :
    root = [1,2,3,4,5] -> 3
    root = [1,2]       -> 1

    Constraint :
    節點數量範圍為 [1, 10^4]
    -100 <= Node.val <= 100

    思路 :
    在思考這題應該以遞回來做嗎!? , 遞回來做的話要怎樣做?
    讓每一個子樹回傳 ( 左右兩邊最深的子節點距離當前sub-root的距離!? , 並持續更新最佳解!? )
    
    要得到每一個Tree,左右兩端子樹最深的節點距離當前的位置,需要傳遞一個深度指標下去.
    走Post-Order , 得到左右兩子樹個別最深的距離->更新答案->選一個更長的向上回報

    複雜度 : 
    - 時間複雜度 : 每一個節點走過一次 O(N) 
    - 空間複雜度 : Stack Call O(H)
    
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum_distance = 0 
        # 回傳當前這顆樹到其最深節點的距離
        def _traverse_depthest_subtree(node:TreeNode) -> int : 
            nonlocal maximum_distance
            if node is None : return 0 
            # Post-Order : 
            left_subtree_depthest_distance = _traverse_depthest_subtree(node.left)
            right_subtree_depthest_distance = _traverse_depthest_subtree(node.right)

            # 嘗試更新一次最佳解 , 以目前的最佳解去比對 "目前這顆樹的左子最深 + 右子最深"
            # ( 題目要的是兩個節點之間最大的 edge 數 , 而不是節點數 , 因此不用包含當前自身節點 )
            maximum_distance = max(
                maximum_distance , 
                left_subtree_depthest_distance + right_subtree_depthest_distance
            )
            
            # 回傳目前為止,包含自身這顆樹的深度
            return 1 + max(left_subtree_depthest_distance , right_subtree_depthest_distance) 

        _traverse_depthest_subtree(root) 

        return maximum_distance
            


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

    # (level-order list, 直徑的邊數)
    # [1,2,None,3,4,5,None,None,6] 的最長路徑在節點 2,不經過 root
    test_set = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),                                        # 邊界:只有 root,沒有邊
        ([1, 2, 3], 2),                                  # 路徑經過 root
        ([1, 2, None, 3, None, 4], 3),                   # 左斜鏈,四個節點三條邊
        ([1, None, 2, None, 3], 2),                      # 右斜鏈
        ([1, 2, None, 3, 4, 5, None, None, 6], 4),       # 直徑不在 root
        ([1, 2, 3, 4, 5, 6, 7], 4),                      # 滿二元樹,葉到葉
        ([-100, 0, 100], 2),                             # 邊界:數值上下限,直徑與值無關
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.diameterOfBinaryTree(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
