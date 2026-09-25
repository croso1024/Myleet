"""
    題意 :
    給定二元樹的根節點 root。
    想像自己站在樹的右側往左看,回傳從上到下看得到的節點值。
    每一層只看得到該層最右邊的節點。

    LeetCode 199 · Medium
    URL : https://leetcode.com/problems/binary-tree-right-side-view/

    Example :
    root = [1,2,3,null,5,null,4] -> [1,3,4]
    root = [1,null,3]            -> [1,3]
    root = []                    -> []

    Constraint :
    節點數量範圍為 [0, 100]
    -100 <= Node.val <= 100

    思路 :

    這一題實際上要的就是每一個層級的最右邊一個節點. 
    可以走遞回 , 並用一個 Hashmap 持續追蹤每一個深度最後一個看到的節點數值.
    也可以走 BFS , 去抓每一個深度最後一個節點.

    這邊選擇走遞回

    複雜度 : 
    - Time O(N) , 每個節點都走過一次
    - Space O(h) , 需要有一個陣列儲存答案,大小等於Tree高度

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

from typing import Dict 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_side_view_map : Dict[int , int] = {}

        def _recursive( node : TreeNode , depth : int ,view_map : Dict[int,int] ) : 
            if node is None : return 
            

            # 這裡走 preorder , 先執行操作,才往左右挖
            # 根據自己所在的深度 , 更新該深度最後一次看到的節點.
            view_map[depth]  = node.val 
            if node.left : 
                _recursive(node.left , depth+1 , view_map ) 
            if node.right : 
                _recursive(node.right, depth+1 , view_map ) 
            
            return None


        _recursive(root , depth = 0 , view_map = right_side_view_map ) 

        # 這裡答案仰賴 dict.values() 根據建立Key的順序回傳 ,
        # 若建立Key的順序不一定 , 可能要寫成   [ right_side_view_map[depth] for depth in sorted(right_side_view_map.keys()) ]
        return list(right_side_view_map.values())
        




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

    # (level-order list, 右側視圖)
    test_set = [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),                                        # 邊界:空樹
        ([1], [1]),                                      # 邊界:只有 root
        ([1, 2], [1, 2]),                                # 沒有右子,左子仍看得到
        ([1, 2, 3, 4], [1, 3, 4]),                       # 更深層只有左側節點
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),  # 左鏈延伸,每層最右仍是左鏈
        ([-100, 0, 100], [-100, 100]),                   # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.rightSideView(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
