""" 
    題意 : 
        給定一條linked list , 同時給定一個值x .
        將這條linkedlist修改為 : 所有小於x的節點 -> 大於等於x的節點
        同時維持這條linked list節點間原始的相對順序
    
    思路 : 
        一個probe負責往前探 , 另外兩個probe分別接在 小於x節點 / 大於x節點 linked list的head 
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional 


""" 
    解法一. 
        基本上就是follow最一開始的想法 , 用probe去做承接 
        這個解法的時間複雜就是O(N) , 不過實際跑得結果普通 , 空間則算是很不錯 , 使用常數空間複雜度
"""
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
            
        probe = head 
        # l1 , l2 分別代表小於/大於等於x節點所構成的linked list 
        l1,l2 = None  , None 
        l1h , l2h  = None  , None 
        while probe : 
            
            # 先紀錄下當前probe指向的節點 
            temp = probe             
            probe  = probe.next 
            
            if temp.val < x :  
                
                if l1 : 
                    l1.next = temp  
                    l1 = l1.next 
                    l1.next = None 
                else : 
                    l1 = temp 
                    l1h = temp 
                    l1.next = None  
                    
            
            else : 
                
                if l2 : 
                    l2.next = temp  
                    l2 = l2.next 
                    l2.next = None 
                else : 
                    l2 = temp 
                    l2h = temp 
                    l2.next = None 

        
        # 至此 , l1 ,l2 分別指向各自linked list的最後一個節點 , 但我們會需要在第二群(大於等於的head)
        # 如果存在大於等於的節點 
        if l1h and l2h : 
            l1.next = l2h 
            return l1h 

        return l1h if l1h else l2h 
        
        