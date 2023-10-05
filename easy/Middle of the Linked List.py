from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" 
    思路 : 
        這一題也是一個標準的Linked-list , 快慢指標框架可以解的題 , 
        看起來是一個快指標走到尾巴後看慢指標的位置就相當於中間 
        
        實做的細節主要就考慮到linked list的長度為奇數還是偶數 , 
        偶數的話一次跳兩步的fastPointer會遭遇有next ,沒有next.next , 應對在slow多一個next即可 

        在寫這一題的時候因為正在看雙指標框架 ,導致我有點先入為主 , 框架套的太快
        其實這一題比較普通的解法可能是先走一次linked list得到長度n, 
        接下來再走一次長度為n/2就好 
        
        另外這一題在實際應用中 , 可以被用在使用Linked list的merge sort尋找拆分中點上 

"""


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head  
        
        while fast and fast.next : 
            
            fast = fast.next.next  
            slow = slow.next  
            
        return slow 
                