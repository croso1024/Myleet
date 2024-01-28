
""" 
    思路 : 
        這一題要在Linked list上要我們實現insertion sort , 
        我的概念是先走訪一次紀錄一個順序:節點表 , 
        
        接著從第二個節點開始拿出來 , 把他插在第一個或後面, 
        換句話說,拿出第i個節點 , 把他插在 1~i的位置
        
        基本上應該就是in-place操作 , dict只是要保存一個所有節點的參照 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

""" 
    解法一. 
        就是做insert sort, 雙迴圈 , 有一些小細節要特別注意,
        即probe=new_head 這個new_head的更新方式 , 以及最後一個節點的next要變為None避免cycle 
"""

class Solution:
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 走訪第一次 , 保存所有節點 , 以順序為key 
        count = 0 
        probe = head 
        node_map = {} 
        max_node = None 
        while probe : 
            node_map[count] = probe 
            if not max_node is None : 
                max_node = probe if probe.val > max_node.val else max_node
            else : 
                max_node = probe 
            probe = probe.next 
            count += 1 
        
        
        # 接下來雙迴圈做insert  , 從第一個節點開始
        # scope 代表這次insert最多檢查到linked list的最大範圍 , 同時也代表這次要取出的節點是哪個
        new_head = node_map[0]
        for scope  in range(1, count) :  
            
            node = node_map[scope]
            
            count2 = 0 
            
            # 為了要順利做插入節點 , 保持一個prev 
            prev = None 
            probe = new_head  # 注意這邊probe是new_head 開始 ,不是原始的head 
            insert_done = False 
            
            while count2 < scope and not insert_done : 
                # 節點的值比較大 , 繼續往後走 
                if node.val > probe.val : 
                    prev = probe 
                    probe = probe.next 
                    count2 += 1 

                # 找到一個比node還大的節點了 , 待表要插入在這 
                else : 
                    # 如果prev是None , 代表這個目前要插入在第一個位置成為new_head 
                    if prev is None : 
                        node.next = probe 
                        insert_done = True 
                        new_head = node 
                    else : 
                        prev.next = node 
                        node.next = probe 
                        insert_done = True 
                
            # 如果走到這邊 , 還沒插入的話,就相當於該節點插在目前scope的尾巴
            
            if not insert_done:
                prev.next = node  
                node.next = probe

        max_node.next = None 
        
        return new_head
    


""" 
    解法二. 
        這題實際上不需要先做O(N)的遍瀝 , 我們只需要每次都拿出上一次搜索範圍的下一個節點
"""
class Solution:
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        new_head.next = head 
        
        prev , cur = head , head .next 
        
        
        while cur : 
            if cur.val >= prev.val : 
                prev , cur = cur , cur.next 
                # 順序沒錯的地方都不用改 , 同步移動prev , cur         
                continue

            # 走到這裡代表prev > cur 
            # 接著初始化一個tmp        
            tmp = head 

            while cur.val > tmp.val : 
                tmp = tmp.next 
                
            prev.next = cur.next 
            cur.next = tmp.next 
            tmp.next = cur 
            cur = prev.next 
        
        return new_head.next
            