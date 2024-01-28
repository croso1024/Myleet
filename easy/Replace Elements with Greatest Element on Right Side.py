
""" 
    思路 :  
        把Array中所有元素替換成其右邊最大的值
        走O(N) ,keep最大值所以空間O(1)
"""

from typing import List 
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        size = len(arr)
        max_ref = -1
        
        for i in range( size-1 , -1 , -1):  
            
            temp = max_ref 
            max_ref = max( arr[i] , max_ref  )
            arr[i] = temp 
        
        return arr             
            
        
        