""" 
    題意 : 
        給定一個字串 , 要判斷該字串在刪除 0 or 1個任意字元後是否可以成為 palindrome , 
    
    思路 :
        這一題就是一個回文串判斷 , 有一次掛掉機會的版本 . 
        我打算使用雙指標內縮來進行判斷 
        
        當遇到左右指標指向不同字元 , 且一次免死金牌還在 :
        檢查 left+1 - right 以及 left - right-1 範圍是否全都是回文 
        
"""

""" 
    解法一.     
        實際的實做也不需要特別用一個變數去 keep 我所謂的 '免死金牌' , 只不過發現異常後走內部的流程去判斷而已
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left , right = 0 , len(s) - 1 
        
        
        # 如果 left == right就一定是回文
        while left < right : 
            
            if s[left] == s[right]: 
                left  += 1 
                right -= 1
            
            # 我們有一次找到異常的機會 
            else :
                # 檢查 left+1 到 right 與 left到 right-1的範圍
                i = left + 1 
                j = right 
                
                l1r , lr1 = True , True 
                
                while i < j : 
                    if s[i] == s[j] : 
                        i += 1 
                        j -= 1 
                    else : 
                        l1r = False 
                        break 
                
                i = left 
                j = right - 1 
                while i < j : 
                    if s[i] == s[j]:
                        i += 1 
                        j -= 1 
                    else : 
                        lr1 = False 
                        break 
                
                return l1r or lr1 

        return True 
                     
                 
            
            