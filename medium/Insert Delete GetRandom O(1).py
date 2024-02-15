""" 
    題意:
        實做一個RandomizedSet class , 包含以下功能
        1. insert : 插入指定數值到集合中 , 回傳True如果這個數值還沒有出現在set並插入 
        2. remove : 從集合中移指定數值 , 回傳True如果這個數值在集合中並且被移除
        3. getRandom() : 從集合中隨機返回一個數值 , 注意每個數值被返回的機率都要相等 
        所有操作的time complexity都要O(1) 
        
    思路:

        這一題我認為比較需要思索的是random的來源,如果無法使用built-in random要如何做?
        我自己是認為可以用round robin的方式來插入數值 , round robin確保所有值都會均勻的出現,
        但就不是真的隨機.
        
        回到集合本身 ,我認為比較麻煩的作法是hashmap + linked list, 但我想應該不用這麼麻煩.
        最簡單就是hashMap , 使用hashMap的猶豫點在於怎麼樣做random  ,
        可能需要搭配list 或 queue , 利用hashmap去存他們在list中的位置 , 而透過circular buffer或deque去做round robin
        這邊最關鍵的問題在於 , 要remove的時候我們就算有index , 但操作數組從中間pop掉一個值還是對時間複雜度很差 .
        
        這裡的解決方法就是直接將該index的數值與最後一個數值對調,再做pop這樣就O(1)
        
        -- 最後實現round robin,但似乎被判定不夠隨機才error , 改用built-in random
        

"""
from collections import deque
from random import randint
class RandomizedSet:

    def __init__(self):
        
        self.hashMap = dict()
        self.storage = deque()

    def insert(self, val: int) -> bool:
        
        if val in self.hashMap : return False 
        else : 
            self.storage.append(val) 
            self.hashMap[val] = len(self.storage) - 1 
            return True 
        
    def remove(self, val: int) -> bool:
        
        if val in self.hashMap : 
            
            storage_index = self.hashMap[val]  
            self.hashMap[ self.storage[-1]  ] = storage_index
            
            self.storage[storage_index] , self.storage[-1] = self.storage[-1] , self.storage[storage_index] 
            self.storage.pop() 
            del self.hashMap[val]
            
            return True 
        else : 
            return False                     

    def getRandom(self) -> int:
        
        
        val = self.storage[  randint(0 ,   len(self.storage)-1 )  ]
        return val 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()