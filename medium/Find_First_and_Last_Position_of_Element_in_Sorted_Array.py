
# beat 99%  , 49% memory
class Solution:
    def searchRange(self, nums, target: int) :  

        size = len(nums) - 1 
        
        left_bound = 0 
        right_bound = size 
        
        while  left_bound <= right_bound: 
           
            pointer = int((left_bound+right_bound)/2 ) 
            #print(left_bound , right_bound,pointer , nums[pointer])
            if nums[pointer] > target : 

                right_bound = pointer if not right_bound == pointer else pointer -1 
                
            elif nums[pointer] < target: 
                
                left_bound = pointer if not left_bound == pointer else pointer+1 
                
            else : # nums[pointer] == target : 
                #print("find")
                return self.diffusion(nums,size,target,idx=pointer)
        return [-1,-1]

    def diffusion(self,nums,size,target,idx) : 
        
        solution = [idx,idx] 
        
        temp = idx 

        while temp - 1 >= 0 : 
            if nums[temp-1] == target : 
                temp = temp-1 
                solution[0] = temp 
            else : break 
        
        while temp+1 <= size : 
            if nums[temp+1] == target : 
                temp = temp+1 
                solution[1] =temp
            else : break 
        return solution         
        
        
        
        
        
        
        
        
        
        
test = [1,1,1,1,2,2,4,4,6,6,6,7,7,7,8,8,8,9,9,9,10,12,12]

#test = [1,2,8,8]
#test = [12,12]
#test =  [5,7,7,8,8,10,12]     
#test =  [5,7,7,8,8,10]
#test = [1,12,12,12,15]
#test = [2,2,5]      
#test = [1,1,3,4,6,7,7,7,8,9,10]
target =1

S = Solution() 
print(S.searchRange(test,target=target) )

