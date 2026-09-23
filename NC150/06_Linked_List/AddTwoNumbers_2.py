"""
    題意 :
    給定兩個「非負整數」的單向鏈結串列 l1、l2,數字以「反向」存放
    (個位在頭、高位在尾)。將兩數相加,回傳同樣以反向鏈結串列表示的和。

    LeetCode 2 · Medium
    URL : https://leetcode.com/problems/add-two-numbers/

    Example :
    l1 = [2,4,3], l2 = [5,6,4]                 -> [7,0,8]
    l1 = [0],     l2 = [0]                     -> [0]
    l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]       -> [8,9,9,9,0,0,0]

    Constraint :
    每個串列的節點數量範圍為 [1, 100]
    0 <= Node.val <= 9
    除了數字 0 本身,串列不包含 leading zero

    思路 :

    這題要回傳的Sum , 一樣採用頭為低位,尾為高位的原則. 
    主要是 l1 , l2 的長度不一致. 一開始也無法得知誰長. 
    也沒有說明要回傳全新 Linked List 還是 in-place 修改某一條. 

    這邊先以全新 Linked List 來解, 程式碼邏輯會比較清晰. 

    複雜度 : Time O(N) , Space O(N) (開全新Linked List , O(1) in-place操作 ) 

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy 
        carry = 0 
        while l1 or l2 : 

            val_1 = l1.val if l1 else 0 
            val_2 = l2.val if l2 else 0 

            if (val_1 + val_2 + carry ) >= 10 :  
                node = ListNode( val = val_1 + val_2 + carry - 10 ) 
                carry = 1 
            else : 
                node = ListNode( val = val_1 + val_2 + carry ) 
                carry = 0 
            
            if l1 : l1 = l1.next 
            if l2 : l2 = l2.next 

            head.next = node 
            head = node 
        
        if carry : 
            node = ListNode(val=1) 
            head.next = node 
        
        return dummy.next 


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

    # (l1, l2, 預期輸出 list)
    test_set = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9], [0, 0, 1]),                    # 長度不同,且需要進位長出新節點
        ([5], [5], [0, 1]),                          # 個位相加剛好進位
        ([9, 9], [1], [0, 0, 1]),                    # 連續進位
        ([1, 8], [0], [1, 8]),                       # 其中一邊為 0
    ]

    for a, b, expected in test_set:
        head1 = build_linked_list(a)
        head2 = build_linked_list(b)
        result_head = c.addTwoNumbers(head1, head2)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | l1={a} | l2={b} | expected={expected} | got={result}")

