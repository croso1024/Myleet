"""
    題意 :
    給定單向鏈結串列的頭節點 head,將整個串列反轉,並回傳反轉後的頭節點。

    LeetCode 206 · Easy
    URL : https://leetcode.com/problems/reverse-linked-list/

    Example :
    head = [1,2,3,4,5] -> [5,4,3,2,1]
    head = [1,2]       -> [2,1]
    head = []          -> []

    Constraint :
    串列中節點數量範圍為 [0, 5000]
    -5000 <= Node.val <= 5000

    思路 :
    直覺想法上 , 有迴圈 , 或著遞回兩種方案. 
    迴圈方案比較不擔心Timeout或性能問題 , 但應該比較考驗控制細節 , 而遞迴方案比較優雅.
    這邊兩種都去寫. 

    基本上這個答案需要繪圖 , 繪製完成後思考步驟來解. 
    第一種迴圈法 , 我採用的是紀錄 prev / cur / next 的方案來走
    在每一回合 cur , 做紀錄 next , 回指 prev 的操作. 並在離開後收尾一行回指


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None 
        cur = head 
        
        while cur and cur.next : 
            
            next = cur.next 

            cur.next = prev 

            prev = cur 

            cur = next 
        
        if cur and prev : 
            cur.next = prev 
        
        return cur 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None 
        cur = head 
        
        while cur  : 
            
            next = cur.next 

            cur.next = prev 

            prev = cur 

            cur = next 
        
        return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hook = None 

        # 給一條 linked list , 回傳反轉後的尾巴
        def _reserve(node : Optional[ListNode]) : 
            nonlocal hook 
            if node is None : return None 
            elif node.next is None : 
                hook = node 
                return node 

            reserved_linked_list = _reserve(node.next) 
            reserved_linked_list.next = node 
            node.next = None 

            return node
        
        _reserve(head) 
        return hook 



def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    c = Solution()

    # (輸入 list, 預期輸出 list)
    test_set = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),                                # 邊界:空串列
        ([1], [1]),                              # 邊界:單一節點
        ([-5000, 0, 5000], [5000, 0, -5000]),    # 邊界:數值上下限
        ([7, 7, 7], [7, 7, 7]),                  # 全部節點值相同
        (list(range(1, 11)), list(range(10, 0, -1))),  # 較長串列
    ]

    for values, expected in test_set:
        head = build_linked_list(values)
        result_head = c.reverseList(head)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
