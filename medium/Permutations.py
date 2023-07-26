# time complexity beats 86 %  , space beats 84%


class Solution:

    def permute(self, nums): 

        self.solution = list() 
        
        if len(nums) == 1 : return [nums] 
        else : self.recursion([],nums)

        return self.solution
    def recursion(self,temp,seq): 
    
        
        if len(seq) > 2: 
            
            for idx , item in enumerate(seq) : 
                self.recursion(temp+[item] , seq[:idx]+seq[idx+1:] ) 
            
            
        else: 
            self.solution.append(temp+[seq[0],seq[1]])
            self.solution.append(temp+[seq[1],seq[0]])
            
            return 
            
            
S = Solution() 
print(S.permute([0,1,2,3,4,6]))