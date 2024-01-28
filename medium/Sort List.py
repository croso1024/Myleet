""" 
    思路 : 
        一直沒有去動的複雜題 , 基本上就是要去實現對Linked list的merge sort
        使用到先前的 merge two linked list 以及要實做一個將linked list拆分為兩半的function
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        # 給定linked list , 透過快慢標去找到其中央節點 , 我們要返回這個節點來傳入下一層遞迴
        def getMid(l):
            slow = l 
            fast = l 
            # 如果只有兩個節點 , return 第一個
            if fast.next.next is None : return slow 
            while fast and fast.next : 
                fast = fast.next.next 
                slow = slow.next 
            return slow 
           
        # 傳入merge的兩條linked list都是已經排序好的 , 我們要用O(1)的空間將這兩條linked list串起來返回頭部
        def merge(l1,l2):
            
            # 合併兩條已經排序好的linked list , 使用一個dummy node
            dummy = ListNode() 
            probe = dummy 
            l1_probe , l2_probe = l1 , l2            

            while l1_probe and l2_probe : 
                
                if l1_probe.val < l2_probe.val : 
                    probe.next = l1_probe
                    probe = probe.next 
                    l1_probe = l1_probe.next 
                else : 
                    probe.next = l2_probe
                    probe=probe.next
                    l2_probe = l2_probe.next 
            
            # 走到這裡就是剩下一個還有沒被接上的
            while l1_probe:
                probe.next = l1_probe
                probe = probe.next 
                l1_probe = l1_probe.next 
            while l2_probe:
                probe.next = l2_probe
                probe=probe.next
                l2_probe = l2_probe.next 
            
            return dummy.next 
            
        # 傳入一個head , 進行merge sort 
        def mergeSort(node): 
            if node is None or node.next is None : return node 
            
            
            mid_node = getMid(node) 
            
            temp = mid_node.next 
            mid_node.next = None 

            left_list = mergeSort(node)
            right_list = mergeSort(temp)

            new_head = merge(left_list , right_list) 
            
            return new_head
        
        
        return mergeSort(head) 