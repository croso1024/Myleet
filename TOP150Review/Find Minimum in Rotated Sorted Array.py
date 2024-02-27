class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left , right  = 0 , len(nums) - 1 

        ans = nums[0] 

        if nums[left] < nums[right] : return nums[left]

        while left <= right : 

            if nums[left] < nums[right] : return nums[left] 

            mid = left + (right-left) // 2 

            ans = min(ans , nums[mid])  

            if nums[mid] >= nums[left] : 
                left = mid  + 1 

            elif nums[mid] < nums[right]: 
                right = mid - 1

        return ans

class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left , right  = 0 , len(nums) - 1 
        sol = nums[0]
        while left <= right  : 

            mid = left +  (right-left) // 2 

            mid_element = nums[mid]  
            sol = min(sol , mid_element)

            # mid_element 最高,那就搜索  mid 到 right 
            if mid_element >= nums[left] and mid_element > nums[right] : 
                left = mid + 1 
            
            elif mid_element < nums[left] and mid_element <= nums[right] : 
                right = mid - 1 

            else : 
                right = mid - 1 

        # 往左邊逼近的binary search , 
        return min( nums[left] , sol )  