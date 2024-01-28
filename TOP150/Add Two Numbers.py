# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# 除了相加還要處理進位邏輯
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        probe_a = l1 
        probe_b = l2 
        
        sol = ListNode()
        connect_probe = sol 
        
        # 控制進位
        carry = False 
        while probe_a and probe_b :  

            # 處理進位邏輯 
            if carry : 
                temp = probe_a.val + probe_b.val + 1 
                carry = False 
            else : 
                temp = probe_a.val + probe_b .val
            # 處理新的值是否可以進位
            if temp >= 10 : 
                carry = True 
                temp -= 10  
            
            connect_probe.next = ListNode(val = temp) 
            connect_probe = connect_probe.next 
            probe_a = probe_a.next 
            probe_b = probe_b.next             

        # 至此就是只剩下一條linked-list或著都沒了 
        while probe_a : 

            if carry : 
                temp = probe_a.val + 1 
                carry = False 
            else : temp = probe_a.val 
            if temp >= 10 : 
                carry = True 
                temp -= 10  
            connect_probe.next = ListNode(val = temp) 
            connect_probe = connect_probe.next 

            probe_a = probe_a .next 
            
            
            
        while probe_b : 
            
            if carry : 
                temp = probe_b.val + 1 
                carry = False 
            else : temp = probe_b.val 
            if temp >= 10 : 
                carry = True 
                temp -= 10  
            connect_probe.next = ListNode(val = temp) 
            connect_probe = connect_probe.next 

            probe_b = probe_b .next 
            
        if carry : 
            connect_probe.next = ListNode(val = 1) 
            connect_probe = connect_probe.next 

        
        return sol .next
    


# 不使用新的linked-list , 直接在原本的linked-list上面操作 
# 把值都加在l1上 , 如果l1沒了才移花接木到l2
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = False 
        dummy = ListNode()
        # probe會晚一格 , 用來當l1 or l2走到None時的銜接
        probe = dummy

        while l1 and l2 : 
            
            if carry :
                l1.val = l1.val + l2.val + 1
                carry = False 
            else :
                l1.val = l1.val + l2.val 

            if l1.val >= 10 : 
                l1.val = l1.val - 10 
                carry = True 

            probe.next = l1 
            probe = probe.next 
            l1 = l1.next 
            l2 = l2.next 

        # 如果l1以經空了 , 要把probe接上l2 , 如果沒有carry接完就是答案了
        if l1 : 
            probe.next = l1 
            probe = probe.next 
        elif l2 : 
            probe.next = l2
            probe = probe.next 
        else : 
            if carry : 
                probe.next  = ListNode(val=1) 
            return dummy.next         
        
        
        if not carry : return dummy.next 

        else : 
            
            while probe and carry : 
                probe.val = probe.val + 1  
                carry = False 
                if probe.val >= 10 : 
                    probe.val = probe.val -  10 
                    carry = True 
                
                if probe.next :                 
                    
                    probe = probe.next  
                    
                    
                elif not probe.next and carry : 
                    probe.next = ListNode(val=1)
                    return dummy.next 

        return dummy.next 
        