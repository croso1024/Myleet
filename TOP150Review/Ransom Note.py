class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashmap1 = {} 
        hashmap2 = {}
        for char in ransomNote : 
            if char in hashmap1 : hashmap1[char] += 1 
            else : hashmap1[char] = 1 
        for char in magazine : 
            if char in hashmap2 : hashmap2[char] += 1 
            else : hashmap2[char] = 1
        
        for element in hashmap1.keys() :  

            if element in hashmap2 and  hashmap1[element] <= hashmap2[element] : pass 
            else : return False 

        return True 


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        element_table = {} 
        for char in magazine :  
            if char in element_table : element_table[char] += 1 
            else : element_table[char] = 1 
        
        for char in ransomNote : 

            if not char in element_table : return False 
            else : 
                element_table[char] -= 1  
                if element_table[char] < 0 : return False 

        return True 