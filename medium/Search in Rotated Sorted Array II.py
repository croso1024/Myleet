""" 
    題意:
        給定一個經過sorted的array (當中可能有duplicate element)  
        在將array送進我的function之前 , array會先經過一次rotation , 使得array變成 
        [array[k] , array[k+1] , ... , array[n-1] , array[0] , array[1] , ... , array[k-1] ]  
        給定一個目標整數 target , 尋找target是否存在於array中 
        
    思路:   
        我不曉得為何給定array的size只有5000 , 這樣或許直接linear search就有不錯的結果
        
        具體來說這一題的基本形是沒有duplicate的版本 , 這樣可以在binary search的時候透過mid , 
        left, right的相對值去找目前rotation的大致形狀 , 但因為這一題增加了duplicate , 有可能出現left,right指向相同值的情況

        我的思路是若left,right指向相同值 , 就left+=1或right-=1 .其餘仍按照原先的search in rotated sorted array I 
        基本上這一題最好畫圖出來思考會比較好,
        關鍵概念在於 "檢查 nums[left] - nums[mid]是否符合sorted , 若否 , 則nums[mid]->nums[right]必定是sorted "
        
    
"""

from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        
        left , right = 0 , len(nums) - 1 
        
        while left <= right : 
            
            mid = left + (right-left)//2 
            if nums[mid] == target : return True 
            
            # 處理duplicate 
            if nums[left] == nums[right] : 
                
                if nums[left] == target : return True 
                
                left += 1 
                continue 

            # 分幾種case , 要看 left , right  ,mid指標對應nums的相對值 

            # 正常情況
            if nums[left] <= nums[mid] : 
                
                # 確保target有在被left-mid包住 , 又mid > target才可以這樣 
                if nums[left] <= target < nums[mid]: 

                    right = mid - 1  
                    
                else : 
                    left = mid  + 1 
            
            # nums[left] > nums[mid]   
            else : 
                
                if nums[right] >= target > nums[mid] : 
                    
                    left = mid + 1 
                
                else : 
                    right = mid - 1
                    
        return False 
            
            

from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        
        left , right = 0 , len(nums) - 1 
        
        while left <= right : 
            
            mid = left + (right-left)//2 
            if nums[mid] == target : return True 
            
            # 處理duplicate 
            if nums[left] == nums[right] : 
                
                if nums[left] == target : return True 
                
                left += 1 
                continue 
            
            # 代表 left -> mid是sorted過的範圍
            if nums[left] <= nums[mid] :  
                
                if nums[mid] > target >= nums[left] : 
                    right = mid - 1 
                
                # target > nums[mid] >= nums[left]
                else : 
                    left = mid + 1 
                    
            
            # 代表 mid->right是sorted過的範圍 , 另外在此 nums[left] > nums[mid] 
            else : 
                
                if nums[right] >= target > nums[mid] :  
                    
                    left = mid + 1 
                
                # nums[right] >= nums[mid] > target
                else : 

                    right = mid - 1 
                
                
        return False 
                