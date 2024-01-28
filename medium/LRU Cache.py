""" 
    資料結構題 , 本題要實做LRU Cache algorithms , 具備
    
    1. 插入/更新 key-value  , 並將該組資料設置為最新  , 如果cache已經滿了 , 踢掉最舊的
    2. 查詢key , 如果存在於cache中 , 就返回該值 
    
    我們要使用一個double linked list來實做 , 同時要有一個hashmap去映射key
    分解具體需要的功能 
    
    - get. 透過hashmap去查詢key是否在cache , 同時要將查詢到的資料組"設置為最新"
    - put. 在cache未滿前 , 將其插入在最新的位置 , 若已經滿了,則要踢出最舊的再插入
    
    

"""


""" 
    為了完成此題的功能 , 需要實做一個double linked list , 我們把頭當作最新的值 , 
"""
class Node : 
    
    # 保留節點的key做查詢
    def __init__(self, key,value):   
        
        self.key = key 
        self.value = value 
        self.prev = None 
        self.next = None 


class DoubleLinkedList : 
    
    def __init__(self): 
        
        self.head = None 
        self.tail = None 
    
    # 在List最前方加入節點
    def add(self , node:Node): 
        
        if self.head  : 
            node.next = self.head 
            self.head.prev = node 
            self.head = node 
        else : 
            self.head = node
            self.tail = node 

    # 移除最尾巴的節點
    def remove(self): 
        
        if self.tail is None : raise RuntimeError("No node in linked list")            

        remove_node = self.tail 

        if self.tail == self.head : 
            self.head = None 
            self.tail = None 
        else : 
            self.tail = self.tail.prev  
            self.tail.next = None 

        return remove_node
    # 給定節點(透過hashtable查到) , 將其移動到Linked list的最前端 , 另外這個功能被call的時候一定是cache內有值 
    # /-> self.head & self.tail != None 
    
    def makeNew(self,node:Node):  

        # 代表說這個節點已經在最新了 , 就不操作了
        if node.prev is None : return 
        
        # node.prev.next = node.next 
        # if node.next :
        #     node.next.prev = node.prev 
            
            
        # node.next = self.head 
        # self.head.prev = node 
        # self.head = node 
        # node.prev =None

        if node == self.tail :  
            self.tail = node.prev  
            node.prev.next = None  
            node.prev = None 
            
            node.next = self.head 
            self.head.prev = node 
            self.head = node 
        
        else : 
            node.prev.next = node.next  
            node.next.prev = node.prev 
            
            node.prev = None 
            node.next = self.head 
            self.head.prev = node 
            self.head = node 
            


    def showList(self): 
        
        print(f"Show linked list")
        probe = self.head 
        while probe :
            print(probe.value)
            probe = probe.next
        print("----\n")
        


class LRUCache:

    def __init__(self, capacity: int):
        # capacity : 最大容量
        self.capacity = capacity 
        # 目前有的元素數 
        self.N = 0 
        # hashtable , 保存cache中的節點 , 使得查詢可以O(1)  
        self.table = dict() 
        # double linked list 
        self.cache = DoubleLinkedList()
        
        
    # put有兩種行為 , 加入新值或更新 , 但都需要將該值變為最新
    def put(self, key: int, value: int) -> None:
        
        # 先確認是不是要更新 , 如果不是 ->要添加值 -> 檢查容量
        if key in self.table : 
            
            self.table[key].value = value 
            self.cache.makeNew( self.table[key]  ) 
            
        # 要添加值 
        else : 
            
            # 達到容量 , 要先做刪除最舊再加入到頭 
            if self.N == self.capacity : 
                remove_node = self.cache.remove()
                self.table.pop(remove_node.key , None)
                self.N -= 1 
            
            node = Node(key,value)
            self.cache.add(  node  )
            self.table[key] = node 
            self.N += 1 
        
        
        
    # 取得資料的值,並且把他更新至最前         
    def get(self, key: int) -> int:
        
        if not key  in self.table : return -1 
        
        node = self.table[key]  
        self.cache.makeNew(self.table[key])
        
        return node.value 

    
    def showCache(self): 
        self.cache.showList()


# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
# param_1 = obj.get(5)
obj.put(1,1)
obj.put(2,2)
obj.showCache()
print("--",obj.get(1)) 
obj.showCache()
obj.put(3,3) 
obj.showCache()
print("--",obj.get(2))
obj.showCache()
obj.put(4,4)
obj.showCache()