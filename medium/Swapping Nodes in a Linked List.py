# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" 
    思路:   
        給定一條linked-list , 以及常數k 
        將list中, 正面數過來第k節點與 倒數第k個節點做個swap 

        題目保證k的size小於等於linked list總長度
        
        為了要做swap ,我們都會需要去keep swap目標的前一個節點 , 
        
        而為了完成這一題的swap ,我們需要抓著四個節點  p1,t1 ,p2,t2 
        分別是 第k個節點的前個節點 , 第k個節點 , 倒數第k個節點的前一個節點 , 倒數第k個節點 
        
        step.1  要抓到第k個節點與其前一個節點 , 需要一個counter走 O(k) 
        step.2  要抓到倒數第k個節點與其前一個節點 , 則需要雙指標走O(N) 
        step.3  得到p1,t1,p2,t2 , 做swap操作 O(1) 
        
        實際實做發現會有很多特殊的case , 例如 t1,t2彼此相鄰 , 或著因為 
        k大於整條長度的一半導致t1實際上是在t2後面的case
        
        修改了一下我的實做 , 在找t1,t2的時候順便紀錄 t1,t2各自是第幾個節點 ,
        如此一來必要的時候就可以進行對調的工作 
        
        接著處理t1為開頭節點 , 以及t1,t2是相鄰的case即可
        這解法的速度還不錯 , 空間很差
        
        在Solution看到了另外一個解法 , 充分使用題意 , 題目可以只調換"value"
        
"""

""" 
    解法一. 找出前k後k  , 接著處理許多edge case

        時間O(N)還行 ,空間O(1) , 但用了蠻多變數
"""
class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None : return head 
        probe = head 
        t1 = head 
        n1 = 1 
        p1 = None 

        for _ in range( k - 1 ) :  
            probe = probe.next 
            p1 = t1 
            t1 = t1.next 
            n1 += 1 
            
        t2 = head 
        n2 = 1 
        p2 = None 
        while probe.next : 
           probe = probe.next 
           p2 = t2 
           t2 = t2.next 
           n2 += 1
        
        # 至此取得 n1,p1,t1 , n2,p2,t2 , 分別代表兩個目標是linked list中的第幾個節點  
        
        # 如果n1,n2是同個節點就直接return 
        if n1 == n2 :  return head 

        # 如果n1節點反而在n2後面 , 做 swap 
        elif n1 > n2 :  
            n1 ,n2 = n2, n1 
            t1 ,t2 = t2 ,t1 
            p1 ,p2 = p2 ,p1 
        
        # 接下來就確保了 t1,p1一定在t2,p2之前 
        
        # 如果t1,t2是相鄰的 
        if n1 + 1 == n2 :  
            
            if p1 is None : 
                t2.next = t1 
                t1.next = None 
                return t2  
            
            else : 
                t1.next,t2.next = t2.next ,t1
                p1.next = t2               
                return head 
        
        else : 
            
            if p1 is None  : 
                p2.next = t1 
                t2.next = t1.next 
                t1.next = None 
                return t2 
            
            else : 
                t1.next ,t2.next = t2.next , t1.next 
                p1.next = t2 
                p2.next = t1 
                return head 

""" 
    解法二. 
        只進行值的兌換  , 在速度上差不多 , 但空間有進步
"""

class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        probe = head 
        t1 = head 
        t2 = head 
        
        for _ in range(k-1): 
            probe = probe.next 
            t1 = t1.next 
        
        while probe .next : 
            probe = probe.next 
            t2 = t2.next
        
        t1.val , t2.val = t2.val , t1.val 
        
        return head 

""" 
    解法三. 
        進一步簡化解法二. , 減少了在尋訪過程的操作  速度很頂 , 空間普通
"""

class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        probe = head 
        temp_node = None 
                
        for _ in range(k-1): 
            probe = probe.next 
        
        temp_node = probe 
        temp_node2 = head 
        
        while probe.next : 
            probe = probe.next 
            temp_node2 = temp_node2.next 
            
        temp_node.val , temp_node2.val  =  temp_node2.val , temp_node.val 
        return head 