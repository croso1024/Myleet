class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ref = dict() 
        be_map = set() 
        size = len(s) 
        probe = 0 

        while probe < size : 

            if s[probe] in ref : 

                if ref[s[probe]] == t[probe] : pass 
                else : return False 
            else : 

                if t[probe] in be_map : return False 
                else :

                    ref[ s[probe] ] = t[probe] 
                    be_map.add(t[probe])



            probe += 1 

        return True 