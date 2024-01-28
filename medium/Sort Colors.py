""" 
    思路 : 
        這一題要求做inplace sort , array大小只有到三百 , 所以我感覺可以直接做
        selection sort

"""

""" 
    解法一. selection sort inplace
"""

from typing import List 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):  
            
            temp_idx = 0 

            for j in range(len(nums)-i) : 
        
                if nums[j] > nums[temp_idx] :temp_idx = j 
            
            # 做swap , j 一定不會到最後一個元素 
            nums[temp_idx] , nums[len(nums)-i-1] = nums[len(nums)-i-1]  , nums[temp_idx] 
        
        return nums
    
    
""" 
    解法二. merge sort  , 這個沒有in-place
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def mergeSort(array):  
            
            if (len(array)) < 2 : return array 
     
            left , right = 0 , len(array)-1

            mid = left + (right-left)//2 

            left_array = mergeSort(array[:mid+1])
            right_array = mergeSort(array[mid+1:])  
            
            # 做Merge 
            array = [None] * len(array) 
            left_probe , right_probe = 0 , 0 
            
            while left_probe < len(left_array) and right_probe < len(right_array) : 

                if left_array[left_probe] < right_array[right_probe] : 
                    array[left_probe+right_probe] = left_array[left_probe]
                    left_probe += 1 
                else : 
                    array[left_probe+right_probe] = right_array[right_probe]
                    right_probe+= 1 
            
            while left_probe < len(left_array) : 
                array[left_probe+right_probe] = left_array[left_probe] 
                left_probe+=1 
            while right_probe< len(right_array) : 
                array[left_probe+right_probe] = right_array[right_probe] 
                right_probe+=1 
                
            return array 

        return mergeSort(nums)



test = [2,0,2,1,1,0,0]
S = Solution()
print(S.sortColors(test))