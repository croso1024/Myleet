from typing import List 


# naive solution : sort every word and use hashtable 
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = dict() 
        
        for str in strs : 
            
            sort_str = "".join(sorted( list(str) ))
            
            if sort_str in hashMap : 
                hashMap[sort_str].append(str) 
            else : 
                hashMap[sort_str] = [str]
            
        return list(hashMap.values())