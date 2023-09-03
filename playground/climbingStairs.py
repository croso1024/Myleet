class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 : return 1 
        elif n == 2 : return 2 
        dp_table = [None] * (n+1)  
        dp_table[1] = 1 
        dp_table[2] = 2 
        
        if n <= 2 : return dp_table[n] 
        
        for n in range(3,n+1): 
            dp_table[n]  = dp_table[n-1] + dp_table[n-2] 
        return dp_table[n]
    

S = Solution()
print(S.climbStairs(5))