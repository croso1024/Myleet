from typing import List 

class Solution:

    # naive solution : sort then calculate , take
    def longestConsecutive(self, nums: List[int]) -> int:

        ref = sorted(nums) 
        print(ref)
        best = 0  
        
        counter = 0 
        
        while  counter < len(nums) : 
            
            temp = 1
            
            while counter < len(nums) -1 : 
                if  ref[counter] + 1  ==  ref[counter+1] :  
                    temp += 1 
                    counter += 1 
                elif ref[counter] == ref[counter+1] : 
                    counter += 1 
                else : 
                    break 

            best = max(best , temp) 
            counter += 1 
        
        return best 



class Solution:

    # O(N) time complexity solution 
    # use hashmap store all element , then perform diffusion search 
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # key : number , value : visited!?
        table  = {  i:False for i in nums  } 
        best = 0
        
        for i in nums : 
            # 如果table[i] 是還沒有探索過的
            if not table[i] :  
                table[i] = True 
                temp = 1 
                
                # 開始往左側與右側去探索 
                left_probe = 1 
                right_probe = 1 
                while i-left_probe in table : 
                    table[i-left_probe] = True 
                    temp += 1 
                    left_probe += 1 
                while i+right_probe in table : 
                    table[i+right_probe] = True 
                    temp += 1 
                    right_probe += 1 
                
                best = max(best , temp)  

        return best 
             
            
        
test = [1,2,0,1]
S = Solution() 
print(S.longestConsecutive(test))