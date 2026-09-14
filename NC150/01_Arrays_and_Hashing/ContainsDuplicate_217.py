"""
題意 : 給定 Array , 若內部有兩個相同Element就回True, 

思路 : 直覺使用Hash ,紀錄已經看過的, 這樣時間複雜度O(N) , 但空間也O(N) , 
如果要降空間 , 可能得要做Sorted + 雙指標走. 

複雜度 : Time O(?) / Space O(?)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen : set = set() 

        for element in nums : 

            if element in seen : 
                return True  
            else : 
                seen.add(element) 

        return False  


# ===  空間O(1) 
class Solution :
    def containsDuplicate(self,nums:List[int]) -> bool : 

        nums.sort() 
        size = len(nums) 

        if size == 1 : 
            return False 
        
        i = 0 
        while i+1 < size : 
            if nums[i] == nums[i+1] : 
                return True 
            i += 1 
        
        return False 
        
        

