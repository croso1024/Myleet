from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2 : return list1 
        elif  list1 and not list2 : return list1 
        elif list2 and not list1 : return list2 
        else : 
            
            new_head = ref = ListNode(val=None) 
            
            while list1 and list2 : 
                
                if list1.val < list2.val : 
                    new_head.next = ListNode(val = list1.val) 
                    list1 = list1.next 
                else : 
                    new_head.next = ListNode(val = list2.val) 
                    list2 = list2.next 

                new_head = new_head.next 
            
            if list1 : 
                while list1 : 
                    new_head.next = ListNode(val = list1.val) 
                    list1 = list1.next 
                    new_head = new_head.next 
            else : 
                while list2 : 
                    new_head.next = ListNode(val = list2.val) 
                    list2 = list2.next 
                    new_head = new_head.next 
            
            
            return ref.next