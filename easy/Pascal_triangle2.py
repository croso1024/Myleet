class Solution:
    def getRow(self, rowIndex: int): 
        # Compute the DP table , output the specific row 
        self.result = [1]
        
        for i in range(1 , rowIndex+1): 
            
            result =  [1] * (i+1)
            
            for j in range(1 , i): 
                
                result[j] = self.result[j-1] + self.result[j]
            
            
            self.result = result 
        
        print(self.result) 
        return self.result 

C = Solution() 
C.getRow(5) 
            
        
        
        