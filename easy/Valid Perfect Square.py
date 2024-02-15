""" 
    題意:
        給定一個整數num , 要判斷這個整數是否是完全平方數 , 不可以使用built-in function
"""

""" 
    解法一 , 檢查根號取整的平方是否能還原數字 , 這個解的速度與空間就很不錯了
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        return True if int(num**0.5) * int(num**0.5) == num else False 

""" 
    解法二, binary search去尋找一個可以相乘等於解的數值 
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l , r = 1 , num 
        
        while l <= r : 
            
            mid = l + (r-l)// 2 
            
            midSqrt = mid  * mid 
            
            if midSqrt == num : return True 
            elif midSqrt > num :  
                r = mid - 1 
            else :
                l = mid + 1 
        
        return False 
            