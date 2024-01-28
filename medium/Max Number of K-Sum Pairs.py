""" 
    思路:
        此題給定一組array , 以及目標數字k , 
        在每一次操作 , 我們都可以從array中挑選兩個數字總和為k的移除  , 
        求最大可以移除的次數     

        這一題最直接的思路是sorting後左右雙指標 ,    
        
        雙指標和為k時 , sol += 1並且同時縮進指標 ,
        若和>k , 縮右指標 , 反之縮左標
        
    
"""
from typing import List 

""" 
    解法一. sorting + 雙指標 , 速度與空間都很優
"""
class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort() 
        sol = 0 
        left  , right = 0 , len(nums)- 1 

        while left < right : 
            
            sum = nums[left] + nums[right] 
            
            if sum == k : 
                sol += 1 
                left += 1 
                right -= 1 
                
            elif sum > k : 
                right -=  1  
            else : 
                left += 1 
        
        return sol 