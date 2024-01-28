""" 
    思路 :  
        這一題與easy版本的Next greater element 差別在於array是環形的 , 
        最後一個元素與第一個元素是相鄰的 , 因此再找next greater element變為從右邊開始一路找到該元素左方 ,
        找到的第一個最大值就是該元素對應的next greater element . 

        先做了一個暴力的O(N^2)硬解 , 但我認為過不了測資 
        稍微思考一下解法 , 嘗試將原始array複製一份貼在後方 , 即 [a,b,c,d,e] -> [a,b,c,d,e,a,b,c,d,e] 
        
        假設找c元素的NGE , 他會從 d->e->a->b->c->d->e的順序開始看  , 即先看右側,再看左側 , 之後會有冗於的再看右側 , 但Total是O(N)
        因此我們針對這個兩倍大小的array 做單調堆疊 , 只不過只有當index在 0 ~ len(nums)-1 的範圍我們才開始將答案append入
        
        
"""



""" 
    解法一. 暴力解 O(N^2) , 感覺應該是過不了測資
"""
from typing import List 
class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        sol = [] 
        for index , element in enumerate(nums) : 
            # 尋找右側 
            find = False 
            for i in range( index+1 , len(nums)): 
                
                if nums[i] > element : 
                    sol.append(nums[i]) 
                    find = True 
                    break 
            
            if find : continue 
            # 如果還沒找到 , 要找左側 
            for i in range(index): 
                if nums[i] > element : 
                    sol.append(nums[i]) 
                    find = True  
            
            if find == False : 
                sol.append(-1)
            
        return sol      
                
        
""" 
    解法二 :  將array複製一份 , 做單調堆疊 
"""

class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        expand_array = nums + nums 
        sol = [None for i in range( len(nums) )]
        stack = [] 
        
        for index in range(len(expand_array)-1 , -1 ,-1): 

            while stack and stack[-1] <= expand_array[index]:  
                stack.pop() 
            
            if index < len(nums) :            
                sol[index]  =  stack[-1] if stack else -1 
            
            stack.append(expand_array[index]) 
        
        return sol 
                
            
            
            
        
        