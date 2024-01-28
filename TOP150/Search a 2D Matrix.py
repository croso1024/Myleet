from typing import List 

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        height = len(matrix)
        width = len(matrix[0])
        
        # 先使用row進行binary search , 再使用column方向 
        left = 0 
        right = height - 1 
        target_row = None 
        
        
        while left <= right : 
            
            mid = left + (right-left) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][width-1]  : 
                # 找到目標row了 , 開始針對這個row做search 
                
                target_row = mid 
                break 
                
            elif target < matrix[mid][0] : 
                right = mid - 1 
            elif target > matrix[mid][width-1] : 
                left = mid + 1 
            else : 
                return False 
        
        if not target_row is None  : 
            
            left , right = 0 , width - 1 
            
            while left <= right : 
                mid = left + (right-left) // 2 
                
                if matrix[target_row][mid] == target : 
                    return True 
                elif matrix[target_row][mid] > target : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            
            return False 
        
        return False 