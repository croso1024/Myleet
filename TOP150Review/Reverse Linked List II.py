class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import  Optional

class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        def reverse(node) : 
            if node is None or node.next is None : return node 
            
            last_node = reverse(node.next)
            node.next.next = node 
            node.next = None 
            
            return last_node 
        
        
        # 先將left , right走到正確節點位置 , 保存right.next , 並將right.next = None 
        # 接著反轉left到right這段再做嫁接
        
        left_counter = 1 
        left_probe = head
        prev = None 
        while left_counter < left : 
            prev = left_probe
            left_probe = left_probe.next 
            left_counter += 1  
        
        right_counter = 1 
        right_probe= head
        while right_counter < right : 
            right_probe  = right_probe.next 
            right_counter += 1 
        
        # 此處就已經找到left , right 
        temp = right_probe.next # maybe有節點 , 也可能是None而已 
        right_probe.next = None 
        reverse_head = reverse(left_probe) 
        
        if prev is None : 
            # 如果prev是None , 代表reverse head就是新的head 
            left_probe.next = temp  
            return reverse_head
        else : 
            prev.next = reverse_head 
            left_probe.next = temp 
            return head 