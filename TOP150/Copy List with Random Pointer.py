class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head )  :
        
        dummy = Node(x=0) 
        connect_probe = dummy 
        check_probe = head 

        copy_table = dict() 
        # traverse origin linked-list 
        while check_probe :  

            if check_probe in copy_table : 
                copy_node = copy_table[check_probe] 
            else :
                copy_node = Node(x = check_probe.val) 
                copy_table[check_probe] = copy_node 

            if not  check_probe.random is None : 

                if check_probe.random in copy_table : 
                    copy_node_random = copy_table[check_probe.random] 
                else : 
                    copy_node_random = Node(x=check_probe.random.val) 
                    copy_table[check_probe.random] = copy_node_random 
                
                copy_node.random = copy_node_random 

            connect_probe.next = copy_node 
            connect_probe = connect_probe.next 
            check_probe = check_probe.next 

        return dummy.next 








