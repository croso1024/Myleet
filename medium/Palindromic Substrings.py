""" 
    思路:    
        這一題對於如何定義DP-table以及怎麼處理 state transition都有點難度
        
        雖然這一題在neet-code是歸類在1D-DP,但我看起來好像也可以做2D-DP
        在唸過東哥的subarray/ subsequence DP分類後我好像總是傾向走2D-DP , 
        但也有題目是 "兩個1D-table一同使用"
        
        從1D的角度來看這一題 , 可以令DP table的方式不外乎
        1.dp[i] = 以 i 為結尾的substring 可以構成的palindromic
        2.dp[i] = 由 0~i 的範圍 , 構成的最大palindromic 
        
        從第二個定義方法 , 我認為比較有機會 
        
        這邊看了Leetcode給予的提示 , 
        如果 "xdx"是palindromic , 那 "bxdxb" 是不是也是? 
        
        看起來是要我們不斷內縮
        1. 主要內縮 dp(i+1 , j-1) 
        2. 調整的內縮 dp(i+1,j) , dp(i,j-1) 每次走到
        
        
        --> 這一題DP解我覺得實在有點太複雜 , 改用暴力解 , 實際上確實在遇到瓶頸時可以先考慮暴力解, 
        同時這一題的暴力解Time complexity 也是O(N^2)
        
        這一題給我的啟發還是 -> 擴張法仍然是處理回文一個有效的方式
"""


"""
    解法一. 
    先嘗試使用暴力解  , 從 s 只有一個字元開始 , 由該字串符的中央開始向外擴散 , 只要一直都是相同的 , 
    就一直累積回文數量  , 這一題使用DP , 我覺得Case有點太過複雜 , 
    主要是這種擴張法 , 他的Time complexity 也是O(N^2) , 
"""
class Solution:

    def countSubstrings(self, s: str) -> int:
        
        result = 0 
        
        # 給定字元所在的index , 奇數或偶數 , 然後向外擴張並且持續增加回文數量 , 直到遇到非回文
        def expand( i , j  ): 
            
            left , right = i , j
            temp = 0 

            while left >= 0 and right < len(s) : 
                if s[left] == s[right] : 
                    temp += 1 
                    left -= 1 
                    right += 1 
                else : break 
            
            return temp                 
                    
        
        
        
        
        for i in range(len(s)): 
            # 當字元的長度為奇數的時候
            result += expand(   i , i ) 
            # 當字元的長度為偶數的時候
            result += expand( i , i + 1 )
        
        return result 
            