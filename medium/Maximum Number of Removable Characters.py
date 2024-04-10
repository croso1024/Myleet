""" 
    題意:   
        給定兩個字串 , s和p ,而p是s的子字串(p的所有char在s都有且相對順序一樣) , 同時給定一個array: removable ,
        要求找到最大的k , 使用前k個removable中選擇的index去移除字串後p仍是substring 

    思路:
        因為substring需要有順序的問題,因此這一題不能直接使用hashmap保存 . 

        而這一題的問題在於找到k的極值 , 從暴力解的思路下去看 , 
        我們可以選擇移除1個 , 計算是否合乎解, 也可以計算移除2個計算是否合乎 , 
        但一有這樣的想法其實就可以想到透過binary search去找 , 因此問題在於
        我們要怎麼計算p是否為s的substring (而且是remove過指定index的substring)
        
        我認為檢查的部份 , 可以透過把 removable[:k] 轉為set傳入 , 
        用兩個probe掃略的方式去檢查 ,而這需要 O(s)的time complexity
        因此total time complexity是 O( LOG(removable) * O(s) ) 
        
"""

from typing import List 

class Solution:

    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        
        # 傳入一個k代表要移除多少個值
        def check(k): 
            removeIndex = set(removable[:k]) 
            s_probe = 0 
            p_probe = 0 
            while p_probe < len(p) and s_probe < len(s) : 
                
                while (s_probe in removeIndex) : 
                    s_probe += 1 
                    
                if not s_probe < len(s): return False 
                
                if s[s_probe] == p[p_probe] : 
                    s_probe += 1 
                    p_probe += 1 
                else : 
                    s_probe += 1 
            
            # 出來後, 只有兩種情況, p_probe走完, 代表是subString , s_probe走完,代表False 
            if p_probe == len(p): return True 
            else : return False 
        
        # 向右逼近的 binary search framework 
        left = 0 
        right = len(removable)
        
        while (left <= right): 
            
            removeAmount = left + (right-left) // 2 
            
            if check(removeAmount) : 
                left = removeAmount + 1 
            else : 
                right = removeAmount - 1 
        
        if right >= 0 : return right 
        else : return 0             

S = Solution()
print(S.maximumRemovals(s = "abcacb", p = "ab", removable = [3,1,0]))
print(S.maximumRemovals(s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]))