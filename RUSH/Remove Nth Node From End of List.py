# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional 

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = None 
        slow = head 
        fast = head 
        
        for i in range(n - 1): 
            fast = fast.next 
        
        while (fast.next): 
            prev = slow 
            slow = slow.next  
            fast = fast.next  
        
        if not prev is None : 
            
            prev.next = slow.next 
            return head 
            
        else : 
            
            return slow.next             