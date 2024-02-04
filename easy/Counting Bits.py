
""" 
    題意 :
        給定整數n , 要返回0->n所有數值在binary表示下的1的數量
    思路 :

        我的第一個想法是DP , 使用 << , >> 運算符可以快速幫我們去算乘除2
        一個數值乘上2就是在後面加上一個0 , 假設 x % 2 == 0 , 則x的binary 1的數量等於 x//2 
        若一個數字k不是偶數 , 則等於 1 + (k//2)有幾個1在其binary representation內這樣 
        
        
"""

from typing import List 
class Solution:
    
    def countBits(self, n: int) -> List[int]:
        
        if n == 0 : return [0]
        
        table = [ 0 for i in range(n+1)]
        # base case等於0,1 
        table[0]  = 0 
        table[1] = 1 
        
        for i in range(2,n+1):  
            
            if i % 2 == 0 : 
                table[i] = table[i//2]  
            else : 
                
                table[i] = table[i//2] + 1 
        
        return table 