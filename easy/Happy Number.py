""" 
    思路 : 
        這一題看起來也有點像是玩數學的題目 , 給定一個數字n 
        我們要將這個數字的每一位做平方並加總來得到新的數字。
        反覆執行這些加總直到數字的和等於1 , 如果可以等於1即為happy number . 
        如果反覆執行無法得到就不是happy number . 
        
        這一題直觀想要拆解成兩個part .
        1. -> 如何處理任意輸入大小n , 依照題意去做digits-wise的square sum 
        2. -> 中止條件 , 如何判斷這個數字往下做也無法到達happy number 
        
        
        針對第一個問題 , 我的打算就是轉str然後遍瀝去累加sum , 
        同時針對第二個問題 , 一個hashset用來保存找過的數值 ,一旦重複就代表無法到達happy number 
"""


""" 
    解法一. 直接寫一個透過build-in做轉換的函數來處理逐數字的平方和
"""
class Solution:

    def isHappy(self, n: int) -> bool:
        
        hashset = set() 

        while n not in hashset : 
            hashset.add(n)  
            sum = 0 
            for digits in str(n): 
                sum += pow(int(digits),2) 
            
            if sum == 1 : return True 
            n = sum 
            
        return False 
             
            
""" 
    看了討論區其他人針對逐數字平方和的作法進行修改
"""
import math 

class Solution:

    def isHappy(self, n: int) -> bool:
        
        hashset = set() 

        while n not in hashset : 
            hashset.add(n)  
            sum = 0 
            while n : 
                # n%10代表最後一個數字 
                sum += (n % 10) ** 2 
                # 將n除以10後捨去小數 , 相當直接砍掉最後一位數
                n = math.floor( n/10  )
            
            if sum == 1 : return True 
            n = sum 
            
        return False 