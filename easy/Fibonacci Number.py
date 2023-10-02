""" 
    簡單的Fibo題 ,實做一個保存前兩位數字的memo DP

"""

class Solution:
    
    def fib(self, n: int) -> int:
        if n == 0 or n == 1 : return 1 
        
        prev_2 , prev_1 = 1 , 1 
        
        for i in range(2 , n+1) : 
            