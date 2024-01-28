# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node): 
            if node is None or node.next is None : return node
            
            last_node = reverse(node.next) 
            node.next.next = node 
            node.next = None 
            
            return last_node
    
        return reverse(head)
        