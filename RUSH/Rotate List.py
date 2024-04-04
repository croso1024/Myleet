# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # get the length of linked list first , then use slow&fast pointer to solve this problem .
        if head is None : return None 
        length = 0 
        probe = head 
        while (probe) : 
            probe = probe.next 
            length += 1 

        k = k % length  

        if k == 0 : return head 
                
        prev = None 
        slow = head 
        fast = head 
        for i in range(k-1): fast  = fast.next 
        
        while fast.next : 
            prev = slow 
            slow = slow.next 
            fast = fast.next
        # after the while loop : 
        # fast is point to the original last node in the linked list 
        # slow is point to the node that will become the new head 
        # prev is point to the node that will become the last node 
        
        fast.next = head  
        if prev : 
            prev.next = None  
            return slow 
            
        else : 
            slow.next = None 
            return fast 
        
        
        
        