from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = [] 
        # travasal all element , use twoSum 
        for index,number in enumerate(nums) : 
            find_result = self.twoSum( nums, number , index)
            if find_result :  
                temp = sorted([number] + find_result) 
                if not temp in result : result.append(temp)
            else : 
                pass 
    
        return result
    
    
    def twoSum(self,sorted_array,target,outside_index): 
        
        left_probe , right_probe = 0 , len(sorted_array) - 1 
        
        while left_probe < right_probe : 

            probe_sum = sorted_array[left_probe] + sorted_array[right_probe]
            
            if probe_sum + target == 0 :
                if left_probe == outside_index : left_probe+= 1 
                elif right_probe == outside_index : right_probe -=1 
                else : return [sorted_array[left_probe] , sorted_array[right_probe]] 
                
            elif probe_sum + target > 0  : 
                right_probe -= 1 
            else : 
                left_probe += 1 
        
        return False
            
            
S = Solution() 
test_case =  [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(S.threeSum(test_case))
            
            
    

    
        
        
            
            