from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" 
    此題也為書本快慢雙指標的範例題目 , 除了檢查linked-list內是否包含cycle,
    同時需要返回cycle的起點 , 因此除了沿用easy版本使用雙指標偵測cycle以外還加入了額外的處理
    
    而這一題tricky的部份也在此 , 假設linked-list內存在cycle , 則當快慢指標相遇時 , 
    如慢指標走了k步 , 快指標必然走了2k步 , " 從此可推得k必須是cycle的整數倍 " (詳見圖)
    我們令cycle的起點到相遇點距離為 m (m<k), 則可以知道linked-list的head到cycle起點為 k-m (因為慢指標)
    而從相遇點重新走到cycle的起點也剛好是k-m
"""


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head 
        
        while fast and fast.next : 
            
            fast = fast.next.next 
            slow = slow.next 
            # 找到相遇點 , 開始後續操作,就不跳出while了 
            if fast == slow : 
                
                # 重新初始化一個指標在head , 讓他們用同樣的速度前進,並且紀錄步數
                fast = head 
                step = 0 
                # 相遇後代表有cycle , 就不考慮會遇到none了 
                while not fast == slow :  
                    fast = fast.next 
                    slow = slow.next 
                    step += 1 
                
                return fast 
        
        return None
            
        