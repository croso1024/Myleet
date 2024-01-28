class MyHashSet:

    def __init__(self):
        
        # 由於題目給定key的範圍在 0<=key<=10^6 , 我們直接初始化一塊memory用來作保存
        self.container = [False for  i in range(pow(10,6)+1)] 
        
    def add(self, key: int) -> None:
        
        self.container[key] = True
        

    def remove(self, key: int) -> None:
        
        self.container[key] = False 

    def contains(self, key: int) -> bool:

        return self.container[key]
        

""" 
    動態擴張的版本 , 速度與空間有明顯提高 , 但仍然算是不佳
"""
class MyHashSet:

    def __init__(self):
        
        # 修改為動態擴容的版本
        self.container = []
        self.size = 0 
        
    def add(self, key: int) -> None:
        
        if key >= self.size : 
            for i in range(key-self.size+1): self.container.append(False)
            self.size = len(self.container)
        
        self.container[key] = True
    

    def remove(self, key: int) -> None:
        if key >= self.size : return 
        self.container[key] = False 

    def contains(self, key: int) -> bool:
        if key >= self.size : return 
        return self.container[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)