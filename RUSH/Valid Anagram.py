
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        hashMap = dict()
        
        for char in s : 
            if char in hashMap:
                hashMap[char] += 1 
            else : 
                hashMap[char] = 1 
        
        for char in t : 
            
            if not char in hashMap : return False 
            if hashMap[char] == 1 :del hashMap[char]
            else : hashMap[char] -= 1 
        
        if not hashMap: return True 
        else : return False 
        
        
