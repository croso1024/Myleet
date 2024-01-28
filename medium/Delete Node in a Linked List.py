""" 
    題意 : 
        這一題不是常規的delete node in linked list , 題目給定了一條linked list , 
        '同時只給了linked list中要我們刪除的節點' ( 已知不會是linked list中最後一個節點 ) 
        我們要在只有拿到這個節點的情況下 , in-place的從原本的linked list中移除這個節點 
    
    思路 : 
        因為我們沒有實際上要移除的節點的前一個節點 , 因此我認為的作法就是 '修改節點的數值' , 
        從要刪除的節點開始 , 我們就是把下一個節點的數值拿來替換當前節點的數值 , 如此迭代 , 並且移除最後一個節點 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

""" 
    解法一. 
        如同上面的想法
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # 題目給定要刪除的節點必定不會是最後一個節點 , 因此確保這邊我們兩個next不會於一開始跳錯
        cur , next1 , next2 = node , node.next , node.next.next 
        
        # 只要當前視野內最後一個節點還有值, 就是做替換的工作
        while not next2 is None : 
            cur.val = next1.val  
            cur , next1 , next2  = next1 , next2 , next2.next
        
        # 跳出後 , 代表當前視野的最後一個節點已經空了 , cur , next1分別指向linked list最後兩個節點 
        # 在此 , 我們就是要把next1的節點值移動到cur上 , 同時把cur.next 指向None 
        cur.val = next1.val 
        cur.next = None 
    
        return 