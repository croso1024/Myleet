class Solution:
    
    
    # diffustion approach  
    def countSubstrings(self, s: str) -> int:
        
        sol = 0 
        probe = 0 
        size = len(s) 
        
        while probe < size : 
            
            # temp 保存 以s[probe]為中心的回文串數量
            temp = 1 
            # 檢查奇數長度回文串
            
            i = 1 
            while (probe-i >=0 and probe+i < size) and s[probe-i] == s[probe+i] : 
                temp += 1 
                i += 1 
                
            # 檢查偶數長度回文串 
            if probe+1 < size and s[probe] == s[probe+1] : 
                # 如果滿足右邊也是同個字,回文串數量先加一再開始檢查 
                temp += 1  
                i = 1 
                while (probe-i >= 0 and probe+i+1 <size) and s[probe-i] == s[probe+i+1] : 
                    temp += 1 
                    i += 1 
            probe += 1 
            sol += temp 
        
        return sol  