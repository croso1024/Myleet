
# sliding windows solution 
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用window去keep track在範圍內不重複的字 
        window = set()    
        sol = 0 
        left = 0 
        right = 0 
        size = len(s) 
        
        # 開放區間的 sliding window [left , right)
        while right < size : 
            
            # 將新的字加入區間 , 這邊在insert的時候就要檢查有沒有元素重複
            add_char = s[right]   

            #如果有元素已經在window內 , 移動left指標 , 直到add_char不在window內部 
            if add_char in window :
                
                while left < right and  add_char in window :
                    window.remove( s[left] ) 
                    left += 1

            window.add(add_char)  
            right += 1 
            
            sol = max(sol , right-left)
        
        
        return sol 
            

            