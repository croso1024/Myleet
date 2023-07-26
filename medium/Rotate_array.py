class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0 or len(nums) <= 1 : return 
        else : 
            k = k % len(nums) 
            for i in range(k): 
                nums.insert(0,nums.pop())

    def rotate2(self,nums :list,k): 

        def reverse(left,right): 
            while left < right : 
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1 
                right -= 1 
                
        if k==0 or len(nums) <= 1 : return 
        else : 
            k = k % len(nums) 
            # reverse first part :
            reverse(0 , len(nums)-k-1 )
            reverse(len(nums)-k , len(nums)-1)  
            # reverse second part : 
            # reverse all of the list 
            nums.reverse()             


S = Solution() 
#test = [1,2,3,4,5,6,7]
test = [5,2]
S.rotate2(test,k=1 )
print(test)