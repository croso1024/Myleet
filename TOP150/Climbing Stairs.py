
class Solution:

    def climbStairs(self, n: int) -> int:


        memo = dict() 
        
        def dp(n): 
            
            if n == 1 : return 1 
            elif n == 2 : return 2  
            elif n in memo : return memo[n] 
            else : 
                sol = dp(n-1) + dp(n-2) 
                memo[n] = sol 
                return sol 
        
        return dp(n)    
    

class Solution:

    def climbStairs(self, n: int) -> int:
        
        temp = [1,2]
        
        if n == 1 : return temp[0]
        elif n==2: return temp[1] 
        else : 
            
            for i in range(3 , n+1):  
                sol = temp[0] + temp[1] 
                temp = [temp[1] , sol] 
        
        return sol  
            