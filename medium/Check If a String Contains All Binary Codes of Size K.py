""" 
    題意:   
        給定一串binary code string s , 以及整數k
        要問是否所有length=k的binary string都包含在這組binary code ( continue sub-string )
        
    思路:   
    
        第一個想法就是DFS展開,走到長度為k後,如果是一個沒看過的binary code就將其加入set,
        最終統計set中有多少組binary code就可以知道是否包含所有的組合 , 
        但這個解法因為s.length可以到 10^5 級別 , 雖然最多展開深度為k=20,但感覺速度上不是最佳
        ----
        實際寫完之後發現,這一題要的是'連續的sub-string' 所以我的想法轉為使用sliding window,但一樣是做相似的事情,
        移動window後如果是新的字串就加入set
"""

""" 
    解法一. sliding window , 這個解的速度還不錯,空間較為普通
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
       hashSet = set() 
       
       for i in range(  len(s) - k + 1  ) :
           
           code = s[i:i+k] 
           
           if not code in hashSet : 
               hashSet.add(code )
            
       return len(hashSet) == pow(2,k) 
                

S = Solution()
print(S.hasAllCodes("00110" , k =2 ))
        