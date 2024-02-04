""" 
    題意 : 
        設計一個class , 在初始化的時候給定一個nums array , 並且支援一個sumRange的界面
        用來計算在nums中 , index left到right的sum , 注意是inclusive sum (nums[left] + nums[left+1] .. + nums[right])
        
    思路 :

        prefix sum秒殺  , 在初始化的時候需要O(N)計算
        在後續call sumRange都是O(1)
        
"""
from typing import List 
class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums  

        self.prefix = [None for i in range(len(nums))]

        prefix = 0 
        
        for i,num in enumerate(nums) : 
            
            prefix += num 
            
            self.prefix[i] = prefix
        
        # self.prefix[i] 代表 nums從 0加到i的結果

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0 : 
            return self.prefix[right] 
        
        else : 
            return self.prefix[right] - self.prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)