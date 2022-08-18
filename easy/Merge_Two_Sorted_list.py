

class ListNode:
    def __init(self,val=0,next=None):
        self.val = val
        self.next = next 

class Solution:


    def mergeTwoLists(self,list1,list2):  
        
        self.solution = ListNode() 
        self.head = self.solution 
        while list1 and list2: 
            
            if list1.val <= list2.val: 
                self.solution.next = list1 
                list1 = list1.next 
            else : 
                self.solution.next = list2 
                list2 = list2.next 
            self.solution = self.solution.next 
        
        self.solution.next = list1 if list1 else list2 

        return self.head.next 

