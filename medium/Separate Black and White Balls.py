
"""
    思路 : 問幾次操作能把所有0放在左邊 ,1放在右邊 
    100 
    1101 
    10101 - > 10011 -> 01011 -> 00111 3次   
    
    我的想法是 , 初始狀態下每一個1右邊有幾個0的總和就是答案     
    所以這邊要存一個array , array[i]代表從index=i的"右方" 有幾個0  
    最後走訪過程遇到 s[i] == 1 就在答案 += array[i]
"""

""" 
    實做上面的想法 , 但速度與空間都不是很優 , 我總共走兩次O(N) , 空間也存O(N)
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        
        array = [0 for i in range(len(s))]
        acc = 0 
        # 由後往前traverse 
        for i in range(len(array)-1 , -1, -1):  
            
            array[i] = acc 
            if s[i] == "0" : acc += 1
        
        sol = 0 
        for i in range(len(s)):  
            
            if s[i] == "1": sol += array[i] 
        
        return sol 
    
    
""" 
    上面兩段O(N)其實可以只走一次 , 而且不需要儲存 ,只要記住就好  
    速度變得很優 , 空間很優 
"""

class Solution:
    
    def minimumSteps(self, s: str) -> int:
        
        acc = 0  
        sol = 0 
        for i in range(len(s)-1 ,-1,-1): 
            
            if s[i] == "1": 
                sol += acc 
            else : 
                acc += 1 
        
        return sol 
            
        