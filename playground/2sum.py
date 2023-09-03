from typing import List 

class Solution:
    # two probe approach
    # def twoSum(self, nums: List[int], target: int) -> List[int]:

    #     sorted_nums = sorted(nums) 
    #     left_probe , right_probe = 0 , len(nums) - 1 
        
    #     while left_probe <= right_probe : 
            
    #         probe_sum = sorted_nums[left_probe] + sorted_nums[right_probe]
            
    #         if probe_sum == target : 
    #             return [nums.index( sorted_nums[left_probe] , 0 ) , len(nums)-1-(nums[::-1].index(sorted_nums[right_probe])) ]
    #         elif probe_sum > target : 
    #             right_probe -= 1 
    #         else : 
    #             left_probe += 1 
        
    # hash table 
    
    def twoSum(self, nums , target): 
        # create hash table        
        table = { num:index for index,num in enumerate(nums) } 
        # traversal all element in nums
        for index , num in enumerate(nums) : 
            if ( target - num ) in table and  table[target-num] != index : 
                return  [ index , table[target-num] ]
            
            
    
          
            

S = Solution()
test_case = [3,3] 
target = 6

print(S.twoSum(test_case , target=target))