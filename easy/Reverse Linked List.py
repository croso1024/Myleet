""" 
    大致上看了一下這一題我先前好像就有做過 , 當時時traverse一次linked list把所有節點加入list 
    然後反著過來重頭建立 , 
    
    基本上現在回來看會覺得透過遞迴的框架比較簡單輕易 , 透過post-order位置去串連整個linked-list ,
    透過遞迴探到最後一個節點後 , 設定一個新的指標在最尾節點 ,  
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 確保至少有一個節點 
        if head is None : return None 
        
        self.newHead = None 
        
        def traverse(node): 
            
            if node.next is None : 
                
                self.newHead = node
                
                return  node  
            
            next_node = traverse(node.next) 
            
            next_node.next = node  
            
            return node 
        # 經過traverse後所有節點的point都被搬往反方向了 , 但是最後一個節點head的next需要手動搬
        head = traverse(head) 
        head.next = None 
        
        return self.newHead 
    

""" 
    嘗試寫一個更加乾淨的版本 
"""
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None : return None 
        
        self.newHead = None 
        
        def traverse(node) : 
            
            if node is None : return None 
            
            next_node = traverse(node.next)  
            # 把下一個節點的next搬到指向自己
            if next_node : next_node.next = node  
            # 如果下一個節點為none , 代表該節點就是新的head 
            else : self.newHead = node 
            
            return node 
        
        head = traverse(head)
        head.next = None 
                
        return self.newHead  
    
    
""" 
    東哥版本的 , 主要在於去除了外部self.newHead的必要性 , 同時把回歸來的節點next改為None也包在遞迴函數裡頭 
"""
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node): 
            # base case , 如果只有一個節點或是沒有節點 , 那反轉後等於自己
            if node is None or node.next is None : return node 
            
            # next node就是反轉完成的Linked list , 同時
            next_node = reverse(node.next) 
            # 此時next_node是指向None的 , 因為已經完成反轉, 而我們當下的節點 next仍然是指向next_node
            node.next.next = node 
            node.next = None # 把當前要離開的節點next設置為None 
            
            # 返回的是反轉後的linked list head , 反著當我們出去這一層後仍然可以用前一層的node.next存取到這一層的內容
            return next_node  
        
        return reverse(head)