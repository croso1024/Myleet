from typing import List 


# dp solution 

# class Solution:

#     def minimumTotal(self, triangle: List[List[int]]) -> int:

#         dp = [  [ None for i in range(j) ]  for j in range( 1, len(triangle) + 1)    ]
#         dp[0][0] = triangle[0][0]
        
#         for i in range(1 , len(triangle)):
            
#             for j in range( len(triangle[i]) ):
                
#                 if j == 0 : 
#                     dp[i][j] = dp[i-1][j] + triangle[i][j] 
#                 elif j == len(triangle[i]) - 1 : 
#                     dp[i][j] = dp[i-1][j-1] + triangle[i][j] 
#                 else : 
#                     dp[i][j] = triangle[i][j] + min(dp[i-1][j-1] , dp[i-1][j]) 
        
#         return min(dp[len(triangle)-1])                

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        prev = [triangle[0][0]]
        for i in range(1 , len(triangle)):
            
            temp = [None for i in range(len(triangle[i]))]
            
            for j in range( len(triangle[i]) ):
                
                if j == 0 : 
                    
                    temp[j] = prev[j] + triangle[i][j]
                
                elif j == len(triangle[i]) -1 : 
                    
                    temp[j] = prev[j-1] + triangle[i][j] 
                
                else : 
                    temp[j] = min(prev[j] , prev[j-1] ) + triangle[i][j] 
        
            prev = temp 
            
        return min(prev)
    
    
     
S = Solution() 
print(S.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
# print(S.minimumTotal([[-10]]))