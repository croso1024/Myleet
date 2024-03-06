""" 
    題目:

        此題要求我們找出最長的happy string , happy string的定義如下:
        - 只有包含a,b,c
        - 不能有aaa,bbb,ccc這樣的出現
        - 只能使用最多a次的'a'
        - 只能使用最多b次的'b'
        - 只能使用最多c次的'c'
        
    思路:

        這一題我的直覺認為可以從DFS展開去想,每一步我們都可以在字串中加上a,b,c三種字的任何一種,
        但也要去注意當string的長度超過2時 , 不能有連續三個一樣字母的情況
        我的想法是去寫一個function展開這棵tree , 但難點在於如何定義這個函數使的展開的過程更有效率不會時間炸掉
        
        我想用遞迴函數去紀錄目前剩餘可用的a,b,c數量,這一題我認為並不是需要靠暴力展開再做優化,而是有規律可尋.
        我使用一個參數去紀錄上一次插入時使用的字母 , 並比較另外兩個未用在上次插入中的字母誰剩的多就用誰來插入.  
        一次最多插入兩個字母 , 若只能插入一個字母待表該字母就是只剩下一個 
        -----
        ->這個解法會有錯產生 , 例如a=3,b=21,c=72,在a用完後b會過早的被用完導致甚於的C沒有辦法再插入(因為b也都一次2個2個的使用) 
        
        
        所以後面參考hint , 這一題應該是使用greedy , 挑選出不會破壞規則但剩餘最多的那個字母插入 , 
        思路很簡單但寫起來有點繁雜,麻煩
                
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        solution = ''
        solution_size = 0 
        
        def insert(a,b,c  , string , lastTwo): 
            nonlocal solution , solution_size
            if len(string) > solution_size : 
                solution_size = len(string)
                solution = string 
                
            maxAppear = max(a,b,c) 
            if maxAppear == 0 : return 
            
            if lastTwo == 'aa' : 
                
                if b>= c and b > 0 : insert(a , b-1, c , string+'b' , lastTwo=lastTwo[1] + 'b')
                elif c > 0 : insert(a , b, c-1 , string+'c' , lastTwo=lastTwo[1] + 'c')
                
                 
            elif lastTwo == 'bb':
                
                if a >= c and a > 0: insert(a-1 , b, c , string+'a' , lastTwo=lastTwo[1] + 'a')
                elif c > 0 : insert(a , b, c-1 , string+'c' , lastTwo=lastTwo[1] + 'c')

                 
            elif lastTwo == 'cc': 
                
                if a>= b and a > 0: insert(a-1 , b, c , string+'a' , lastTwo=lastTwo[1] + 'a')
                elif b > 0 : insert(a , b-1, c , string+'b' , lastTwo=lastTwo[1] + 'b')

            
            else :   
                
                if maxAppear == a : insert( a-1,b,c , string+'a' , lastTwo= lastTwo[1] + 'a' )
                elif maxAppear == b : insert( a,b-1,c , string+'b' , lastTwo= lastTwo[1] + 'b' )
                elif maxAppear == c : insert( a,b,c-1 , string+'c' , lastTwo= lastTwo[1] + 'c' )
                
        
        insert(a,b,c, '' , '  ' )
        return solution 
            
S = Solution()
print(S.longestDiverseString(7,1,0))    
        
            