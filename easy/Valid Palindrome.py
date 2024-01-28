
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0 
        right = len(s) - 1 
        
        
        while left < right :  
            
            # 走到left指向ascii
            while left < right and (not ("A" <= s[left] <= "z") or not ( "0"   )): 
                left += 1  
            
            while left < right and  not ("A" <= s[right] <= "z"):
                right -= 1 
            
            # print(f"Compare {s[left]} {s[right]}")
            
            if left != right : 
                if s[left].lower() == s[right].lower() : pass 
                else : 
                    return False 
                left += 1 
                right -= 1

        return True             

test = "A man, a plan, a canal: Panama" 
S = Solution() 
S.isPalindrome(test) 