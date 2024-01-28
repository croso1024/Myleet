""" 
    題意 : 
        給定一串linked-list , 要我們將 奇/偶數 index的節點串成一組 , 舉例來說
        1->2->3->4->5 , 要串成  1->3->5->2->4 , 也就是奇數 1,3,5 th節點按照原始順序一組 , 接著是偶數的節點
        題目要求 O(1) space + O(N) time complexity 
        
    思路 :
        這一題我的直觀想法就是兩個probe去做穿線 , 
        第一個probe負責穿 奇數節點 , 用一次跳兩步的方式 , 串完後再串第二支 
        
        我第一次實做的方法是初始化probe , odd_probe ,even_probe , 後兩者用跳步的方式來串連,
        但實際上會遇到odd_probe串連完成後 , even_probe出現問題的情況 , 
        因此我認為需要 '交錯的串連兩條list' , 但同時也要保有最初的odd/even_head  
        上面這個第二次實做可以精簡為只使用單一指標 , 但我最終使用一個step計算節點數量 ,方便判斷指標跳出的位置是落在odd-list還是even-list
        的最後一個節點. 並以此進行對應的相接工作。
        
        
        
        
        
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None : return head 
        
        probe, ref = head, head.next  
        prev = None 
        step = 1
        
        while probe and probe.next : 

            prev = probe 
            temp = probe.next 
            probe.next = probe.next.next 
            probe = temp
            step += 1 
        
        # print(step) 
        # print("head list")
        # c = head 
        # while c : 
        #     print(c.val)
        #     c = c.next 
        
        # d = ref 
        # while d  :
        #     print(d.val)
        #     d = d.next 
        
        # 若總長度為奇數 , 則probe為最後一個節點 
        if step % 2 == 1 : 
            probe.next = ref 
        else : 
            prev.next = ref 
        
                    
        # if probe is None : 
        #     prev.next = ref 
        # else : 
        #     probe.next = ref 
            
        return head 
        
        
        
        