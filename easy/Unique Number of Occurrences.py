""" 
    思路 :  
    
        統計每一個digits 在array中出現的次數都是unique , 
        digits的種類數 -> hashmap的key數量 , hashmap的value保存該數字出現次數 
        
        換句話說 hashmap.value放進hashset的size要等於key的數量

"""
from typing import List 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        
        hashmap = {} 
        
        for item in arr: 
            if item in hashmap: 
                hashmap[item] += 1 
            else : 
                hashmap[item] = 1 
        
        
        return len(hashmap.keys()) ==  len({ v for v in hashmap.values() })