""" 
    思路 :  
        最naive的解法就是雙迴圈 
        外層走left -> right 
        內層針對每一個digits走一次digits-wise的檢查

"""
from typing import List 

class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    
        sol = []
        
        for number in range(left , right+1 ) : 
            
            valid = True  
            
            for digit in str(number): 
                
                if digit != "0" and number % int(digit) == 0: continue 
                valid = False                 
                break 
            
            if valid: sol.append(number) 
        
        return sol 
        
        