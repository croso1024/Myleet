""" 
    思路 : 
        這一題只是要計算整個字串中的字母可以湊出幾個 balloon
        ,用一個hashmap去統計每一個字母的出現次數 , 
        然後去看b a l o n各自出現了幾次 
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        
        word_dict = dict() 
        for char in text: 

            if char in word_dict: 
                word_dict[char] += 1 
            else : 
                word_dict[char] = 1 
        
        # 檢查balloon的元素足夠湊出幾個 
        sol = 0  
        
        
        def makeInstance(): 
            nonlocal word_dict 
            
            if "b" in word_dict  and word_dict["b"] > 0: 
                word_dict["b"] -= 1
            else : 
                return False 
            
            if "a" in word_dict  and word_dict["a"] > 0: 
                word_dict["a"] -= 1
            else : 
                return False 
                
            if "l" in word_dict  and word_dict["l"] > 1: 
                word_dict["l"] -= 2
            else : 
                return False 
            
            if "o" in word_dict  and word_dict["o"] > 1: 
                word_dict["o"] -= 2
            else : 
                return False 
            
            if "n" in word_dict  and word_dict["n"] > 0: 
                word_dict["n"] -= 1
            else : 
                return False 
            return True 
            
        while makeInstance() : 
            sol += 1 
        
        return sol 
            
        
        