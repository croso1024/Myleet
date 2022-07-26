# class Solution:
    
#     def searchInsert(self, nums ,target): 
#         self.index = 0
#         self.target = target 
#         self.RecursionSearch(nums)

#         return self.index 


#     def RecursionSearch(self,nums):
#         print(nums , self.index)
#         if len(nums) == 1 : 
#             if self.target > nums[0]:
#                 self.index +=1 
#                 return
#             else : 
#                 return

#         else: 
#             half = len(nums)//2 
#             left,right = nums[:half]  , nums[half:]

#             if self.target > right[0]: 
#                 self.index +=  len(left) 
#                 self.RecursionSearch(right)  

#             elif self.target < right[0] :
#                 self.RecursionSearch(left)
            

#             else: 
#                 self.index += len(left)
            
# C = Solution() 
# print(C.searchInsert([-2,1,3,5,6,8,10],target=7))

## 加速版 ,把index當作recursion的參數傳下去取代修改物件屬性 
# faster than 31% memory usage less than 82% 
class Solution:
    
    def searchInsert(self, nums ,target): 
        self.target = target 
        return  self.RecursionSearch(nums,0)


    def RecursionSearch(self,nums,index):
        
        if len(nums) == 1 : 
            return index+1 if self.target>nums[0] else index 
      
        else: 
            left,right = nums[:len(nums)//2]  , nums[len(nums)//2:]

            if self.target > right[0]: 
              
                return self.RecursionSearch(right ,  index+len(left) )  

            elif self.target < right[0] :
                return self.RecursionSearch(left, index)
            
            else: 
                return index+ len(left)
              
            
C = Solution() 
print(C.searchInsert([-2,1,3,5,6,8,10],target=7))