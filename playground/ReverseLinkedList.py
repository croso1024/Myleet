from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head : return head
        
        result = []
        
        while head : 
            result.append(head.val)
            head = head.next 
        
        result = result[::-1]
        new_head = real_head = ListNode( result[0] )
        
        for node in result[1:] : 
            
            new_head.next = ListNode(node) 
            new_head = new_head.next
        
        return real_head
        
        
    
    def reverseList(self,head): 
        
        if (not head) or (not head.next) : return head 
        
        current = prev = head 
        
        while current.next : 
            # next 先指向下一個節點 , 用來紀錄還原current 
            next = current.next 
            # 把現在的節點指向前一個節點 
            current.next = prev 
            # 把前一個節點更新成現在的節點 
            prev = current 
            # 把現在的節點更新成前面保存的next 
            current = next 
        head.next = None
        current.next = prev
        
        return current 