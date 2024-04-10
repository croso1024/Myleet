"""
    實做LRU cache ,
    用linked-list + hashmap , linked list用來maintain 最近使用的順序,
    同時hashmap提供快速的參照 , 尋找該key是否存在以及調整其在linked list中的順序
    
    linked list需要能夠從中間任意節點拿出該節點 , 然後將其放到最左或最右代表最新使用 ,
    同時maintain一個linked list長度最大值代表快取大小

"""

class ListNode : 
    
    def __init__(self,key ,val,prev=None,next=None) : 
        self.key = key 
        self.val = val 
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        
        self.maximum_capacity = capacity
        self.current_capacity = 0 
        self.hashmap = dict()
        
        # 我定義head代表最久沒用的, tail代表最靠近最新使用的
        self.head = ListNode(key = None , val=None)  
        self.tail = ListNode(key = None , val=None)

        self.head.next = self.tail 
        self.tail.prev = self.head 


    # 從hashamp中拿到對應節點的值 , 同時將該節點移動到tail的前一個 
    def get(self, key: int) -> int:
        
        if key not in self.hashmap : 
            return -1 
        else : 
            
            return_node = self.hashmap[key]
            self.renew(return_node) 
            return return_node.val
        

    # 在hashmap中放入或更新指定的節點 , 同時將該節點移動到tail的前一個
    def put(self, key: int, value: int) -> None:
        
        if key not in self.hashmap: 
            
            if self.current_capacity == self.maximum_capacity : 
                # 移除第一個最舊的節點
                removeNode = self.head.next 
                del self.hashmap[removeNode.key]   
                removeNode.next.prev = self.head 
                self.head.next = removeNode.next 
                self.current_capacity -= 1 
                
            newNode = ListNode(key = key , val=value) 
            self.hashmap[key] = newNode
            self.addnew(newNode)         
            self.current_capacity += 1 
            
        else : 
            
            updateNode = self.hashmap[key] 
            updateNode.val = value 
            self.renew(updateNode) 
    
    
    # 把指定節點移動到隊列尾巴, 只會用在已經有節點存在於list ,故 head -> 1 -> 2 -> ... -> n -> tail
    def renew(self,node): 
        
        if node == self.tail.prev : return
        
        prevNode = node.prev 
        nextNode = node.next 
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        lastNode = self.tail.prev 
        self.tail.prev = node 
        
        lastNode.next = node 
        node.prev = lastNode
        node.next = self.tail
    
    def addnew(self,node):
        
        lastNode = self.tail.prev  
        lastNode.next = node
        node.prev = lastNode 
        node.next = self.tail 
        self.tail.prev = node 
        

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2) 
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4) 
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))