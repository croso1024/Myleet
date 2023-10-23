""" 
    思路 : 
        此題給初兩個字串 s和p , 要求我們返回所有p的異位同構詞出現在s中的index, 
        這邊所謂的s中的異位同構詞直白來講就是對應元素的出現次數和p一樣的子字串 , 
        
        我們要維護一個大小和p相同的window , 然後掃略過去 , 只要window裡面是同構詞,
        就將left(起始index)放進result的array內
        
        解法一就是比較直覺的 fixed window sliding 
        解法二就是依照東哥的框架 , 伸縮式的sliding window
"""


""" 
    解法一. 
        固定長度window掃蕩 , 判斷有效使用一個dict和valid_digits來做 
"""
from typing import List 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s) : return [] 
        
        left = 0 
        right = len(p) 
        window = dict()
        target = dict() 
        valid_digits = 0 
        sol = [] 
        # 更新target dict 
        for char in p :     
            if char in target : target[char] += 1 
            else : target[char] = 1 
            
        # 初始window的內容放進window dict , 順便修改valid-digits
        for char in s[:right] : 
            if char in window : window[char] += 1
            else : window[char] =1
            if char in target and window[char] == target[char] : 
                valid_digits += 1
        
        
        if valid_digits == len(target.keys()) : sol.append(left)
        
        # 開始做sliding window : 
        # 1.移動right並更新window , valid_digits
        # 2.移動left並更新window , valid_digits 
        # 3.檢查是否為解
        while right < len(s) :  
            
            add = s[right] 
            if add in window : window[add] += 1 
            else : window[add] = 1 
            if add in target  and target[add] ==  window[add] : valid_digits+=1 
            right += 1
            
            
            # 更新步驟略有不同, 因為remove一定是先前看過的值,window中必定有key ,
            # 另外先檢查是否在target內並且數量相等 , 是的話才會因為移除而減少valid-digits
            remove = s[left] 
            if remove in target and target[remove] == window[remove] : valid_digits-=1
            window[remove] -=1 
            left += 1
            
            if valid_digits == len(target.keys()) : sol.append(left)
            
        
        return sol
    
""" 
    解法二 . 標準sliding window框架 , 這個方法的time complexty和space都略優於方法一(但我覺得更像是線上執行的誤差)
    不過整個程式碼框架比較乾淨一些

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(p) > len(s) : return [] 
        
        left = 0 
        right = 0
        window = dict()
        target = dict() 
        valid_digits = 0 
        sol = [] 

        # 一樣需要先將target dict更新起來
        for char in p : 
            if char in target : target[char] += 1 
            else : target[char] = 1
       
        # 其實實際的更新步驟和定長window基本上就一樣 , 只是結構上的差異 ,
        
        while (right < len(s)) : 
            
            add = s[right] 
            if add in window : window[add] += 1 
            else : window[add] = 1 
            if add in target and target[add] == window[add] : 
                valid_digits += 1 
            
            right += 1 
        
        
            # 注意更新解的位置!! 以及判斷是否要收縮的條件
            if valid_digits == len(target.keys()) : 
                sol.append(left) 
                
            while ( right - left == len(p) ) :
                
                remove = s[left] 
                if remove in target and target[remove] == window[remove] : 
                    valid_digits -= 1 
                window[remove] -= 1 
                left += 1 
                
        return sol