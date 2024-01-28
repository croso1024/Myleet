# Definition for singly-linked list.
from typing import Optional
""" 
    題意 :  
        給定一條長度為n的linked list , 已知n必定是偶數 , 並且定義所謂的twin node , 
        對於index為 0<=i<=(n/2)-1 的節點來說 , twin node 就是節點 i 與節點 (n-1-i) , 例如在六個節點的linked list中
        index = 0 , 1, 2的twin node分別是 5, ,4 ,3 
        現在題目要求整個linked list中 twin node值最大的組合
        
    思路 : 
        這一題換句話就是要找哪個組合的總和最大 , 最直觀的想法可以直接將整個list的值存進一個array ,
        之後從兩端走O(N)計算總和來更新就是答案 , 如此一來時間為O(N) , 空間也為O(N) 
        
        我認為這一題應該希望我們有個空間為O(1)的作法

        

"""


""" 
    解法一. 比較直觀的存值與使用 , 時間空間都是O(N) 
        這邊有個小抉擇 , 因為一開始不知道linked list的長度為何 ,可以選擇
        1. 直接走linked list並且不斷append值 , 這樣需要完整O(N)空間 
        2. 先走一次linked list得到總長度 , 接著初始化一塊大小為O(N/2)的空間 , 再走一次O(N)來填充 

        這邊直接採用第一種作法 , 比較直接簡單
        速度還不錯 , 空間偏差 , 如預期那樣
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ref = list() 
        probe = head 
        while probe : 
            ref.append(probe.val) 
            probe = probe.next 
        
        size = len(ref)         
        # 得到一個O(N)長度的每個節點的值 , 以及整條list的長度
        best = 0  
        for i in range(size//2): 
            
            if ref[i] + ref[size-1-i] > best :
                best = ref[i] + ref[size-1-i] 
        
        return best
    

""" 
    解法二. 這邊用快慢標去實做一個更好的解法 , 
        概念上類似於上面提到先走linked list得到總長度 , 接著初始化一半空間的概念 ,
        我用快慢標 ,也同樣初始化一個list 
        在快標走到底之前使用慢標去加入list , 一旦快標走到底 ,
        那接下來就不繼續增加ref的長度 , 由慢標去加總ref的best
        
        這個解法我認為在概念上比起第一個更好 , 但實際結果就是速度差不多 , 空間有些微提昇 ,
        我一開始是寫counter 來處理slow走得時候的計算 , 但在Solution看到把ref當作stack的概念更漂亮一點 
        雖然性能沒什麼提昇
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head 
        ref = list()

        # 因為保證linked list長度為偶數 , 這邊只要確認fast指標

        while fast : 
            ref.append(slow.val)
            slow = slow.next 
            fast = fast.next.next 

        best = 0 
        # 讓slow繼續走 , 同時更新best 
        while slow : 
            
            best = max(best , slow.val + ref.pop())
            
            slow = slow.next 

        return best 

""" 
    解法三. 要讓空間為O(1) , 則可以將linked-list做反轉 ,  
        但我們只需要反轉半條 , 透過快慢標去做找中間 , 之後且一個反轉的function做這件事情
        
        這一題在理想上計算速度也是O(N) ,空間則是O(1) , 但實際上因為遞迴的層數太多反而用了更多記憶體空間
"""

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 反轉linked list 
        def reverse(node): 
            if node is None or node.next is None : return node 
            
            last_node = reverse(node.next) 
            node.next.next = node 
            node.next = None 
            
            return last_node 
        
        # 快慢標 
        slow = fast = head 
        
        while fast :  
            slow = slow.next 
            fast = fast.next.next     
        
        # 將慢標指向的這一段做linked list反轉 ,並取得他的head 
        # 注意慢標會停在 index = n//2  , 我們要以這個反轉的linked list長度走訪為主
        probe1 = reverse(slow)
        probe2 = head 
        best = 0
        while probe1 :  
            
            best = max(best , probe1.val + probe2.val  )            
            probe1 = probe1.next 
            probe2 = probe2.next 
        
        return best