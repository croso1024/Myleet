""" 
    Given an integer array nums ( with all distinct integer ) , and a value 'target' 
    return all possible combination that sum equal to target 

    p.s : (1,2) and (2,1) are different combination in the definition of this problem

    -> Backtrack algorithms 
    --------------------------------------------
    Use the general backtrack algorithms will lead time limit exceeded in this problem , 
    cause (1,1,1,2) == (1,1,2,1) == ( 1,2,1,1 )  == (2,1,1,1) 
    so i think we need to use the backtrack with starting index (rest array) ,
    and use the high-school permutation&combination formula to solve this problem . 

"""
# from math import factorial 
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
        
#         solution = 0
#         nums.sort() 
#         def permutationFormula(items:dict):  

#             temp = 0 
#             denumerator = 1 
#             for amount in items.values() : 
#                 temp += amount 
#                 denumerator *= factorial(amount) 
#             # print(seq ,  factorial(temp) // denumerator ) 
#             return  factorial(temp) // denumerator 


#         def backtrack( start_index ,  items: dict , acc ): 
#             nonlocal solution 
#             if acc > target : return  
#             elif acc == target : 
#                 solution += permutationFormula(items) 
#                 return 
            
#             # for i in range(start_index , len(nums)) : 
#             for i , num in enumerate( nums[start_index:] ) : 

#                 if acc + num <= target : 

#                     if num in items : 
#                         items[num] += 1 
#                     else : 
#                         items[num] = 1 

#                     backtrack( start_index + i  , items  ,    acc+num )
                    
#                     items[num] -= 1 

#                 else : 
#                     break 

#             return 
        
#         backtrack(0 , {} , 0)
        
#         return solution 

from typing import List 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()         
        # preceding zero 
        dp = [0 for i in range(target+1)]

        for i in range(target+1): 

            for num in nums  :
                if num > i : break  
                elif num == i : 
                    dp[i] += 1 
                else : 
                    dp[i] += dp[i-num]
                
        return dp[target]
