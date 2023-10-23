""" 
    思路 :  
        這一題給定一個只有 "a","b" 兩種字元的字串 , 並且我們每次可以移除其中palindromic的substring
        求至少要幾次的動作才能將這個字串清空 . 
        
        直覺上一看感覺這題不像easy , 因為每個字自己可以被當作回文 , 所以最多的移除步數會在 len(s) , 
        
        如果暴力列舉的話 , 那就是一個迴圈走過所有字元 , 並在其中 1.檢測回文 2.去除回文部份往下傳遞
        這樣的時間複雜度應該會爆炸 , 但應該是可行
        
        --> 結果這一題是智商壓制 , 我們可以移除回文子字串(定義為只要不改變order , 就可以任意跳過)  ,
        又因為字串只有a和b , 因此如果原始字串不是回文 , 那一定可以移除一次子字串變成回文
        
        因此答案只會是1 or 2 
        
"""

""" 
    解法一. 暴力列舉 , 在每一層遞迴都找所有回文可能性 , 然後計算移除的總次數
"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        solution = len(s)
        # 計算res字串 , 透過回文移除至少需要的步數 
        def min_step( res , remove_step ):
            nonlocal solution
            if len(res) == 0 : 
                solution = min(solution  , remove_step)
                return 



            for idx in range(len(res)): 
                
                count_odd = 0  
                count_even = 0 
                # 開始擴展找回文 , 如果沒有回文就break了 
                # 有回文就往下展開
                
                # 需要考慮回文串的長度為奇數與偶數的情況
                while idx-count_odd >=0 and idx+count_odd < len(res): 
                    
                    if res[idx-count_odd] == res[idx+count_odd] : 
                        min_step( res[:idx-count_odd] + res[idx+count_odd+1:] , remove_step+1 )
                    else : break 
                    count_odd+=1
                    
                
                while idx-count_even >= 0 and idx+count_even+1 < len(res): 
                    
                    if res[idx-count_even] == res[idx+count_even+1] : 
                        min_step( res[:idx-count_even] + res[idx+count_even+2:] , remove_step+1)
                    else : break 
                    count_even += 1 
                    
     

        min_step(s,0)
        return solution


""" 
    解法二 . 這題實際上只會需要一次或2次
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        if s == s[::-1] : return 1 
        else : return 2                     
