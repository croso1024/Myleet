
""" 
    思路 :  
        這一題要我們去找到array中找到一組indexs , 
        滿足 index間距 > indexDifference  &  value差距 > valueDifference 
        這道題的easy版本可以直接雙迴圈搞定 , 因為array size很小 ,
        medium版本則是將array size擴大到 10^5 , 因此O(N^2)會超時 
        
        
        大致上看到題目的思路是建立一個array , 用來保存array在特定範圍內的極值所在的index 
        由後往前建立 ,  array[i] 代表 nums[i:]的範圍內 , 最大值與最小值出現的index , 
        也自然在 i~len(nums)-1的範圍, 這樣我們就可以走一次O(N)的時間 , 因為index必然滿足條件, 
        我們只要看array中對應位置的極值是否有滿足valueDifference
       
       O(N)
"""

from typing import List 

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        # create reference array 
        array = [None] * len(nums) 
        
        probe = len(nums) - 1 
        biggest_index = None 
        smallest_index = None 
        
        # O(N) 建立一個參考array         
        # array[i] 代表 nums[i:]的範圍內 , 最大值與最小值出現的index , 也自然在 i~len(nums)-1的範圍
        while probe >= 0 : 
            biggest_index = probe if (biggest_index == None or nums[probe] > nums[biggest_index]) else biggest_index
            smallest_index = probe if (smallest_index == None or nums[probe]<nums[smallest_index]) else smallest_index
            array[probe] = (biggest_index , smallest_index) 
            probe -= 1 
            
        
        # 走O(N)時間 , 當我們走到index = i , 就看 array[i+indexDifference] , 
        # 他對應的index必然是滿足index條件 , 直接看他內部的極值是否滿足valueDifference就好 
        
        for i in range( len(nums) - indexDifference ): 
            
            if abs(nums[ array[i+indexDifference][0]] - nums[i]) >= valueDifference :
                return [i ,  array[i+indexDifference][0]  ]
            
            elif abs(nums[ array[i+indexDifference][1]] -nums[i] ) >= valueDifference : 
                return [i , array[i+indexDifference][1]   ]
        
        
        return [-1,-1] 
            
            
            
            