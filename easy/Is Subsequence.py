""" 
    思路 : 
        給定字串s和t , 問是否可以刪除t中某些字串得到s ,
        因為考慮到字元的位置以及字串中可能有重複字元的問題 , 不能單看s中的每個字元是否有出現在t 
        
        目前想的方法大概有兩種 
        1. 基於Backtrack框架爆蒐所有可能性 , 透過剪枝加速 
        2. 類似DP的作法 , t字串從只有一個字開始 , 只要t加入的字符合s , 我們就可以開始等待下一個要出現在s的字 
        
"""

""" 
    解法一. 

        這一題使用backtrack的框架去列舉所有可能 , 並做一些剪枝
        - 一旦遇到一組可行就直接return True 
        - 如果t被砍到長度等於s還不等於也不用往下展開了

    --> 解法可行 , 但時間複雜度不可以

"""
class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        
        self.result = False         
        # 基於Back track的框架 , 這一題的動作清單和軌跡我認為可以一致 
        # 即把 "還可以刪除的字元" 作為動作清單 , 同時會隨著回溯樹展開而慢慢變小 
        
        def backtrack( subString ): 
            
            # base case就是已經砍到小於我們要找的目標 , 那就要返回了
            if len(subString) < len(s) or self.result : 
                return 
            
            # 找到目標字串 , 修改外部變數後return
            if subString == s : 
                self.result = True 
                return 
            
            for i in range(len(subString)) : 
                
                
                # pre-order位置要做的應該是做動作並傳入
                # 並在post-order撤銷動作 , 這邊因為是複製一份string作為參數 , 因此直接寫在backtrack裡面
                backtrack(  subString[:i] + subString[i+1:] )
                
        
        backtrack( t )
        return self.result
    
""" 
    解法二 . 
        我們就直接拿s[i] ,i=0 開始等待 , 用for-loop走t , 一旦遇到相同 , 那就可以i++等待下一個 ,
        一旦全部等到就完成也不用檢查後半 , 如此一來就O(n)時間 
        
        順利解,時間空間都蠻不錯的 , 但就不是依賴什麼框架
"""

class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        
        self.result = False 
        self.size = len(s) 
        if self.size==0 : return True 
        
        probe = 0 
        
        for char in  t :
            
            if char == s[probe] : 
                probe += 1
                if probe == self.size : return True 
        
        return False                  
                
                
                
             
        
        
        
        