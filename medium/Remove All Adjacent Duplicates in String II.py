""" 
    題意:
        給定一個字串s , 以及整數k
        題目會執行所謂的k duplicate removal , 將字串中第一次出現有連續k次的相同字母刪除 , 接著將刪除完後的左右兩邊接合
        接著再次執行k duplicate removal , 一直到找不到任何k連續字母出現
        
    思路:  
        這一題比較輕易的作法是使用stack, 在存的過程中同時紀錄"這是該字母連續出現的第幾次" , 
        以這個思路往下就相當簡單 , 當新字母等於stack最頂端的字母 , 就檢查是否要觸發消除,否則就是連續次數+1後加入stack
        
        而一旦消除發生 , 下一個字母也能自然地接上消完後的前半段 , 同時可以繼續累積連續出現次數
        
        TC:O(N) , MC:O(N), 
        
        
"""


""" 
    解法一. 按照上述思路,速度還不錯,但或許是我在stack中存了兩種東西導致空間很差 
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] 
        
        for letter in s : 
            
            if stack : 
                
                
                if stack[-1][0] == letter : 
                    
                    
                    if stack[-1][1] + 1 == k :  
                        
                        for i in range(k-1):stack.pop() 
                        
                    else : 
                        
                        stack.append ( (letter , stack[-1][1]+1 ) )

                else : 
                    
                    stack.append( (letter , 1 ))
            
            
            
            else : 
                
                stack.append( (letter,1) )
        
        return "".join( [ i[0] for i in stack  ] )
        

""" 
    解法二. 更加優化空間的作法,就是我不要直接存入新的item進入stack,而是直接修改stack頂端值的計數
        實際上因為降低pop次數 , 速度與空間都有很大提昇
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] 
        
        for letter in s : 
            
            if stack : 
                
                if stack[-1][0] == letter : 
                    
                    if stack[-1][1] + 1 == k :  
                        
                        stack.pop()
                        
                    else : 
                        
                        stack[-1][1] += 1 

                else : 
                    
                    stack.append( [letter , 1 ])
            
            else : 
                
                stack.append( [letter,1] )
        
        # 利用stack的每個元素代表的字體乘上出現次數
        sol = "" 
        
        for letter , times in stack : 
            sol += letter * times 
            
        return sol 
        
        

S = Solution()
print(S.removeDuplicates("deeedbbcccbdaa" , k=3))

            
            
            
            
        
        