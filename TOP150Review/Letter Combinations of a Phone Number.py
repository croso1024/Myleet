from typing import List 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map_table = {
            "2" : "abc" , 
            "3" : "def" , 
            "4" : "ghi" , 
            "5" : "jkl" , 
            "6" : "mno" , 
            "7" : "pqrs" , 
            "8" : "tuv" , 
            "9" : "wxyz" , 
        }
        if len(digits) == 0 : return [] 
        sol = [] 
        
        def backtrack( res , track  ): 
            
            if not res  : 
                sol.append( "".join(track) ) 
                return 
            
            # 拿出當下第一個號碼所對應的所有字母 
            for char in map_table[res[0]] :   
                
                # 把字母放進track , 遞迴展開"少了第一個號碼"的狀態 
                track.append(char)
                backtrack(  res[1:]  , track  ) 
                track.pop()
            
        backtrack( digits  , []) 
        return sol 