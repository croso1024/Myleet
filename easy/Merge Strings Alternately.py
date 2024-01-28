""" 
    思路: 
        沒啥好說的 , 雙指標 O(N)結束
"""

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        size1 = len(word1) 
        size2 = len(word2) 
        
        
        probe1 , probe2 = 0 , 0
        sol = ""
        
        while probe1 < size1 and probe2 < size2 : 
            
            sol = sol + word1[probe1] + word2[probe2]  
            probe1 += 1 
            probe2 += 1 
            
        
        # 走到這邊代表至少有一個probe是走到底了
        while probe1 < size1 : 
            sol = sol + word1[probe1] 
            probe1 += 1 
            
        while probe2 < size2 :
            sol = sol +word2[probe2]
            probe2 += 1 
        
        return sol