""" 
    思路 :
        給定兩個字串 , ransomNote和magazine 
        求ransomNote的字串能不能從magazine中被拼湊出來 , 所有字都不能重複使用 
        
        -> 這一題思路也很直觀, maintain兩個hashmap紀錄出現的字母和次數 
        
        magazine要能夠完成建構 , 必須所有字母都有 , 且數量>= ransomNote中的數量
"""

""" 
    解法一. 就是按照上述的思路 , 兩個dict做traverse 
    總共走三次O(N) , 空間也是O(N)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        src_map = dict() 
        dst_map = dict() 
        
        for char in ransomNote : 
            
            if char in dst_map : 
                dst_map[char] += 1 
            else : 
                dst_map[char] = 1 
                
        for char in magazine : 
            
            if char in src_map : 
                src_map[char] += 1 
            else : 
                src_map[char] = 1 
                
        # 檢查是否能夠完成建構 
        
        for word , freq in dst_map.items() : 
            
            if (not word in src_map) or ( freq > src_map[word] ) : return False 
        
        return True 
            