""" 
    思路 : 
        這題要求我們用一個蠻詭異的順序去操作Linked-list , 以 1->2->3->4->5 來說
        
        要變成 1->5->2->4->3 , 也就是 頭尾頭尾 一邊跳一邊內縮 
        
        這一題比較直觀的想法 , 是透過O(N)去保存所有節點 , 
        然後雙指標從兩側逐漸內縮串連所有節點

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional


""" 
    解法一. 就先存下所有節點 , 然後雙指標協助串連 
    
        這個解法的速度跟空間就非常優秀了 , 蠻莫名的 , 那似乎空間上很難只有O(1) , 同時這個解法時間是O(N)
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
        Do not return anything, modify head in-place instead.
        """
        
        storage = [] 
        temp = head 
        while temp : 
            storage.append(temp)
            temp = temp.next 
            
        # 保存下所有節點 , 已知head是不會變的 , 所以我們left從1開始 , 初始化雙指標
        left = 1
        right = len(storage) - 1 
        
        # 我們用cur , 協助我們連接所有節點        
        cur = head 
        
        while left <= right : 
            
            # 一律先接right , 修改right , 才接left 
            cur.next = storage[right] 
            right -= 1  
            cur = cur.next 
            
            if not left <= right : break 
            
            cur.next = storage[left] 
            left += 1 
            cur = cur.next 
        
        cur.next = None  

        return head 