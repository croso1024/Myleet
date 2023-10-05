""" 
    此題為書本雙指標框架的範例之一 , 使用快慢雙指標來處理Linked List 
    
    要判斷一個Linked list內部是否有cycle , 可以透過不斷檢查節點的next屬性來看 ,
    一旦出現null , 則該linked list是沒有cycle的 , 但問題在於如果有cycle的情況我們就會陷入
    close-loop . 
    
    因此解決這個問題的慣用技巧就是一快一慢的雙指標 ,
    如果linked list沒有cycle , 快指標會先到達null 
    如果含有cycle,則快慢指標最終會相遇到並抓出cycle
    
"""


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" 
    解法一. 我閱讀基本概念後手刻
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None : return False
        
        slow = fast = head 
        
        # 脫離while迴圈代表fast-pointer走到none了 , 沒有cycle
        while fast.next  : 
            
            # 快指標一次前進兩格 , 如果遇到None , 代表這個Linked list沒有cycle
            fast = fast.next 
            if fast.next : fast = fast.next 
            else : return False 
            
            slow = slow.next 
            
            # 如果兩個指標彼此相遇 , 代表出現了cycle
            if slow == fast : return True 
            
        return False 
    
""" 
    解法二. 看書本的方式來做優化
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head 
        # 直接判斷本身和下一個節點是否為none , 是的話就能夠直接出去了        
        while fast and fast.next  : 
            
            # 快指標一次前進兩格 , 如果站上none,待會就出去了
            fast = fast.next.next 
            slow = slow.next 
            
            # 如果兩個指標彼此相遇 , 代表出現了cycle
            if slow == fast : return True 
            
        return False 