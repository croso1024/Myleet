# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) :
        
        # go through two linked-list , and record the backward-reference,
        # next , back-trace the every node , until the previous node refer to different source 
        
        # get the backward-reference for both linked-list 
        record_A = [None] 
        record_B = [None]

        while headA.next :   
            record_A.append(headA)  
            headA = headA.next  
            
        while headB.next : 
            record_B.append(headB)
            headB = headB.next         
        
        if len(record_A) == 1 and len(record_B) == 1 :
            return headA if headA == headB else None 
        
        # headA , headB is refer to last node in linked-list now , 

        # special-case , if last node is intersection 
        if not (record_A[-1] == record_B[-1]) and headA == headB : return headA 
        elif not (record_A[-1] == record_B[-1])  and  not headA == headB : return None 

        else :         
            # back-trace  
            for i in range(  min(len(record_A),len(record_B) ) - 1 ) : 
                if record_A[ len(record_A)-1-i ] == record_B[ len(record_B)-1-i ]: 
                    target = record_A[ len(record_A)-1-i ] 
                else :  
                    return target

            return target