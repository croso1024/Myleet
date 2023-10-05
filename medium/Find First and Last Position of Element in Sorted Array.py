""" 
    此題為書本在Binary search的進階概念 "左側邊界與右側邊界"對應的題目 
    看提交紀錄來說我在2022就有做過 , 當初是使用Binary search找到target number後
    使用while 迴圈向左右兩邊擴散 . 
    
    現在學習左右邊界的Binary search後 , 直觀來說可以用兩次的Search來找出左右邊界 
    即 2 x O(LogN)  . 
"""

""" 
    解法一. 
        直觀上的就是左邊界搜索與右邊界搜索各走一次  , 我採用的是封閉區間的邊界搜索方式 
        最關鍵的步驟在於" 找到目標數值後仍要進一步壓縮搜索空間 " , 
        對於尋找左側邊界來說 , 進一步壓縮後新的mid只會等於(再壓縮)或小於(讓left前進) ,
        而前進的結果就是站上第一個target .
        
        如此最終就可以定位在第一個(最後一個)出現的target位置
"""
from typing import List 


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        sol_left = -1 
        sol_right = -1 
        # 第一次先run一個左側邊界搜尋 , 使用封閉搜索空間比較好寫 : 
        left , right = 0 , len(nums)-1 
        while left <= right : 
            mid = left + ( right - left )//2  # == (left+right) // 2 
 
            # 左側邊界搜尋 , 當我們遇到target的時候就是將搜索空間嘗試往左再縮小            
            if nums[mid] == target : 
                # 關鍵步驟 , 即便找到了也要進一步壓縮搜索範圍 , 如此一來最終會定位在第一個target上
                right = mid - 1  

            # 調整搜索空間為 [left , mid-1]
            elif nums[mid] > target : 
                right = mid - 1 

            # 調整搜索空間為 [mid+1 , right] , 如果最終有找到結果 , 則left經過mid+1後會指向左邊界 
            else : 
                left = mid + 1 
                
        if left >= 0 and left < len(nums) and nums[left] == target: 
            sol_left = left 
                
        # 第二階段 , 執行右側邊界搜索 
        left , right = 0 , len(nums)-1 
        while left <= right : 
            mid = left + (right-left) // 2 
            
            if nums[mid] == target : 
                left = mid + 1 
            elif nums[mid] > target : 
                right = mid - 1 
            else : 
                left = mid + 1 
        
        if right >= 0 and right < len(nums) and nums[right] == target : 
            sol_right = right 
        
        return [sol_left , sol_right]
        
C = Solution() 
print(C.searchRange(nums=[1,2,2,2,3] , target=2))
print(C.searchRange(nums=[1,2,2,2,3] , target=3))
print(C.searchRange(nums=[1] , target=1))
            
            
                

