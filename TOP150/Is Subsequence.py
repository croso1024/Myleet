class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t) : return False 
        
        probe_s = 0 
        probe_t = 0 
        
        # 兩個指標一起走 , probe_s指到的代表當前要"對消"的字母 
        # 一旦probe_t指向了一個和probe_s一樣的值 , 就可以讓probe_s往前走 , 如果probe_s走完則為True            
        while probe_t < len(t) and probe_s < len(s) : 
            
            if s[probe_s] == t[probe_t] : 
                probe_s += 1 
                probe_t += 1 
        
            else : 
                probe_t += 1 


        # 離開while後 , 如果probe_s != len(s) , 則為False 
        return True if probe_s == len(s) else False                 
            

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        probe_s = 0 
        
        for char in t :
            if probe_s < len(s)  and  char == s[probe_s]: 
                probe_s += 1 
        
        return True if probe_s == len(s) else False 