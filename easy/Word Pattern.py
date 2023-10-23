""" 
    思路 :
        hashmap去儲存patter對應的值做對照即可 

"""

""" 
    解法一 . hashmap + hashset來處理 
    看了一下其實hashset也不是非得要在主要loop中添加 , 可以在最後透過 len(set(list(hashmap.value())))
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # 如果patter的長度和s.split()後不同直接false 
        split = s.split(" ")
        if not len(pattern) == len(split) : return False 

    
        hashmap = dict() 
        # hash set的目的要確保所有key到值都是一對一 , 沒有多個key映射到同個value的情況
        hashset = set() 

        for i in range(len(pattern)) : 
            
            # 從patter取出符號 , 檢查是否在hash-map 
            # 不在 -> 將符號作為key , 對應的字串元素作為值存入hash-map
            # 在 -> 確認該符號應該要對應到什麼值 , 確認s確實就是該值 , 否則return False 
            key = pattern[i]  
            if key in hashmap : 
                if  not  hashmap[key] == split[i]  : return False 
            else : 
                hashmap[key] = split[i]
                hashset.add(split[i]) 
            
        if len(hashmap.keys()) == len(hashset) : return True 
        else : return False 


""" 
    解法二 . 優化了一下hashset的使用
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # 如果patter的長度和s.split()後不同直接false 
        split = s.split(" ")
        if not len(pattern) == len(split) : return False 

    
        hashmap = dict() 

        for i in range(len(pattern)) : 
            
            # 從patter取出符號 , 檢查是否在hash-map 
            # 不在 -> 將符號作為key , 對應的字串元素作為值存入hash-map
            # 在 -> 確認該符號應該要對應到什麼值 , 確認s確實就是該值 , 否則return False 
            key = pattern[i]  
            if key in hashmap : 
                if  not  hashmap[key] == split[i]  : return False 
            else : 
                hashmap[key] = split[i]
            
        if len(hashmap.keys()) == len(set(list(hashmap.values()))) : return True 
        else : return False 
        