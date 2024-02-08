""" 
    題意 :
        給定一個字串 , 要我們依照該字出現的次數進行sorted 
    
    思路 :
        建立一個hashmap用來紀錄各個字元的出現次數 ,
        接著有兩種作法:
        
        1. 對原始s做sorted , key = hashmap[char]  -> O(NlogN)
            實做後有問題: 直接對原始s做sorted , 這會造成如果有兩個char出現次數一樣 , 那在sorted的結果中可能會交錯排列
            
        2. 直接對hashmap value做sorted , 接著重建回一個字串 -> O(26log26) + O(N)
"""

""" 
    解法一. 
        hashMap value做sort進行字串重建
        速度與空間都很不錯
        
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        
        hashMap = dict() 
        
        for char in s : 
            if char in hashMap : 
                hashMap[char] += 1 
            else :
                hashMap[char] = 1 
        
        sol = ""
        for key in sorted(  hashMap.keys() ,key =  lambda key : hashMap[key] , reverse=True) : 
            
            sol += key * hashMap[key] 
        
        return sol 
            