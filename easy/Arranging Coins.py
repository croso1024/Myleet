""" 
    題意:   
        給定n個錢幣用來排成一列列 , 第i列總共需要i個錢幣來排滿
        我們要計算給定的n塊錢幣可以'排滿'幾個row 
        
    思路: 
        
        若n個錢幣可以排到m row , 則 n > m(1+m)//2   
        也可以說 n 屬於: 
        m(1+m) // 2  < n  <= (m+1)(1+(m+1)) // 2  
        
        而n必定小於row數 , 所以我們使用binary search 初始的bound就為 1 , n 
"""

""" 
    解法一. binary search 
        速度與空間都不錯
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left , right =  1 , n 
        
        while left <= right : 
            
            mid = left + (right-left)//2 
            # 排到mid level所需要的coins 
            midCoin1 = (mid*(1+mid)) // 2 
            midCoin2 = ( (mid+1)*(2+mid) ) // 2
             
            # n的數量剛好等於mid層
            if midCoin1 <= n < midCoin2:
                return mid
            
            # n的數量大於midCoin數量
            elif n >= midCoin2 :
                left = mid + 1 
            
            elif n < midCoin1 : 
                right = mid - 1 
        
        return -1   

C = Solution() 
print(C.arrangeCoins(n=2525153253))