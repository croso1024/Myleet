# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

""" 
    使用了一條新的 linked-list 
"""
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        probe_a = list1 
        probe_b = list2 
        
        dummy = ListNode() 
        connect_probe = dummy 
        
        
        # 在兩條linked-list還在的時候就是比大小來選擇連接的東西 
        while probe_a and probe_b  : 
            
            if probe_a.val < probe_b.val : 
                connect_probe.next = probe_a 
                connect_probe = connect_probe.next 
                probe_a = probe_a.next 
            else : 
                connect_probe.next = probe_b 
                connect_probe = connect_probe.next 
                probe_b = probe_b.next  
        
        # 至此後 , 只剩下其中一條有值 
        while probe_a : 
            connect_probe.next = probe_a 
            connect_probe = connect_probe.next 
            probe_a = probe_a.next 
        while probe_b : 
            connect_probe.next = probe_b
            connect_probe = connect_probe.next 
            probe_b = probe_b.next 
        
        return dummy.next 



""" 
    in-place 操作一條linked list 
"""
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 : return list2 
        elif not list2 : return list1  
        
        if list1.val < list2.val : 
            sol_head = list1 
            connect_probe = list1
            probe_a = list1.next 
            probe_b = list2 
            
        else : 
            sol_head = list2 
            connect_probe = list2
            probe_a = list1 
            probe_b = list2.next 
            
        # probe_a, probe_b 用來保存"下一個參考"
        
        while probe_a and probe_b : 
            
            if probe_a.val < probe_b.val : 
                connect_probe.next = probe_a 
                connect_probe = connect_probe.next 
                probe_a = probe_a.next 
            else : 
                connect_probe.next = probe_b
                connect_probe = connect_probe.next 
                probe_b = probe_b.next 
            
        if probe_a : 
            connect_probe.next = probe_a 
        if probe_b : 
            connect_probe.next = probe_b 
        
        return sol_head 


class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 : return list2 
        elif not list2 : return list1  
        
        dummy = ListNode()
        probe = dummy
        
        while list1 and list2 : 
            
            if list1.val < list2.val : 
                probe.next = list1 
                probe = probe.next 
                list1 = list1.next 
            else : 
                probe.next = list2 
                probe = probe.next 
                list2 = list2.next 
        
        if list1 : 
            probe.next = list1 
        else : 
            probe.next = list2 
        
        return dummy.next 
            
            
            