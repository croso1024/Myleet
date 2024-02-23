# class Solution:
#     def integerReplacement(self, n: int) -> int:
        
#         solution = float("inf")
#         # memo = dict() 
#         def recursion(x , steps):
#             nonlocal solution
#             if x == 1 : 
#                 solution = min(solution , steps) 
            
#             elif x % 2 == 0 : 
#                 recursion( x//2 , steps+1 )  
            
#             else : 
#                 recursion( x+1 , steps+1 )
#                 recursion( x-1 , steps+1 )
        
#         recursion(n , 0)

#         return solution
class Solution:
    def integerReplacement(self, n: int) -> int:
        
        solution = float("inf")
        memo = dict() 
        def recursion(x):
            nonlocal solution
            if x == 1 : return 0 
                
            elif x in memo : 
                return memo[x] 
            
            elif x % 2 == 0:
                step = recursion(x//2)+1
            else : 
                step = 1 + min(recursion(x+1) , recursion(x-1)) 
            
            memo[x] = step 
            return step 

        return recursion(n)