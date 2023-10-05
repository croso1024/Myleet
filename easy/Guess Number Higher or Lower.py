# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass 

""" 
    這一題比較特殊 , 提供API給我們互動!? , 在給定的一個數值範圍1-n內 , 
    透過binary search去找出未知的目標數值 ,
    我們可以call guess()來看我們猜測的數字是否正確 , 
    換句話說就是在判斷binary search的mid的部份改成call guess() 

"""

class Solution:

    # 做binary search , 這一題特殊在於說他不是一般的array做binary search 
    # 因為是給定1-n的範圍 , 因此我們要仔細定義好搜索區間 
    def guessNumber(self, n: int) -> int:
    
        # 初始化搜索區間為封閉 [1,n]  , 一般來說會是[0 , n-1]
        left , right = 1 , n   
        
        while left <= right : 
            # 我們可以pred目標數字
            pred = left + (right-left) // 2 
            
            # 通過guess()來得知我們猜測的數字是大於小於等於目標 
            if guess(pred) == 0 : return pred 
            
            # guess(pred) == 1 : 預測值低於實際值 
            elif guess(pred) == 1 : 
                left = pred + 1 
            else : 
                right = pred - 1  
                
        return False     
            
                
                