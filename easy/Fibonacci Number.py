""" 
    簡單的Fibo題 ,實做一個保存前兩位數字的memo DP

"""

class Solution:
    
    def fib(self, n: int) -> int:
        
        if n in [0 ,1]  : return n
        
        prev_2 , prev_1 = 0 , 1 
        
        for i in range(2 , n+1) : 
            
            solution = prev_2 + prev_1 
            prev_2 , prev_1 = prev_1 , solution  
        
        return solution 