# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 

class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if head is None : return None 

        lessList = ListNode() 
        greatList = ListNode() 
        
        leProbe = lessList
        gtProbe = greatList
        probe = head 
        
        while probe : 
            
            # node.val >= x -> In greatList 
            if probe.val >= x : 
                gtProbe.next = probe  
                gtProbe = gtProbe.next 
            else : 
                leProbe.next = probe 
                leProbe = leProbe.next 
                
            temp = probe 
            probe = probe.next 
            # cut off link
            temp.next = None  
        
        # 走完後, 把greatList的頭接在leProbe的尾巴
        leProbe.next = greatList.next 
        return lessList.next 
        