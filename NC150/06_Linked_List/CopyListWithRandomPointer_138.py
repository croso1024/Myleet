"""
    題意 :
    給定一條長度為 n 的單向鏈結串列,每個節點除了 next,還有一個 random 指標,
    可以指向串列中的任意節點,或是 null。

    請做這條串列的 deep copy:
    複製出恰好 n 個全新節點,val / next / random 都要對應到「複製後」的節點,
    複製串列裡的任何指標都不得指回原串列的節點。
    回傳複製後的頭節點。

    輸入 / 輸出以 n 個節點的 list 表示。每個節點是 [val, random_index]:
      - val           節點的值
      - random_index  random 指向的節點 index(0-based);null 表示沒有指向

    LeetCode 138 · Medium
    URL : https://leetcode.com/problems/copy-list-with-random-pointer/

    Example :
    head = [[7,null],[13,0],[11,4],[10,2],[1,0]] -> [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head = [[1,1],[2,1]]                         -> [[1,1],[2,1]]
    head = [[3,null],[3,0],[3,null]]             -> [[3,null],[3,0],[3,null]]

    Constraint :
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random 為 null,或指向串列中的某個節點

    思路 :
    這一題的想法是，我們使用一個 HashMap 先儲存曾經看過的節點與複製品的對照. 
    如果某個節點已經有了複製品. 那就直接使用,沒有就建立再用. 
    這樣確保我們依據 next 節點走一輪後, 所有節點都建立過. 
    這個方案需要 O(N)時間複雜度 , O(N) 空間間複雜度

    複雜度 : Time O(N) , 即走訪一次整條List , Space : O(N) 每一個節點都要儲存一份複製品,但這也是產結果本來就要的. 

    Trade-off :

"""

from random import random
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        next: "Optional[Node]" = None,
        random: "Optional[Node]" = None,
    ):
        self.val = val
        self.next = next
        self.random = random


from typing import List , Dict 
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        
        if head is None : return None 
        
        # Store the hash or origin node , value is the replica
        self.copy_map : Dict[int ,  Node] = {} 
        self.copy_map[ id(head ) ] = Node(head.val) 

        # copy node 
        cur = head 

        while cur : 

            next_node = cur.next 
            random_node = cur.random 

            if next_node : 

                if id(next_node) not in self.copy_map : 
                    self.copy_map[id(next_node)] = Node(next_node.val ) 
                
                self.copy_map[id(cur)].next = self.copy_map[id(next_node)] 
            
            if random_node : 

                if id(random_node) not in self.copy_map : 
                    self.copy_map[id(random_node)] = Node(random_node.val) 
                
                self.copy_map[id(cur)].random = self.copy_map[id(random_node)] 
            
            cur = next_node 
        
        return self.copy_map[id(head)]


def build_random_list(pairs: List[List[Optional[int]]]) -> Optional[Node]:
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rand) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand is not None:
            nodes[i].random = nodes[rand]
    return nodes[0]


def random_list_to_list(head: Optional[Node]) -> List[List[Optional[int]]]:
    nodes: List[Node] = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    index = {node: i for i, node in enumerate(nodes)}
    return [
        [node.val, None if node.random is None else index[node.random]]
        for node in nodes
    ]


def shares_node_with(original: Optional[Node], copied: Optional[Node]) -> bool:
    seen = set()
    curr = original
    while curr:
        seen.add(id(curr))
        curr = curr.next
    curr = copied
    while curr:
        if id(curr) in seen:
            return True
        curr = curr.next
    return False


if __name__ == "__main__":
    c = Solution()

    # (pairs, 預期輸出) —— random_index 用 None 表示 null
    # 另檢查複製後的節點沒有與原串列共用
    test_set = [
        ([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]], [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
        ([[1, 1], [2, 1]], [[1, 1], [2, 1]]),
        ([[3, None], [3, 0], [3, None]], [[3, None], [3, 0], [3, None]]),
        ([], []),                                              # 邊界:空串列
        ([[1, None]], [[1, None]]),                            # 單節點,random 為 null
        ([[1, 0]], [[1, 0]]),                                  # 單節點指向自己
        ([[1, None], [2, None], [3, None]], [[1, None], [2, None], [3, None]]),
        ([[1, 2], [2, 0], [3, 1]], [[1, 2], [2, 0], [3, 1]]),  # random 交錯指向
    ]

    for pairs, expected in test_set:
        head = build_random_list(pairs)
        copied = c.copyRandomList(head)
        result = random_list_to_list(copied)
        shared = shares_node_with(head, copied)
        passed = result == expected and not shared
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={pairs} | expected={expected} | got={result} | shared={shared}")
