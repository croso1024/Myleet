# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

""" 
    題意 : 
        給定數字n , 並已知從某個數字開始是所謂的bad version ( 概念上說 , 在某個版本有問題後 , 使得後方的版本都有問題) 
        我們可以用題目給定的isBadVersion API來做是否為bad version的檢查 , 總之我們要用盡量少的call 數去找到bad version
        
    思路 :
        蠻無腦的做 left bound binary search 
"""

def isBadVersion(version : int) -> bool : 
    pass 


""" 
    解法一: binary search with left bound 
        注意這一題是給n個版本 , 即數列為 1,2,3,...,n
"""
class Solution:

    def firstBadVersion(self, n: int) -> int:
        
        left , right = 1 , n 
        
        while left <= right : 
            
            mid = left + (right-left)//2 
            
            # 往左極限逼近
            if isBadVersion(mid) : 
                
                right = mid - 1 
            
            # 如果不是bad version , 代表要將mid往右移 , 即往右邊縮小
            else : 
                left = mid + 1 
            
        return left 