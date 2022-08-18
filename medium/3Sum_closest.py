class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort() 
        self.nums = nums
        self.size = len(self.nums) - 1 
        self.target = target 
        self.bestSolution  = None
        
        self.error = float("inf")
        for index in range( self.size ) :  
            
            
            self.recursionFind(index,index+1,self.size)
            
       
        return self.bestSolution

    def recursionFind(self, current_index ,l_index ,r_index ) : 
        
        
        if l_index == r_index : return 
        else: 
 
            temp_error =   self.target - (self.nums[current_index]+ self.nums[l_index] + self.nums[r_index ])  
        
            
            if abs(temp_error) <= self.error :

                self.error = abs(temp_error)
                #self.bestSolution = (current_index,l_index,r_index)
                self.bestSolution = self.nums[current_index] + self.nums[l_index] + self.nums[r_index ]
                
            if temp_error > 0 : self.recursionFind(current_index,l_index+1,r_index )
            elif temp_error <0 : self.recursionFind(current_index,l_index , r_index-1 ) 
            
    
            

####### Testing ########33
nums = [-2,0,3]
target = 1
SSS = Solution()
sol =   SSS.threeSumClosest(nums,target) 
print(sol)