
class Solution:
    def romanToInt(self, s: str) -> int:
        
        ref = {
            'I' : 1 , 
            'V' : 5 ,
            'X' : 10 , 
            'L' : 50 , 
            'C' : 100 , 
            'D' : 500 , 
            'M' : 1000 , 
        }
        
        probe = len(s) - 1 
        solution = 0 

        while (probe > 0) : 

            if ref[s[probe]] == ref[s[probe-1]] * 5 or ref[s[probe]] == ref[s[probe-1]] * 10 : 
                solution += ( ref[s[probe]] - ref[s[probe-1]]) 
                probe -= 2  
            else : 
                solution +=  ref[s[probe]]
                probe -= 1 
        
        if probe == 0 : 
            solution += ref[s[probe]]
        
        return solution