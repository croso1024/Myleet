""" 
    題目給定一個 M x N的矩陣 , 其中的每一列都是sort過的 , 
    同時每一列最大的元素會小於(沒有等於)下一列的小元素 , 我們要判斷題目給定的數值是否存在於matrix內
    
    思路 :  
        最簡單的作法可能就是將matrix攤為一個大list , 接著執行Binary Search 
        如此一來空間為O(M x N) , 時間為 O( log (M x N) ) 
        
        更好一點的作法 , 應該是把每一個row視為 (min , max) , 利用這個先針對row做Binary search 
        找到特定row後再針對該row做Binary search 
        
"""
from typing import List 

""" 
    解法一. 
        攤開matrix執行Binary search  
        
        -> 速度很優 , 但空間普通
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m , n = len(matrix) , len(matrix[0]) 
        flat = [] 
        for i in range(m) : 
            flat.extend(matrix[i])        
        #取得攤平後的矩陣flat 
        
        # 執行Binary Search  
        left , right =  0 , len(flat) - 1 
        
        while left <= right :  
            
            mid = left + (right-left)//2 
            
            if flat[mid] == target : return True 
            
            elif flat[mid] > target : 
                right = mid - 1 
            else : 
                left = mid + 1 
            
        return False 
            
""" 
    解法二.     
        雙重Binary Search , 
        外層的Binary Search用來尋找目標值落在哪個row 
        內層的Binary Search用來找尋在該row中是否有目標值  
        
        -> 超優速度與空間
"""
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 第一層的Binary Search     
        left , right = 0 , len(matrix) - 1 
        row = None 
        while left <= right : 
            mid = left + (right-left) // 2 
            
            # 使用區間來判斷元素是否落在區間內  , 如果找到了之後就可以跳出 
            if   matrix[mid][0] <= target <= matrix[mid][-1]   : 
                row = matrix[mid] 
                break  

            # 如果mid區間的最小元素大於target ,限縮搜索空間到左半
            elif matrix[mid][0] > target : 
                right = mid - 1  
                
            # mid區間的最大元素小於 target , 限縮空間到右半 
            elif matrix[mid][-1] < target : 
                left = mid + 1  
                
        # 如果沒有找到row的話 , 就算是找不到了 
        if not row :  return False 
        
        left , right = 0 , len(row) - 1  
        
        while left <= right : 
            
            mid = left + (right-left) // 2 
            
            if row[mid] == target : return True 
            
            elif row[mid] > target : 
                right = mid - 1 
            else : 
                left = mid + 1  
        
        return False 
        
        
        

            
             
                
        
        
        