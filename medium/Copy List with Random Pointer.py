
""" 
    思路 : 
        此題給定一個節點結構特殊的Linked-list , 即每一個節點除了自己的值和next pointer外
        還有一個random pointer , 在Linked-list中指向隨機的節點 , 
        我們要產生一個Deep copy of node , 即除了值以外 , 節點之間point的關係也要與原始linked-list一樣
        
        
        對於這題 , 我的思路直觀會是建立hashmap , 保存尋訪節點的順序 , 值 , random pointer對象
        這一題的難點可能是在於 , 就算我們儲存了random pointer的對象 , 在走訪過程遇到時可能不易判斷 
        
        重新整理一次思緒 , 我就建立一個copy table  , key為原始節點 , value則是他的複製 ,
        在走訪的過程中,每一步 , 都先複製當前所在的節點 , 接著看他的pointer , 如果是一個已經存在copy表的就拿出來連接,
        沒有的話,複製一個, 連接並加入copy表
        
        這一題其實還不錯 , 我認為算是Linked list內需要好好思考拼接的一題
        
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #用來儲存原始節點與複製品
        copy_map = dict() 
        
        new_head = Node(x=0)
        new_probe = new_head 
                    
        probe = head 
        
        # 在每一輪中 , probe代表原始linked list的節點 , node則是他的複製品
        # random_node也是複製品節點 
        while probe : 
            
            if probe in copy_map : 
                node = copy_map[probe] 
            else : 
                node = Node(x = probe.val)
                copy_map[probe] = node 
                
            # 如果該原始節點的random指向的不是None , 那就看copy-map有沒有他的random所指向的 , 找到或建立複製品後接上去
            if not probe.random is None :    
                
                if probe.random in copy_map: 
                    random_node = copy_map[probe.random] 
                else : 
                    random_node = Node(x = probe.random.val)
                    copy_map[probe.random] = random_node 
                
                node.random = random_node
            
            new_probe.next = node 
            probe = probe.next 
            new_probe = new_probe.next 
        
        return new_head.next 
        
        
            

        
            
            
                    
