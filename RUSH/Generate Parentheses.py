from typing import List 

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        solution = list()
        
        def backtrack(useLeft , useRight , track):
            
            if (useLeft < useRight):return 
            
            elif (useLeft == n and useRight == n ): 
                solution.append(track)
                return 
            
            elif ( useLeft == n):
                backtrack( useLeft , useRight+1 , track+")") 
            else : 
                backtrack(useLeft+1 , useRight , track+"(")
                backtrack(useLeft , useRight+1 , track+ ")")  
        
        backtrack( 0 , 0 , "" )
        return solution                  