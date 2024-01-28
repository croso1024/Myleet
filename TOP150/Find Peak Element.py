class Solution:

    # 往高處壓縮 
    def findPeakElement(self, nums: List[int]) -> int:
        
        left , right = 0 , len(nums) - 1 

        def isPeak(i) : 

            if i == 0 or nums[i] > nums[i-1] : pass 
            else : return False 

            if i == len(nums) - 1 or nums[i] > nums[i+1] : pass 
            else : return False 

            return True   

        while left <= right : 


            mid = left + (right-left ) // 2 

            # step.1 判斷是否為peak 
            if isPeak(mid) : return mid 

            # step.2 如果不是peak , 就看mid左邊右邊誰高 , 來決定限縮的搜索範圍
            if mid == 0 : 
                left = mid + 1 
            elif mid == len(nums) - 1 : 
                right = mid - 1 
            else : 

                if nums[mid-1] > nums[mid+1] : 
                    right = mid - 1 
                else :
                    left = mid + 1 
        
        return -1 