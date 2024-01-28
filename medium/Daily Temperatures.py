""" 
    思路 :  
        這一題的概念跟next greater element基本上就是一樣 , 
        在我看來就是要多保存index而已  ,
        因為這一題要求返回的是 NGE 距離本身的index距離為何 
"""


""" 
    解法一: 單調推疊+紀錄index
    
    element in the stack : ( temperature of ith day , index  )
    
"""
from typing import List 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        sol = [None for i in range(len(temperatures))] 
        stack = [] 
        
        for i in range(  len(temperatures) -1 , -1 ,-1 ): 
            
            while stack and stack[-1][0] <= temperatures[i] : 
                stack.pop() 
            
            sol[i] = ( stack[-1][1] - i ) if stack else 0 
            stack.append( (temperatures[i] , i)  )

        return sol 
            
            

        