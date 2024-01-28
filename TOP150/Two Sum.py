from typing import List 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # key為nums的值 , 用來做查詢 , value則是保存他的索引位置
        hashmap = { nums[i]:i for i in range(len(nums))  }

        for idx , num in enumerate(nums) : 
            
            if target - num in hashmap  and not hashmap[target-num] == idx : 
                return idx , hashmap[target-num]
        
        return [-1,-1]        
            

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ref_table = list(range(len(nums)))
        ref_table.sort(key = lambda x : nums[x])
        nums.sort()

        left = 0 
        right = len(nums) - 1 
        
        while right > left : 
            
            sum = nums[left] + nums[right] 
            
            if sum == target : return [  ref_table[left] , ref_table[right] ]
            elif sum > target : 
                right -= 1 
            else : 
                left += 1 
                
        
        return [-1,-1]