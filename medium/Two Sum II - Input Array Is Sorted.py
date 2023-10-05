from typing import List 

""" 
    思路 :
        這一題就是twoSum , 給了一個sorted array , 但同時要求constant complexity的版本 ,
        看起來就是左右雙指標擊殺 , 另外要注意這一題的index是從1開始算 , 就直接在return處+1
    
      
"""

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        # 題目給定了non-decreasing order的array -> 左右雙指標 
        left , right = 0 , len(numbers) - 1 
        
        # 題目說明不可以使用相同索引的元素
        while left < right : 
            
            sum = numbers[left] + numbers[right] 
            
            if sum == target : return [left+1 , right+1] 
            
            # sum大於target , 右邊要收縮來讓sum變小 
            elif sum > target : 
                right -= 1      
                
            else : 
                left += 1  
                
        
        return [-1,-1]