# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
""" 
    思路 : 
        這一題給定一個數值 , 要我們把linked list上這個數值都移除 , 
        就是建立一個Dummy head , 然後透過prev , probe兩個指標去操作就好

"""

from typing import Optional 

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        probe = head 
        
        newhead = ListNode() 
        newhead.next = probe 
        prev =  newhead 
        
        while probe : 
            
            if probe.val == val : 
                prev.next = probe.next 
                probe = probe.next  
            
            else : 
                prev = probe 
                probe = probe.next 
        
        return newhead.next 