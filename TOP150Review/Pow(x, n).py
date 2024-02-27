
""" 
    拆分 , 遞迴的求解下去
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = dict() 
        memo[0] = 1 
        memo[1] = x 
        # recursion是假設 n 為正的 pow function 
        def recursion( x , n) : 
            if n in memo : return memo[n]
            
            if n % 2 == 0 : 
                memo[n] = recursion( x  , n//2 ) *  recursion( x  , n//2 )
            else :
                memo[n] = x * recursion(x , (n-1)//2) * recursion(x , (n-1)//2)

            return memo[n]
        
        
        if n > 0 : 
            return recursion(x , n ) 
        else : 
            return 1/recursion(x , abs(n))

S = Solution() 
# print(S.myPow( 2 , pow(2,31) - 1 ))
print(S.myPow( 2 , pow(2,27)))

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # recursion是假設 n 為正的 pow function 
        def recursion( x , n) : 
            if n == 0 : return 1 
            elif n ==1 : return x             
            else :
                if n % 2 == 0 : 
                    temp = recursion( x  , n//2 ) 
                    return temp * temp 
                else :
                    temp = recursion(x , n-1) 
                    return x * temp 
        
        if n > 0 : 
            return recursion(x , n ) 
        else : 
            return 1/recursion(x , abs(n))
