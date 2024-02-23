"""
    We use heap to store the linked list(by the value of first node)

"""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListHead : 

    def __init__(self,linkedlist):
        self.l = linkedlist
    def __lt__(self,other):
        return self.l.val < other.l.val 
    def __eq__(self,other):
        return self.l.val == other.l.val 
    def __gt__(self,other): 
        return self.l.val > other.l.val 
  
    
from typing import Optional
from heapq import heappop , heappush
from typing import List 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        listPool = [] 
        
        for l in lists : 
            if l : heappush( listPool , ListHead(l) )     
            
        sol = ListNode(val=0) 
        probe = sol 

        while listPool : 

            linkedHead = heappop( listPool ) 
            probe.next = linkedHead.l
            probe = probe.next 
            
            if linkedHead.l.next : 
                linkedHead.l = linkedHead.l.next 
                heappush(listPool , linkedHead )
        
        return sol.next
            





























