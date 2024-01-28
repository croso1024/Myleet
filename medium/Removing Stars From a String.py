""" 
    思路 : 
    
        給定一個包含*的字串s , 每一個*會消除掉他左邊最近的非*字符 , 求給定的輸入經過消除完成後的結果 
        最直接的想法可能是stack , 遇到*就做pop , 但這麼直觀的想法不太確定說這一題為什麼可以是medium 
        
        總之先implement一個stack來嘗試 
"""


""" 
    解法一. stack solution , 有點訝異說這樣能過 , 速度還不錯就是空間略差 , 因為存了一個stack 
"""
class Solution:
    
    def removeStars(self, s: str) -> str:
        
        stack = [] 
        
        for item in s : 
            if item == "*" : 
                stack.pop() 
            else : 
                stack.append(item) 
                
        
        return "".join(stack) 
    

