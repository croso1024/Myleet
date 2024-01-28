""" 
    思路 : 
        把同一層之間的節點做個串連 , 基本上算是階層尋訪的套路 
        我這邊覺得可以BFS , 然後在尋訪一層BFS的時候去用一個輔助probe串連 node 
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque

""" 
    解法一. Implement BFS , 因為Tree的結構本身不會回頭 , 因此不需要做visited array
    空間不錯 , 速度上略差 , 但我覺得其實差不多是clear了
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root is None : return root 

        Queue = deque() 
        Queue.append(root) 
        
        while Queue : 
            
            size = len(Queue) 
            # probe 指向該層級的第一個節點 
            probe = None
            
            for i in range(size): 
                
                cur_node = Queue.popleft() 

                if cur_node.left : 
                    Queue.append(cur_node.left) 
                
                if cur_node.right: 
                    Queue.append(cur_node.right) 
                    
                # 操作Probe 串連同一個階層的節點
                if not probe is None : 
                    probe.next = cur_node 
                    probe = probe.next 
                else : 
                    probe = cur_node 
                    
        
        return root 

""" 
    解法二. 透過hashmap操作各個深度 , 速度更快一些 , 空間較差 ,
            我猜是因為雖然hashmap保存O(h) , 但遞迴太深
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        hashmap = dict() 

        def traverse(node,depth): 
            if node is None : return 
            
            if depth in hashmap : 
                hashmap[depth].next = node 
                hashmap[depth] = node  
            else :
                hashmap[depth] = node 
            
            traverse(node.left , depth+1 )
            traverse(node.right  , depth+1)
        

        traverse(root , depth=0)
        return root 