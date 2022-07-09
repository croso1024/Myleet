import time
class Solution(object):
    
    """first edition , can pass ,but pool runtime
    """
    # def removeElement(self, nums, val):
    #     index = 0  
    #     find = 0 
    #     for i in range(len(nums)) : 
    #         if nums[index] == val : 
    #             nums.pop(index) 
    #             nums.append("_")  
    #             find+=1 
    #         else:  
    #             index += 1 
    #     #print(nums)
    #     return   len(nums) - find           
# s = Solution()
# t1 = time.time()
# k = s.removeElement([0,1,2,2,3,0,4,2],val = 2 )
# print(time.time()-t1)
# print(k)

    """ second edition more speed and more save memory
    """

    def removeElement(self,nums,val):
        find = 0 
        l = len(nums)
        for i in range(l) : 
            #print(nums,"step",i,"index",l-1-i)
            if nums[l-1-i] == val : 
                nums.pop(l-1-i) 
                nums.append("_")  
                find+=1 
            else:  
                pass
        #print(nums)
        return   l - find     
s = Solution()
t1 = time.time()
#k = s.removeElement([0,1,2,2,3,0,4,2],val = 2 )
#k = s.removeElement([3,2,2,3],val = 3 )
k = s.removeElement([],val = 3 )
print(time.time()-t1)