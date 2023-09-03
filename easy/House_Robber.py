class Solution:

    # Dynamic programming 
    """ 
    Given a  list of house ( Length = X ) , and the maximum robbable money 
    is Xk  ,  the money of number x house is xk
    ,  So the maximum robbable money of (X+1) house , is : 
    (X+1)k = max(  Xk  , (X-1)k + (x+1)k )
    
    
    """
    # Solution 1. DP with memory ( low speed , poor space )
    def robDP1(self, nums): 
        self.size = len(nums)
        
        
        if self.size == 1 : return nums[0] 
        elif self.size == 2 : return max(nums[0],nums[1]) 
        else : 
            self.MaxMoney_K = [0 for i in range(self.size)]
            self.MaxMoney_K[0]  = nums[0] 
            self.MaxMoney_K[1] = max(nums[0],nums[1])
        

            for i in range(2 , self.size): 
                self.MaxMoney_K[i] = max( self.MaxMoney_K[i-1] ,self.MaxMoney_K[i-2] + nums[i])
        
        return self.MaxMoney_K[-1]
    # Solution2. DP without memory (high speed , good space)
    def robDP2(self,nums): 
        if len(nums) == 1 : return nums[0]
        prev_one = max( nums[0] , nums[1] )
        prev_two = nums[0]

        for i in range(2,len(nums) ): 
            
            temp = prev_one 
            prev_one = max(temp , prev_two+nums[i] )  
            prev_two = temp 

        return prev_one
    # Solution 3. recursion ( brain storming )
    def robDP3(self,nums): 
        if len(nums) == 1 : return nums[0]
        elif len(nums) == 2 : return max(nums[0], nums[1])
        else : 
            return max(  self.robDP3(nums[:-1])  , self.robDP3(nums[:-2]) + nums[-1]         )
        
    
C = Solution() 
test_case = [104,209,137,52,158,67,213,86,141,110,151,127,238,147,169,138,240,185,246,225,147,203,83,83,131,227,54,78,165,180,214,151,111,161,233,147,124,143]
print(C.robDP3(test_case)) 