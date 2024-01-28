""" 
    題意 : 
        在不使用built-in 的前提下實做一個hashmap , 實現以下method : 
        void put(int key , int value) : 將 key:value放入map中 , 若key已經存在 , 則只是更新值
        int get(int key) : 透過key去找指定的value , 如果key不存在 ,返回-1
        void remove(key) : 若key存在於map , 則移除該組key:value
        
    思路 : 
        我不清楚這邊所謂的 implement without built-in hashtable 的意思是我可不可以使用dict , 
        若可以使用,則就直接使用dict , 就算要避免使用dict method , 其操作仍相當簡單
        
        另一種就是透過hash() , 去實做open address或著 separate chain 
"""

""" 
    解法一. 透過dict的實做
"""
class MyHashMap:

    def __init__(self):
        self.hashmap = dict() 

    def put(self, key: int, value: int) -> None:
        
        self.hashmap[key] = value 

        return 
        

    def get(self, key: int) -> int:
        
        if key in self.hashmap : 
            return self.hashmap[key] 
        else : 
            return -1 
        

    def remove(self, key: int) -> None:
        
        if key in self.hashmap : del self.hashmap[key] 
        
        return
        

""" 
    解法二. 實做separate chain , 速度和空間都沒有上面dict的實做好 , 但看起來酷炫許多
"""

class Node : 
    def __init__(self , key , value): 
        self.key = key 
        self.value = value 
        self.next = None 

class MyHashMap:

    def __init__(self):
        self.M = 777 
        self.hashmap = [None for i in range(self.M)]  
        


    def put(self, key: int, value: int) -> None: 
        
        hashvalue = key % self.M
        
        if self.hashmap[hashvalue] is None : 
            self.hashmap[hashvalue] = Node(key = key , value = value )
        else : 
            
            prev = None 
            probe = self.hashmap[hashvalue] 
            
            while probe : 
                
                if probe.key == key :  
                    probe.value = value 
                    return 
                
                prev = probe 
                probe = probe.next 
            prev.next = Node(key = key , value = value) 
        
        return 
                

    def get(self, key: int) -> int:
        
        hashvalue = key % self.M 
        
        probe = self.hashmap[hashvalue]
        
        if probe is None : return -1 
        
        while probe : 
            
            if probe.key == key : return probe.value 
            probe = probe.next 
        
        return -1 
        

    def remove(self, key: int) -> None:
        
        hashvalue = key % self.M 
        
        probe = self.hashmap[hashvalue] 
        
        if probe is None : return  
        
        prev = None 
        
        while probe : 
            
            if probe.key == key :  
                
                if not prev is None : 
                    prev.next = probe.next 
                else : 
                    self.hashmap[hashvalue] = None 
                    
            prev = probe 
            probe = probe.next 
        
        return
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)