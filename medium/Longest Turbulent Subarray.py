""" 
    思路 :  
        這題在思路上可以想到用2D-DP table或是兩個1D DP-table 
        
        兩個1D table可能就是 
        dp1[i] : 以i為結尾 , i為大
        dp2[i] : 以i為結尾 , i為小 
        
        如此一來
        dp1[i] = dp2[i-1] + 1 if nums[i] > nums[i-1] else 1 
        dp2[i] = dp1[i-1] +1  if nums[i] < nums[i-1] else 1 
        
"""
from typing import List 

""" 
    解法一. 就是雙1D table , 釐清兩種狀態之間的關係即可

"""

class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        dp1 = [None for i in range(len(arr))]    
        dp2=  [None for i in range(len(arr))] 
        
        
        dp1[0] = 1 
        dp2[0] = 1 
        
        # 推進狀態
        for i in range(1 , len(arr)): 
            
            if arr[i] > arr[i-1] : 

                dp1[i] = dp2[i-1] + 1  
                dp2[i] = 1  

            elif arr[i] < arr[i-1]: 

                dp1[i] = 1 
                dp2[i] = dp1[i-1] +1 

            else : 
                
                dp1[i] = 1 
                dp2[i] = 1 
        return max(  max(dp1) , max(dp2))

test = [9,4,2,10,7,8,8,1,9]
S = Solution() 
S.maxTurbulenceSize(test) 