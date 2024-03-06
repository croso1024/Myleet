""" 
    題意:
    
        給定字串s1,s2,s3 .如果把 s1,s2各自拆開成為n,m個sub-string group ,且 |n-m| <= 1 , 且交錯排列
        這樣是否可以湊成s3. example. 
        s1 湊成 a,b兩個group , s2湊c,d , 問 a,c,b,d 或 c,a,d,b 這樣可不可湊成s3, 注意不能是 a,d,b,c 仍要保持group的順序

    思路:
        透過recursion , 在每一個recursion中使用雙指標去交替的填充字串,
        當遇到s1,s2的值都可以用來被填充,就兩種可能性都嘗試.
        
        另外這一題有個比較重要的implicity的想法就是, 其實不用太care分sub-string後變成 |n-m| <= 1 .
        因為只要是交錯排列就必定是滿足|n-m| <= 1 
"""

""" 
    Method.1 直接recursion without memo
    直接就是兩個字串交錯比對,一旦遇到兩種都可以的情況就展開 , 我這邊直接使用原始函數,故recursion function的含意就如同原始題目定義
    但這個解法沒有memo , 時間複雜度上我想應該不優 , 有明顯優化空間
    
    --- 
    這個解法我沒有拿去跑測試,所以有個edge case我沒有注意到,
    就是有可能s1或s2實際上還沒用完, s3就被填滿. 需要為這種probe1 or probe2還沒走到底的情況做一層保護
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        probe1 , probe2 = 0 , 0
        for i in range(len(s3)): 
            
            if (probe1 < len(s1) and s1[probe1] == s3[i]) and (probe2 < len(s2) and s2[probe2] == s3[i]) :          
                
                return self.isInterleave( s1[probe1+1:] , s2[probe2:] , s3[i+1:]  ) or self.isInterleave( s1[probe1:] , s2[probe2+1:] , s3[i+1:]  )
            
            elif probe1 < len(s1) and s1[probe1] == s3[i] : 
                probe1 += 1 
            elif probe2 < len(s2) and  s2[probe2] == s3[i] : 
                probe2 += 1 
            else: return False 
        
        return True 
    
    
""" 
    Method.2 , 優化解法一, 改變recursion function 的parameter為指標數值
    
    但這一題有個相當奇妙的地方, 一開始我在 ( probe1 < len(s1) and s1[probe1] == s3[i] ) 的兩種case中是直接probe1+1這樣去走
    算是老老實實的算完這一段recursion , 只有在遇到兩個選擇都可以的時候展開. 這樣會導致計算速度慢很多而exceed time limit
    稍微去想一下,在原本的作法recursion的展開點只有在s1,s2都同時遇到可用, 這樣還是會有很多冗餘的計算
    因此需要把普通的流程也加入填memo
    
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3) : return False 
        memo = dict() 
        size = len(s3)
        
        # 返回在 s1[probe1:] , s2[probe2:] , s3[probe1+probe2:] 這個範圍內是否可以有interleaving stirng的solution
        # 實際上就和原始題目的definition一樣,但更改了parameters為數值
        def recursion(probe1 , probe2): 
            
            k = probe1 + probe2 
            if (probe1,probe2) in memo :
                return memo[(probe1,probe2)] 
            
            for i in range( k , size): 
                
                # 兩種情況都可以的case
                if ( probe1 < len(s1) and s1[probe1] == s3[i] ) and (probe2 < len(s2) and s2[probe2] == s3[i] ) :  
                    
                    memo[(probe1,probe2)] = recursion(probe1+1 , probe2 ) or recursion(probe1 ,probe2+1)
                    return memo[(probe1,probe2)]

                elif ( probe1 < len(s1) and s1[probe1] == s3[i] ) :  
                    
                    memo[(probe1,probe2)] =  recursion(probe1+1 , probe2)
                    return memo[(probe1,probe2)]
                
                elif ( probe2 < len(s2) and s2[probe2] == s3[i] ) :  
                    
                    memo[(probe1,probe2)] = recursion(probe1,probe2+1)
                    return memo[(probe1,probe2)]
                
                else : 
                    
                    memo[(probe1,probe2)] = False 
                    return False 
            
            if probe1 == len(s1) and probe2 == len(s2) : 
                memo[(probe1,probe2)] = True 
                return True 
            else : 
                memo[(probe1,probe2)] = False 
                return False
        
        return recursion(0,0) 

""" 
    修正一下解法二的結構 , 既然每一步都要跳recursion展開,那就不需要for-loop了
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3) : return False 
        memo = dict() 
        size = len(s3)
        
        # 返回在 s1[probe1:] , s2[probe2:] , s3[probe1+probe2:] 這個範圍內是否可以有interleaving stirng的solution
        # 實際上就和原始題目的definition一樣,但更改了parameters為數值
        def recursion(probe1 , probe2): 
            
            k = probe1 + probe2 
            if k == len(s3) : return True 
            
            if (probe1,probe2) in memo :
                return memo[(probe1,probe2)] 
            
                # 兩種情況都可以的case
            if ( probe1 < len(s1) and s1[probe1] == s3[k] ) and (probe2 < len(s2) and s2[probe2] == s3[k] ) :  
                
                memo[(probe1,probe2)] = recursion(probe1+1 , probe2 ) or recursion(probe1 ,probe2+1)
                return memo[(probe1,probe2)]

            elif ( probe1 < len(s1) and s1[probe1] == s3[k] ) :  
                
                memo[(probe1,probe2)] =  recursion(probe1+1 , probe2)
                return memo[(probe1,probe2)]
            
            elif ( probe2 < len(s2) and s2[probe2] == s3[k] ) :  
                
                memo[(probe1,probe2)] = recursion(probe1,probe2+1)
                return memo[(probe1,probe2)]
            
            else : 
                memo[(probe1,probe2)] = False 
                return False 
       
        
        return recursion(0,0) 

S = Solution()
s1 = "abababababababababababababababababababababababababababababababababababababababababababababababababbb"
s2 = "babababababababababababababababababababababababababababababababababababababababababababababababaaaba"
s3 = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"
print(S.isInterleave(s1,s2,s3))