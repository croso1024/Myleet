"""
    題意 :
    給定二元樹的根節點 root,回傳層序遍歷(level order)的結果。
    同一層由左到右,每一層各自成為一個 list。

    LeetCode 102 · Medium
    URL : https://leetcode.com/problems/binary-tree-level-order-traversal/

    Example :
    root = [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    root = [1]                     -> [[1]]
    root = []                      -> []

    Constraint :
    節點數量範圍為 [0, 2000]
    -1000 <= Node.val <= 1000

    思路 :
    標準 BFS 搜索,這題我就不走 Recursive , 改用 While Loop 的BFS模式. 
    一樣是每一個節點只需要走訪一次, 時間O(N) , 空間上因為要存走訪中同一層以及下一層節點,抓O(N)

    複雜度 : Time O(N) / Space O(N)

    Trade-off :

"""

from collections import deque
from math import nextafter
from typing import Deque, List, Optional


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


from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        answer = [] 

        bfs_queue : Deque[TreeNode] = deque() 
        if root : bfs_queue.append(root) 
        else : return [] 

        # BFS 的邏輯 , 以一個 Queue 維護待 Traverse 的清單. 
        # 每一輪開始 traverse 的當下就是答案要的快照 

        # 此處的 while 判斷就作為還有沒有要開下一輪 Traverse 的判決
        while bfs_queue : 
            size = len(bfs_queue)
            answer.append( [node.val for node in bfs_queue])
            # 只走訪這一輪(同一階層)的節點 
            for i in range(size) : 
                next_visited = bfs_queue.popleft() 
                if next_visited.left : bfs_queue.append(next_visited.left)
                if next_visited.right : bfs_queue.append(next_visited.right) 
            
        return answer





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

    # (level-order list, 預期分層結果)
    test_set = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),                                    # 邊界:空樹
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, None, 2, None, 3], [[1], [2], [3]]),    # 一路往右歪
        ([1, 2, None, 3], [[1], [2], [3]]),          # 一路往左歪
        ([-1000, 0, 1000], [[-1000], [0, 1000]]),    # 邊界:數值上下限
    ]

    for values, expected in test_set:
        root = build_tree(values)
        result = c.levelOrder(root)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
