
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1 : return strs[0] 

        sol = 0 

        for idx , char in enumerate(strs[0]) :  

            for i in range(1 , len(strs)): 

                if len(strs[i]) > idx and strs[i][idx] == char : pass 
                else : return strs[0][:sol]
            
            sol += 1 
        
        return strs[0][:sol]

        