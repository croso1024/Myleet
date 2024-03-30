class Solution:
    
    def longestPalindrome(self, s: str) -> str:
    
        best = s[0]

        def getPalindromic( i , j ):
            
            if s[i] != s[j] : return s[i]
            
            while ( i > 0 and j < len(s)-1):
                
                if s[i-1] == s[j+1] : 
                    i -= 1 
                    j += 1 
                else : break 
                
            return s[i:j+1]
        
        
        for i in range(len(s)-1): 
            
            
            odd = getPalindromic( i , i ) 
            even = getPalindromic( i , i+1) 
            
            if len(odd) > len(even) :
                
                if len(odd) > len(best) : 
                    best = odd 
            
            else : 
                
                if len(even)>len(best) : 
                    best = even 
            
        return best 
            

S = Solution() 
print(S.longestPalindrome('a'))