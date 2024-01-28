""" 
    思路 :  
        給定linked-list , 裡面已經是排序好的節點 , 要返回一條linked-list , 裡面所有的元素在原始linked-list都沒有重複
        , 這邊的思路就是去檢查當前probe和下一個 , 如果一樣就要跳過 , 一直到不一樣才代表可以將這個節點加入
        另外這一題 , 我的兩個寫法都會需要記得 , 把connect_probe的next砍掉 , 否則會保留那些本應該要移除的部份
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

""" 
    解法一. 基本上就是上面的思路 , 但有點土砲 , 太多edge-case的處理 不夠漂亮 
        速度倒還行蠻不錯的 , 空間不優
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None : return head 
        
        sol = None 
        connect_probe = None 
        check_probe = head 
        
        while check_probe.next : 
            
            if check_probe.val != check_probe.next.val : 
                
                if connect_probe is None : 
                    connect_probe = check_probe 
                    sol = connect_probe 
                else : 
                    connect_probe.next = check_probe 
                    connect_probe = connect_probe.next 

                check_probe = check_probe.next 
            
            else : 
                # 跳過所有相同值的部份
                temp = check_probe.val 
                while check_probe and check_probe.val == temp : 
                    check_probe = check_probe.next  
                # 最後要不是check probe == None , 就是已經脫離重複區 
                if check_probe == None : 
                    if connect_probe is None : return None 
                    else : 
                        connect_probe.next = None 
                        return sol 
        
        # 連接上最後一個節點 , 因為如果最後一個節點的前一個節點是和他一樣 , 就會被 else內的while給跳過了 
        if not connect_probe is None : 
            connect_probe.next = check_probe 
        else : 
            sol = check_probe
        
        return sol                                     
                
                
""" 
    解法二. 基本上就是希望寫的乾淨一點  , 速度些微慢一點 , 空間好一點
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sol = ListNode() 
        connect_probe = sol 
        probe = head 
        
        while probe and probe.next : 
            
            if probe.val != probe.next.val : 
                
                connect_probe.next = probe 
                connect_probe = connect_probe.next 
                probe = probe.next 

            # 遇到重複的 , 要開始跳躍 , 跳到下一個值為不重複的
            else : 
                temp = probe.val 
                while probe and probe.val == temp : 
                    probe = probe.next 
                
                # 來到這裡 , 要馬probe == None , 或著probe.val != temp , 這邊可以順暢回去接上半部while 
        
        # 到達這邊 , 就是probe == None 或probe.next == None  
        # 如果probe != None , 那他就可以接在解上 
        if not probe is None : 
            connect_probe.next = probe 
            connect_probe = connect_probe.next 
            
        connect_probe.next = None 
        
        return sol.next
                
                                    
                