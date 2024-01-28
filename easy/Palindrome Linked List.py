# Definition for singly-linked list.
""" 
    題意 :  
        給定一個linked-list , 如果這個linked list是一個palindrome就回傳True 
        follow-up : 使用O(N)時間與O(1) 空間
        
    思路 : 
        這一題一個簡單的stack作法就是用快慢標 , 慢標放東西進stack , 快標把stack東西拿出來檢查抵銷 
        這樣就是O(N)時間 , O(N/2)空間 
        
"""
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


""" 
    解法一 , 快慢標搭配stack , 時空間O(N)
"""        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        stack = []
        
        while fast and fast.next : 
            
            stack.append(slow.val)
            slow = slow.next 
            fast = fast.next.next 
            
        # 出來代表快標走完了 , 如果fast is None : 說明linekd list長度為偶數 , 否則為奇數

        # linked list長度為奇數 , 則此時正中央還沒被放進stack 
        if fast : 
            
            slow = slow.next 
            
            while slow  : 
                
                if stack.pop() != slow.val : return False 
                slow = slow.next 
                
        # linekd list長度為偶數 , 此時slow已經走到右半邊
        else : 
            
            while slow : 
                
                if stack.pop() != slow.val : return False 
                slow = slow.next 
        
        return True 
                        
""" 
    解法二.  快慢標走到正中央 , 接著反轉後半段 , 重新開始走並比較 
        我原本使用recursion做反轉 , 但實際上這樣反轉會堆stack導致空間 , 速度都不差(即便理論時間複雜度O(N),空間O(1))
        修改為 while loop的反轉 , 基本上就ok
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: 

        def reverse(node):
            prev = None 
            curr = node 
            while curr : 
                next_node = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next_node
            return prev 
            
        slow = fast = head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
            
        # fast is None代表節點總數為偶數 , 此時slow正在左半最後 
        # fast != None 代表節點總數為奇數 , 此時slow就在正中間
        
        if fast is None : 
            probe = reverse(slow) 
            slow = head 
            
            while probe : 
                
                if probe.val != slow.val : return False 
                probe = probe.next 
                slow = slow.next 
        
        else : 
            probe = reverse(slow.next) 
            slow = head 
            
            while probe : 
                
                if probe.val != slow.val : return False 
                probe = probe.next 
                slow = slow.next 
        
        return True 
            
            
            
        