class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 

        def alphanumeric(item): 

            # if "A" <= item <="Z" or "a" <= item <= "z" : 
            if "a" <= item <= "z" : 
                return True 
            elif "0" <= item <= "9" : 
                return True 
            else : 
                return False 
        
        left = 0 
        right = len(s) - 1

        while right > left : 

            while right > left and not alphanumeric(s[left]) :  
                left += 1 
            
            while right > left and not alphanumeric(s[right]): 
                right -= 1 
            
            if not right > left : return True 

            if s[left] == s[right] : 
                left += 1 
                right -= 1 
            else : 
                return False 
        
        return True