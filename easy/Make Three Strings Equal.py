""" 
    Step.1 先尋找三個字串從左邊數來的共同部份 , 
    step.2 sol =  a - common_length + b - commen_length + c - commen_length

"""

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        # pick one element as standard 
        probe = 0
        size1 , size2 , size3 = len(s1) , len(s2) , len(s3) 
        min_size = min(size1,size2 , size3) 
        
        while probe < min_size and (s1[probe] == s2[probe] == s3[probe] ): 
            probe += 1 
        
        # probe代表共同長度 
        return  size1+size2+size3 - (3*probe) if probe !=0 else -1 