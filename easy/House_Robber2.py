class Solution:

    # Circle Version of House Robber, 
    # divide two part to solve circle list 
    #     A         A B C 
    #   B   C  -->    B C D
    #     D

    def rob(self, nums) :
        if len(nums) <= 3 : return max(nums) 
        else : 
            return max( self.subDP(nums[:-1]) , self.subDP(nums[1:]) )
    
    
    def subDP(self,nums): 
        if len(nums) <= 2 : return max(nums) 
        else : 
            prev_one = max(nums[0] , nums[1])
            prev_two = nums[0] 
            
            for i in range(2,len(nums)): 
                temp = prev_one 
                prev_one = max(temp , prev_two+nums[i])
                prev_two = temp 
            
            return prev_one 
            
C = Solution()
print(C.rob([2,3,2,5,5,1]))