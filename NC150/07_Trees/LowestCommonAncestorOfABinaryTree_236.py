"""
    題意 :
    給定一棵一般二元樹的根節點 root,以及樹中兩個不同的節點 p、q。
    回傳 p 與 q 的最低共同祖先(LCA)。

    LCA 是同時把 p、q 當成後代的最低節點。節點可以是自己的後代,
    所以若 p 是 q 的祖先,答案就是 p。節點值全部唯一,p 與 q 一定都在樹上。

    這題是 CORE_LIST 的外掛 P0,不在 NeetCode 150 的 15 題 Trees 裡。
    NC150 收的是 BST 版 235;236 才是面試常考的一般二元樹版本,而且是 235 的超集。

    LeetCode 236 · Medium
    URL : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

    Example :
    root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 -> 3
    root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 -> 5
    root = [1,2],                         p = 1, q = 2 -> 1

    Constraint :
    節點數量範圍為 [2, 10^5]
    -10^9 <= Node.val <= 10^9
    所有 Node.val 都不相同
    p != q
    p 與 q 都存在於樹中

    思路 :
    已知所有節點的數值都不同, p != q 且 p , q 都必定在tree當中. 
    一種解法，是去紀錄每一個遍歷到當前節點時，已經經過的Path. 
    直到找到 p 和 q. 
    如果此時我們紀錄了走訪到 p & q 的軌跡. 我們就能在O(N)內找到他們的共同祖先.
    (從root出發 , 一直配對到第一個不等同的節點,則前一個就是LCA)
    此算法時間複雜度 O(N) , 空間 O(H) , 但我想未必是最漂亮的. 

    第二條解 , 修改遞回的定義. 
    去找到當前節點下方是否存在p or q !? 
    每一個節點去做 : 
    - 檢查左子樹是否包含 p / q / p and q / None 
    - 檢查右子樹是否包含 p / q / p and q / None 
    - 基於上述兩個結果 , 判斷自己是不是LCA , 或著需要繼續待著"底下有誰的資訊上去" 

    時間複雜度 O(N) , Space O(H)

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

from typing import Dict , List 

class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        
        # Only record the path to p/q 
        path_hook : Dict[int , List[int]] = {
            p.val : None , 
            q.val : None , 
        }
        node_ref : Dict[int,TreeNode] = {} 

        # pre-order traverse
        def _traverse_and_record_path(node:TreeNode , current_path : List[int]):  
            if node is None : return 
            node_ref[node.val] = node
            current_path.append(node.val)
            # Copy a path from root to p/q
            if node.val in path_hook: path_hook[node.val] = current_path[:]
            _traverse_and_record_path(node.left , current_path=current_path)
            _traverse_and_record_path(node.right , current_path=current_path) 
            current_path.pop()

            return 
        
        _traverse_and_record_path(node=root , current_path=[])
        
        # After traverse , we already have the path from root->p / root->q 
        # Use O(N) compare and find the answer 
        path_to_p = path_hook[p.val]
        path_to_q = path_hook[q.val]

        # 拿掉兩條軌跡 , 每一條軌跡從 root 出發 , 止於 p/q , 共通部分抽出即可. 
        # 至少 root 會完全一樣 , 因此 path_to_p[0] == path_to_q[0]
        for i in range( max(len(path_to_p) , len(path_to_q))) : 

            if i < len(path_to_p) and i < len(path_to_q) : 

                if path_to_p[i] != path_to_q[i] : return node_ref[path_to_p[i-1]]
            
            # 其中一條已經空了 , 直接回任意條前一格
            else : 
                return node_ref[path_to_p[i-1]]

        return None

from typing import Tuple
class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        answer = None 

        # 回傳 : 該子樹底下有 p / q 兩個 boolean
        def _recursive(node:TreeNode)-> Tuple[bool]:
            nonlocal   answer
            if node is None : return [None,None]

            # post order , 先追左/右有沒有包含 p or q 
            left_include_p , left_include_q = _recursive(node.left) 
            right_include_p , right_include_q = _recursive(node.right) 

            # 更新自己有沒有p/q 
            if node.val == p.val or left_include_p or right_include_p : 
                have_p = True 
            else : 
                have_p = False 

            if node.val == q.val or left_include_q or right_include_q : 
                have_q = True 
            else : 
                have_q = False 

            if have_p and have_q and answer is None: 
                answer = node 

            # 回傳自己和底下子樹是否包含 p / q 
            return  ( have_p , have_q )

        _recursive(root) 
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    c = Solution()

    # (level-order list, p 的值, q 的值, LCA 的值)
    # 節點值唯一,測資用值找回節點再比較答案的值
    tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    test_set = [
        (tree, 5, 1, 3),                                 # 分屬左右子樹
        (tree, 5, 4, 5),                                 # p 是 q 的祖先
        ([1, 2], 1, 2, 1),                               # LCA 是 root
        (tree, 7, 4, 2),                                 # 兩葉節點,LCA 在較深處
        (tree, 6, 4, 5),                                 # 一側較深、一側較淺
        (tree, 0, 8, 1),                                 # 兄弟節點
        (tree, 7, 8, 3),                                 # 跨過 root
        ([0, -(10**9), 10**9], -(10**9), 10**9, 0),      # 邊界:數值上下限
    ]

    for values, p_val, q_val, expected in test_set:
        root = build_tree(values)
        p = find_node(root, p_val)
        q = find_node(root, q_val)
        result_node = c.lowestCommonAncestor(root, p, q)
        result = None if result_node is None else result_node.val
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(
            f"{status} | p={p_val} q={q_val} | expected={expected} | got={result}"
        )
