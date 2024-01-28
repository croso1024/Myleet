# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

""" 
    思路:   
        這一題要做的只是砍掉linked list中間的節點 , 題目告知中間的節點指的是 floor(n/2) , 
        即5個節點要砍掉index=2的 ,6個節點要砍index=3的  
        
    最簡易思路可能是先走O(N)去計算節點數量 , 然後第二趟帶著prev走到中央後操作 ,

    這邊直接實做快慢標 , 慢標會帶著prev一起走 , 這一尋訪一次就結束了
        
    
"""


""" 
    解法一. 簡單的實做快慢標 , 速度與空間都很優
"""
class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head 
        fast = head 
        prev = None 
        
        
        while fast and fast.next : 
            
            prev = slow 
            slow = slow.next 
            fast = fast.next.next  
            
        # 到此就是走到底了 , 此時slow指向要砍的標
        
        # 要砍的就是第一個節點 , 或著說也只有一個節點
        if prev is None : return None 
        
        prev.next = slow.next  
        
        return head 
            