class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        
        dictionary = {} 
    
        for char in word : 
            
            if char not in dictionary.keys(): 
                dictionary[char] = 1 
             
            else: 
                dictionary[char] += 1
        
        temp = list(dictionary.values() )
     
        for idx in range(len(temp)): 
            
            temp2 = temp[:] 
            temp2[idx]  -= 1 
            if self.same_beside_zero(temp2): return True 
        
        return False 
            
    
    def same_beside_zero(self,seq): 
        
        seq = [i for i in seq if i] 
        return max(seq) == min(seq) 
         
            
test = "abbbccc"

S = Solution()
print(S.equalFrequency(test))