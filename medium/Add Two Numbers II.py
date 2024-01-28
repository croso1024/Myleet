""" 
    思路 : 
        這一題比起 Add Two Number II 感覺更有意義 , 是從低位數連接到高位數 
        
        思路上可以想到幾種解法的架構 :
        
        1. 反轉兩條list , 利用Add Two Number I 的方式相加後再次反轉 
        2. 東哥的想法除了也提到第一點 , 還有使用Stack先進後出也能作到反轉效果
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

""" 
    解法一 . 
        Stack解法 , 利用先進後出的性質去操作
        一開始先把所有節點存入Stack , 然後開始pop , 將pop出來的結果做相加直到有一邊空了
        
        速度上還可以 , 但空間我想是因為兩個stack + 新的Linked list , 空間不太好
"""

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        stack1 , stack2 = [] , []    
        probe1 ,probe2 = l1 , l2 
        
        #  把linked list1 加入stack 
        while probe1 : 
            stack1.append(probe1)
            probe1 = probe1.next 
        while probe2 : 
            stack2.append(probe2) 
            probe2 = probe2.next 
            
        # 開始一個個取出做相加 

        # 初始化進位變數與 "下一個節點" , 注意因為這一題是反轉串連 , 我們就是去紀錄下一個節點如果存在就將其連接
        carry = False 
        next = None 
        while stack1  and  stack2  : 
            
            node1 = stack1.pop()
            node2 = stack2.pop() 
            
            # 處理加法邏輯
            if carry : 
                cur_node = ListNode(val= node1.val+node2.val +1  )
                carry = False 
            else : 
                cur_node = ListNode(val = node1.val + node2.val )
            
            # 處理進位邏輯                            
            if cur_node.val // 10 > 0 : 
                cur_node.val = cur_node.val % 10 
                carry = True 
            
            # 如果next存在 ,把現在的節點連接上next 
            if next : 
                cur_node.next = next 

            next = cur_node 
        
        # 走到這邊,代表剩下一個stack有東西
        
        while stack1 : 
            node1 = stack1.pop() 
            
            if carry :
                cur_node = ListNode(val = node1.val + 1 )
                carry = False
            else :
                cur_node = ListNode(val = node1.val )
                
            # 處理進位邏輯                            
            if cur_node.val // 10 > 0 : 
                cur_node.val = cur_node.val % 10 
                carry = True 
            
            if next : 
                cur_node.next = next 
            next=cur_node
            
        while stack2 : 
            node2 = stack2.pop() 
            
            if carry :
                cur_node = ListNode(val = node2.val + 1 )
                carry = False
            else :
                cur_node = ListNode(val = node2.val )
                
            # 處理進位邏輯                            
            if cur_node.val // 10 > 0 : 
                cur_node.val = cur_node.val % 10 
                carry = True 
            
            if next : 
                cur_node.next = next 
            next=cur_node
        
        if carry : 
            cur_node = ListNode(val=1) 
            carry = False 
            cur_node.next = next 
            next = cur_node
        

        return next 
    

""" 
    解法二. 反轉兩個list , 然後走Add Two Number I的邏輯 , 最後將結果反轉
    
    這個作法反而是空間有變好 , 時間不太好
"""

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        new_head = [None,None,None]
        
        # 反轉linekd list  , i 表示存放新head的位置
        def reverse(node,i):  
            if node is None : return node
            next_node = reverse(node.next , i )
            if not next_node  is None : 
                next_node.next = node
                node.next = None 
            else : 
                new_head[i] = node 
            return node 
        
        reverse(l1 , 0)
        reverse(l2 , 1)
        
        l1 = new_head[0]
        l2 = new_head[1] 
        
        # 反轉兩條linked-list之後做 Add Two Number I 的套路
        
        sol = ListNode() 
        sol_probe = sol 
        prev = None 
        carry = False 
        
        probe1 = l1 
        probe2 = l2 
        
        while probe1 and probe2 : 
            
            if carry : 
                sol_probe.val = probe1.val + probe2.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe1.val + probe2.val 
            
            if sol_probe.val // 10 > 0 : 
                sol_probe.val = sol_probe.val % 10 
                carry = True 
            
            sol_probe.next = ListNode()
            prev = sol_probe
            sol_probe = sol_probe.next 
            probe1 = probe1.next 
            probe2 = probe2.next 
                
        while probe1 : 
            
            if carry : 
                sol_probe.val = probe1.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe1.val 
            
            if sol_probe.val // 10 > 0 : 
                sol_probe.val = sol_probe.val % 10 
                carry = True 
            
            sol_probe.next = ListNode() 
            prev = sol_probe 
            sol_probe = sol_probe.next 
            probe1 = probe1.next 
        
        while probe2 : 
                        
            if carry : 
                sol_probe.val = probe2.val + 1 
                carry = False 
            else : 
                sol_probe.val = probe2.val 
            
            if sol_probe.val // 10 > 0 : 
                sol_probe.val = sol_probe.val % 10 
                carry = True 
            
            sol_probe.next = ListNode() 
            prev = sol_probe 
            sol_probe = sol_probe.next 
            probe2 = probe2.next 
        
        
        if carry : 
            sol_probe.val = 1 
            carry = False 
        else : 
            prev.next = None 
        
        # 此時的sol , 就是反轉完成的兩個linked-list相加的結果 , 要再次將其反轉 
        reverse(sol , 2) 
        
        return new_head[2] 