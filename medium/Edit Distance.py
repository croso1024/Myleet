""" 
    思路: 
        給定兩個字串 s1 , s2  我們可以針對s1進行插入/刪除/替換 , 求把s1轉成s2最少需要幾步

        同樣是兩個字串的DP問題 , 比較能直覺的想到DP-table會是考慮在
        s1[0:i] , s2[0:j] 的情況下的Edit distance .
        
        書本在介紹這一題的時候,首先是以top-down的思路來考慮 ,即從兩邊都是滿字串開始考慮 , 
        一步步縮小問題的規模 . 
        
        由後往前 , 
        
        A. 如果指向的字元相同 , 那代表不需要編輯繼續往前
            而如果有一個字串較短而先走完 :
            
            1. s1先走完 -> 要把s2剩餘的字元插入到s1 
            2. s2先走完 -> 要把s1剩餘的字元都刪除
        
            這個走完的情況就是演算法的base case
            
        B. 指向的字元不同 , 那就是要修改字元讓他們相同了 , 因為題目給定的操作不會讓我們更換順序
            否則允許我們做swap的話難度就爆表
            
            如果遇到不同 , 那最佳解會在這兩種case中 
            1. 老實把s1不同的改成s2 , 即 1 + 繼續比較後面edit distacne 

            2. 說不定s1下一個值能夠對應s2 , 那就先跳過(但後面還是要刪除) 
               因此也要 1 + 跳過s1這個值,s2不變的edit distacne

            3. 插入那個缺少的值後繼續比較 , 即 1 + s1不動 , s2可以走到下個值的edit distance 

"""

""" 
    解法一. 
        先做top-down的遞迴 , 按照上述的邏輯來完成
        但這個作法沒有memo , 所以我沒有拿去提交 , 因為感覺會Time limit exceeded
    
"""

class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
    
        
        # dp函數的定義為返回字串 s1[0:i] 和 s2[0:j] 的最小編輯距離 ,
        # 注意這邊的i,j如同上面所示的 list slice , 為開放區間
        def dp(i,j) : 
            
            # base case - 1 : s1 字串已經空了 , 那就是把s2剩餘的全部插入到s1
            # base case - 2 : s2字串先空 , 把s1剩餘的全部刪除
            # base case - 3 : s1 s2同時都是空的 , 那就是0 
            
            # 集中成下面的這個 case 
            if i==0 or j==0: 
                return i if i!=0 else j  
            

            # 如果兩個字就是一樣的 , 那就不需要做操作 , 繼續往前看
            if word1[i-1] == word2[j-1] : 
                return dp(i-1,j-1)  

            # 兩個字不一樣的時候 , 就會需要做修改或跳躍 
            # 此時有三種選擇分支 

            # 1. 就老實做修改 , edit distance + 1 
            # 2. 先不要修改 , 跳過一格 , 說不定s1的下一個就是我們要的 , 
            # 但edit distance還是要+1來反應最後刪掉這個我們跳過得 

            else : 
                # 分別對應修改 , 刪掉s1元素繼續比 
                return 1 + min( dp(i-1,j-1) , dp(i-1,j) , dp(i,j-1) ) 
        
        return dp(len(word1) , len(word2)) 
    
    
"""
    解法二. top-down遞迴加上memo  
    
    --> 這個解法在速度和空間上就非常優勢了 , 

    而且top-down的優勢還是在於只要理清每個狀態下可以做的選擇(動作) , 加上memo
    就不太需要考慮到說遞推dp-table的順序
"""

class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = dict() 
        
        def dp(i,j,memo): 
            
            if i == 0 or j==0: return i if i!=0 else j 
                
            elif (i,j) in memo : return memo[(i,j)] 
            
            else : 
                
                if (word1[i-1] == word2[j-1]) :  
                    
                    result = dp(i-1, j-1 , memo) 
                
                else : 
                    
                    result =  1 + min(
                        dp(i-1, j-1 ,memo) , # 修改s1 , 繼續比較 
                        dp(i-1 ,j ,memo) ,   # 跳過(其實就是直接刪除)該s1元素 , 繼續比較 
                        dp(i,j-1 , memo)     # 插入新元素在s1 , 繼續比較 
                        
                    )


            memo[(i,j)] = result 
            return result 
    
        return dp(len(word1) , len(word2) , memo)
    

""" 
    解法三. Bottom-up 遞推

    根據我們上面top-down的寫法其實很明顯了 , 一個二維的DP table ,
    計算特定位置 dp[i][j]的值當方式為 
    
    Case.1  word1[i-1] == word2[j-1] : 
        dp[i][j] = dp[i-1][j-1] 
    
    Case.2  word1[i-1] != word2[j-1] : 
        dp[i][j] = 1 + min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1]) 

    !! 建議還是畫一張表出來 , 可以更加直觀的清楚以推進方式來解的思考過程. 
    
    同樣的這一題也是會考慮到空字串 , dp-table的大小為 len(word1)+1  x len(word2)+1 
    
    另外base case也不太一樣  , dp[0][j] = j  , dp[i][0] = i 
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [ [None for j in range(len(word2)+1)]  for i in range(len(word1)+1) ]
        
        
        for i in range(  len(word1) +1  ):
            
            for j in range( len(word2) + 1 ): 
                
                if i == 0 : dp[i][j] =  j 
                elif j == 0 : dp[i][j]  = i  
                
                else : 
                    
                    if word1[i-1] == word2[j-1] : 
                        # return 左上 
                        dp[i][j] = dp[i-1][j-1]
                    else : 
                        
                        dp[i][j] =  1 + min(
                            dp[i-1][j-1],
                            dp[i-1][j], 
                            dp[i][j-1] 
                        )
        
        return dp[len(word1)][len(word2)]
    
""" 
    解法四. 
        就是解法3, 只是base case不再到主要的雙迴圈判斷 , 這樣比較多步驟 
        改成單獨出來計算base case , 可以有效提昇一些速度
"""
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [ [None for j in range(len(word2)+1)]  for i in range(len(word1)+1) ]
        
        
        for i in range( len(word1)+1 ): dp[i][0] = i 
        for j in range( len(word2)+1 ): dp[0][j] = j 
            
        
        for i in range( 1 , len(word1) +1  ):
            
            for j in range( 1, len(word2) + 1 ): 
                
                if word1[i-1] == word2[j-1] : 
                    # return 左上 
                    dp[i][j] = dp[i-1][j-1]
                else : 
                    
                    dp[i][j] =  1 + min(
                        dp[i-1][j-1],
                        dp[i-1][j], 
                        dp[i][j-1] 
                    )
        
        return dp[len(word1)][len(word2)] 


S = Solution()
print(S.minDistance("video" , "record"))