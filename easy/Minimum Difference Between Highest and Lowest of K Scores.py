from typing import List 
""" 
    給定一組Array 與常數k , 我們必須從array中選出k個值,使得選出的最大值與最小值差距最小 
    換句話說答案就是在"前k大的值" 或著 "前k小的值"  這兩個範圍的極值差 
    
    第一個直覺作法就是sorted , 以k作為window size掃略一次
    
    
    
"""


""" 
    解法一. 
        第一個直覺作法就是sorted , 以k作為window size掃略一次
        速度居然能到100% , 反而空間不佳 , 但我這已經是in-place solution了

"""

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort() 
        size = len(nums)
        
        best = float("inf")
        for i in range(  size-k+1  ): 
            
            if nums[i+k-1] - nums[i] < best : 
                best = nums[i+k-1] - nums[i] 
            
        return best 