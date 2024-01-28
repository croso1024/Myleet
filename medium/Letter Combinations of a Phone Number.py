""" 
    思路 :  
        這題單純只是要羅列出所有的排列組合 -> 直接想到要用backtrack
        不過這一題居然要自己把每個button對應的字母寫起來有點2
"""


from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0 : return []
        table = {
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        solution = [] 
        
        # backtrack : 參數為剩下的digist , track則是目前該分支所拼湊的字
        # 這一題比較單調展開 , 只要展當前的字母所對應的所有可能 
        def backtrack(res_digits , track) : 

            if len(res_digits) == 0 : 
                solution.append("".join(track)) 
                return 
            
            for char in table[res_digits[0]] : 
                
                track.append(char)
                backtrack( res_digits[1:]  , track )
                track.pop()
        
        backtrack(digits , []) 
        
        return solution