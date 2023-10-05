# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        
        node = head 
        count = 0 
        while  node : 
            count+=1 
            node = node.next 
        # get the length of linked list 
        target = count - n  -1 
        if count == n : 
            
            return head.next
        
        node = head 
        while target : 
            target-=1
              
            node = node.next 
        
        node.next = node.next.next   
        
        return head  
    
# faster than 83 % , memory less than 70%  

class Solution2:
    def removeNthFromEnd(self, head, n: int) :
        
        node = head 
        temp = {}
        count = 0 
        while node:
            temp[count] = node
            count+=1  
            node = node.next 
        if count == n : return head.next 
        elif n == 1 : 
            temp[count-2].next = None 
            return head 
        else : 
            temp[count-n-1].next = temp[count-n+1] 

             
        return head 
        

test1 = ListNode(0) 

node1 = ListNode(1)
#test1.next = node1 
#node1.next = ListNode(2) 

def show(head):
    for i in range(5): 
        if head:
            print(head.val)
            head = head.next
        else : 
            print(-1)
S = Solution() 
test1 = S.removeNthFromEnd(test1,1) 
show(test1)

""" 
    以上為古早寫法 
"""

""" 
    此題要求我們移除在Linked list中"倒數"第n個節點 , 直接透過遞迴的思路從最後一個節點往回走 ,
    
    我原先的解題思路 : 
    
        當我們離開節點回到上一層節點的當下 , count代表著上一層(也就是當前節點的next)是串列中的倒數第幾個節點 , 
        如果上一層節點就是要移除的目標 , 就可以輕易的透過當前節點的next指向被移除節點的next 
        
        不過會需要補上一個檢查 , 檢查離開head的當下 , head是list中的倒數第幾個節點 , 如果head才是要移除的對象 ,
        直接把head指向next就可
    
    東哥版本解法 , 
        使用快慢雙指標 , 為了要移除倒數第n個節點 , " 我們需要找到倒數n+1個節點 " , 
        初始化兩個指標,並讓fast先走n個節點 , 當fast走到最後一個節點 , 則slow指標也停在倒數n+1個節點上了 ,
        即slow的next就是我們要移除的目標

"""

""" 
    解法一. 遞迴反向解決
"""


from typing import Optional
 
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        count = 0
        
        def traverse(node): 
            nonlocal count 
            if node is None : return None         
            
            traverse(node.next) 
            # 離開一個節點後就來檢查一下剛剛那個節點是倒數第幾個  , 如果是我們要移除的目標 , 就把當下節點指向他的下一個
            if count == n : node.next = node.next.next 

            # 每離開一次節點就增加一個倒數    
            # count代表的當下這一層遞迴的節點是倒數第幾個 
            count += 1 
        
        traverse(head)
        if count == n : 
            head = head.next 
        
        
        return head
    
""" 
    解法二. 雙指標戰術 , 很省空間因為省去了遞迴深度 , 主要就是細節的處理 , 快指標要先走幾步這些操作
"""

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # # 只有一個節點就直接砍掉了
        # if head.next is None : return None 

        # 初始化快慢雙指標 
        slow = fast = head 
        # 先讓快指標走n步 , 已知linked list的長度必須大於等於n 
        for i in range(n) : 
            fast = fast.next  
        
        # 如果fast直接走到None了 , 那代表砍第一個節點
        if fast == None : return slow.next 
        
        # 當快指標走完n步後還有下一個 , 就繼續同步前進 , 走到快指標到底  
        while fast.next : 
            
            fast = fast.next 
            slow = slow.next 
            
        # 當快指標沒有下一個了 , slow的下一個就是目標
        slow.next  = slow.next.next 
        
        return head 
    
""" 
    補充 : 如果只是要找倒數第k個節點 
"""
def findLastKthNode(head , k) : 
    
    slow = fast = head 
    
    for i in range(k) : fast = fast.next 
    
    while fast : 
        fast = fast.next 
        slow = slow.next 
        
    return slow 