
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        
        probe = len(s) - 1 
        length = 0 
        
        while probe >= 0 and s[probe] == " ":
            probe -= 1 
        
        
        while probe >= 0 : 
            
            if s[probe] != " ": 
                length += 1 
            else : break 
        
        return length 