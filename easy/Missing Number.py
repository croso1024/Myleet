
""" 
    思路 : 
        在新代被問的類似題 , 在follow-up的部份沒有答出來 , 即使用O(N)時間+O(1)空間 
"""

from typing import List 


""" 
    解法一. 先做sort , 然後從頭開始++ 
    
    速度較差 , 空間不錯
"""
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort() 
        
        probe = 0 
        size = len(nums) 
        
        while probe+1 < size : 
            
            if nums[probe]+1 == nums[probe+1] :
                probe += 1 
            else : 
                return nums[probe] + 1  
        
        
        return nums[0] -1 if nums[size-1] == size else nums[probe] + 1


""" 
    解法二 . 做hash set去存值 ,以及取得一個最小值和最大值 
"""

class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        
        hashset = set() 
        minimum = float("inf") 
        
        for item in nums :  
            hashset.add(item) 
            minimum =  min(minimum , item) 
        
        # 取得最小值 
        if minimum != 0 : return 0  
        
        while minimum+1 in hashset : 
            minimum += 1 
        
        return minimum + 1 


""" 
    解法三 . 
        follow-up的O(N)時間與O(1)空間 , maintain一個sum值去加總所有值 
        同時maintain最大與最小值 , 最後計算上底+下底成高除以2
"""

        
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        
        sum = 0 
        minimum = nums[0]
        maximum = nums[0] 
        
        for item in nums : 
            sum += item 
            minimum = min(minimum, item) 
            maximum = max(maximum , item) 
            

        # 我原先的計畫是讓 上底+下底成高除以2 - 實際sum就有答案 , 
        # 但需要處理一些edge case ,即缺值在兩個極端的情況 , 這邊直接用條件分歧去做這件事

        if minimum != 0 : return 0 
        elif maximum != len(nums) : return len(nums)
        else : 
            return ((maximum+minimum)*(len(nums)+1) // 2 ) - sum
    

S = Solution() 
S.missingNumber([3,0,1])
        