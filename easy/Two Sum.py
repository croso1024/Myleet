""" 
    這一題是在書本的左右雙指標中提到 , 不過這一題也是有名利用hash-table來解
    ,這裡就各解一次 
"""


""" 
    解法一 . Hash table , 時間O(n) , 空間O(n)
"""
from typing import List 

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #  一個table保存數值以及對應index 
        table = { num : idx for idx,num in enumerate(nums)  } 
        
        for idx  ,num  in enumerate(nums)  : 

            # 尋找table中有沒有可以和num搭配得到target,但又不是自身的
            if target - num in table  and  not table[target - num] == idx     : 
                return [ idx , table[target-num] ] 
              

        return [-1,-1]
    
    
""" 
    解法二 . 雙指標 時間O(n log n) , 空間O(1) ( 如果nums是sorted , 否則還是O(n) )
    
    需要先進行sort , 在給定的nums list為排序完成的情況下 
    透過將target與兩個指標所對應到的數值和做比較 , 一旦總和小於target , 將左指標右移  
    
"""

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index_list 會去 map到原始nums中的index值
        index_list = sorted([i for i in range(len(nums))] , key=lambda idx :nums[idx]   )
        nums.sort() 
        left , right = 0 , len(nums) - 1 
        
        while left <= right : 

            sum = nums[left] + nums[right]
            
            if sum == target : return  [  index_list[left] , index_list[right]]
            elif sum > target : right -= 1 
            else : left += 1 
            
        
        return [-1,-1]
                
            
            
            
            