""" 
    思路 : 
        這一題要計算字串中最後一個單字的長度 , 空間可能會有空字串   
"""

""" 
    解法一. 完全不使用內建function , 走O(N) 速度不太好 , 空間極優 
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        word_length = 0 
        last_length = 0 
        pos = 0 

        while pos < len(s): 
            
            if s[pos] == " ": 
                last_length = word_length if word_length != 0 else last_length
                word_length = 0 
            else : 
                word_length += 1 
            pos += 1 
        
        last_length = word_length if word_length != 0 else last_length
        
        return last_length

""" 
    解法二. 
        寫完解法一想到 , 完全可以從後面倒數回來 , 這樣只要第一次中斷就找到答案了
        速度有明顯提昇 , 空間不佳
    
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        pos = len(s) -1 
        word_length = 0 

        while  pos >= 0 : 
            
            if s[pos] == " " and word_length == 0: pass 
            elif s[pos] != " " :
                word_length += 1 
            
            else : 
                return word_length 
            
            pos -= 1 

        return word_length