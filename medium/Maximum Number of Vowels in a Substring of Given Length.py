""" 
    思路 :  
        此題給定一個字串s 和int k , 要找到在長度最多為k的sub-string中
        最多有幾個母音 a,e,i,o,u 出現


    # 解法上直觀可以想到sliding window的solution , 去maintain window中的母音數量
    # 使用一個數值去存window內的母音數量即可 
    
    時間O(N) , 空間O(1) 
"""


class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:

        #母音集合
        vowels = {"a","e","i","o","u"}
        # 紀錄最佳解 
        sol = 0 
        
        # 紀錄window內的母音數量 
        window = 0 
        
        left , right = 0 , 0 
        
        
        while right < len(s) :  
            
            if s[right] in vowels : window += 1    

            right += 1 
            
            while (right-left) > k  and left < right : 
                
                if s[left] in vowels : window -= 1 

                left += 1 
        
            # 更新目前的解
            sol = max(sol , window) 
        
        return sol 
        
        
            
            