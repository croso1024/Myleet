class Solution:
    def canJump(self,nums): 
        canReach = 0 
        for idx,step in enumerate(nums): 
            if canReach >= idx :
                canReach = max((step+idx) , canReach) 
            else : break
        return True if canReach >= (len(nums)-1) else False 