

""" 
    思路 : 
        這一題使用DP來解, 建立dp table , 使用dp[i]來對應 字串s[:i]的部份有多少種decode方法
        因為題目告知0在前無法decode , 因此開頭數字若為0就是違反規則等於 0 
        
        - 狀態轉移方程式: 
        Case.1 
            當加入一個新的數字 dp[i] , 如果他可以獨立表示 , 同時又能夠和前一個數字結合的話 , 
            那麼解碼方法為 dp[i-1] + dp[i-2] , 以1123 為例, 在加入3的時候 
            如果把3當作獨立的解碼 , 那不影響總解碼數 , 因此為dp[i-1] 
            如果把3和前一個數字合併來看 , 那麼解碼總數則為 dp[i-2]  ,  
        Case.2 
            加入一個新數字,可以獨立表示但無法合併前一個數字 , 則解碼方式不會增加 ,dp[i]=dp[i-1] 
        Case.3 
            加入的新數字為0 , 
                則前一個數字必須是1或2 , 否則無法解碼
                如果是1或2了 , 則解碼數量 dp[i]等於dp[i-2] , 因為合併綁死了前一個數字 
                例如 1120 在加入0的時候 ,解碼方法等於只有11時的兩種
            
        
        
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0" : return 0 
        
        dp = [None] * (len(s)+1)
        # 我們設定dp[0]代表字串是空的時候的解碼數量 ,將其設為一主要是方便計算 
        dp[0] = dp[1] = 1 
        
        
        # 注意我們的dp table是0個字母到所有字母 , 共 len(s)+1的長度 
        # 而for loop的i是指dp-table的索引 , 換算到字母索引要-1 ,
        # ex. dp-table的索引3相當於第三個字母 , s[2]
        for i in range(2,len(s)+1) :
            
            char = s[i-1] 
            
            if char == "0" :  
                # 新加入的數字為0 , 則前一個數字必須要是1或2 
                if not s[i-2]  in ["1","2"] : return 0 
                # 必須和前一個數字合併 
                dp[i] = dp[i-2]  
            
            # 來到這個else , 至少該數字可以單獨表示 , 因此就是檢查能不能做合併表示 
            else : 
                # 要合併至少前一個數字不能是0 , 並且兩個數字小於等於26
                if not s[i-2] == "0" and int(s[i-2]+char) <= 26 : 
                    
                    dp[i] = dp[i-1] + dp[i-2] 
                
                # 只能單獨表示無法合併  
                else : 
            
                    dp[i] = dp[i-1] 
        
        
        return dp[-1] 
    

C = Solution()
C.numDecodings(s="1123")
        