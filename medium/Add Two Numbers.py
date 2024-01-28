
""" 
    思路 : 
        這一題簡單的想法是通過初始化一條額外的Linked list來完成 
        使用while迴圈同時走訪兩條linked list , 然後做加值 , 進位的操作
        一直走到其中一條沒有了以後 , 再將剩下的走完 
        
        這一題在演算法思維上不難 , 麻煩的點在於細節的處理 , 我犯下的細節錯誤包含 
        
        1. 在其中一條linked list走完後 , 仍然有可能進位的值會推廣到後面幾位 ( 而不是只有一條走完開始走下一條時的那一位 ) , 因此進位邏輯要繼續
        2. 走到最後一個值 , 如果沒有了 , 依照我的邏輯會初始化一個ListNode , 但這有可能是0因此要刪除
            而在刪除0的部份 , 原先我是直接做 sol_probe(指向最後一個節點) == 0時 , 直接將其值改為None 
            但忽略了這樣做實際上是一個重新賦值 , 前一個節點仍然指向那個==0的 , 因此需要一個prev指標去保存前一個節點 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        probe1 = l1 
        probe2 = l2 
        
        # carry表示進位的資訊
        carry = False
        # result就是新的 , 作為解答的Linked list 
        sol = ListNode()
        prev = None 
        sol_probe = sol 
        
        while probe1 and probe2 :  
            
            if carry : 
                sol_probe.val = probe1.val + probe2.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe1.val + probe2.val 

            # 進位發生 
            if sol_probe.val // 10  > 0 : 
                carry = True 
                sol_probe.val = sol_probe.val % 10 
            
            probe1 = probe1.next 
            probe2 = probe2.next 
            sol_probe.next = ListNode() 
            prev = sol_probe
            sol_probe = sol_probe.next 
        
        # 接下來處理的是只剩下一條的情況 ,要馬就是剩下 l1 , 或著 l2 
        
        # 假設剩下的是l1 
        while probe1 : 
            
            if carry :
                sol_probe.val = probe1.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe1.val 
                
            if sol_probe.val // 10 > 0 : 
                carry = True 
                sol_probe.val = sol_probe.val % 10 
                
            probe1 = probe1.next 
            sol_probe.next = ListNode() 
            prev = sol_probe
            sol_probe = sol_probe.next

        # 假設剩下的是l2
        while probe2 : 
            
            if carry :
                sol_probe.val = probe2.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe2.val 
                
            if sol_probe.val // 10 > 0 : 
                carry = True 
                sol_probe.val = sol_probe.val % 10 
                    
            
            probe2 = probe2.next 
            sol_probe.next = ListNode() 
            prev = sol_probe
            sol_probe = sol_probe.next

        # 最後的進位
        if carry : 
            sol_probe.val = 1 
            
        if sol_probe.val == 0 : 
            prev.next = None 
        
        return sol 