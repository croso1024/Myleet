class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle and needle in haystack and not needle==haystack:  
            l= len(needle) 
            
            for i,char in enumerate(haystack): 
                
                for j in range(l): 
                    if haystack[i+j] == needle[j]:
                        index = i
                    else:
                        index = -1 
                        break 
                if index>=0 :
                    return index
            
                    
 
            
        else : 
            return ( 0 if (not needle or needle==haystack) else -1  )


    # 討論區 
    class Solution:               #--> 速度和空間都和我寫的差不多
        def strStr(self, haystack: str, needle: str) -> int:
            if needle not in haystack:
                return -1
            else:
                return haystack.index(needle)  

    class Solution:             # -->速度快不少
        def strStr(self, haystack: str, needle: str) -> int:
            return haystack.find(needle) 