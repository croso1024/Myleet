class Solution:
    def removeDuplicates(self, nums ) : 
        self.probe = None 
        self.k = 0
                
        for index in range(len(nums)): 
            if not self.probe == nums[index - self.k ]: 
                self.probe = nums[index - self.k ]
            else: 
                nums.pop(index - self.k ) 
                nums.append("_")
                self.k += 1 
                
        return len(nums) - self.k 

S = Solution()
number = [0,0,1,1,1,2,2,3,3,4]
print(S.removeDuplicates(nums=number))
print(number)
        