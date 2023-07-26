class Solution:
    def spiralOrder(self, matrix):
        """
            we pop every first row in the solution 
            then rotation the matrix by left 90 degree , do the same thing  
            until this matrix empty
            
            finally we flat the solution matrix to 1-d as solution 
        """
        
        
        sol = list() 
        while matrix: 

            tmp = (  matrix.pop(0) )  
            [ sol.append(i) for i in tmp ]            
            matrix = self.left_rotation(matrix)
        print(sol)                    
        return sol
    
    
    def transpose(self,matrix):
        return list(zip(*matrix))
    def left_rotation(self,matrix):  
        return self.transpose(matrix)[::-1]
        
import numpy as np 
S = Solution() 
a = np.random.randint(1,9,size=(9,1)).tolist() 
print(np.array(a))
S.spiralOrder(a)
    
            