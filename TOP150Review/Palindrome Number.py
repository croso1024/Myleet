class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 : return False  

        # 透過 % 10取出所有數字到陣列 
        res = x 
        digits = []  

        while res != 0 : 
            
            digits.append(res%10) 
            res  = res// 10  
        
        left , right = 0 , len(digits)-1

        while right > left : 

            if digits[left] == digits[right] : 
                left += 1 
                right -= 1
            else : return False 
        
        return True