""" 
    思路 : 
        這一題實際上從題目給的資料範圍來看就能大致看出無法使用backtrack , 
        而這一題的觀察也比較特殊 , 去思考一個完整的Square有什麼樣的特性 
        
        令DP-table dp[i][j] 代表 "以i,j為正方形右下角時可以得到的最大正方形"   
        
        而這個性質 , 如果 matrix[i][j] == 0 , 那dp[i][j] = 0
        而 matrix[i][j] == 1 時 , 其可以構成的最大正方形邊長會與他左上 ,左邊與正上所能構成的正方形中的邊長最小值再 +1
        
        
        

"""
from typing import List 
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        best = 0 
        height , width = len(matrix) , len(matrix[0]) 
        dp =  [ [0 for i in range(width)] for j in range(height) ]
        
        for i in range(height): 
            
            for j in range(width): 
                
                if i==0 :
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0             
                elif j == 0 : 
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0 
                
                else : 
                    if matrix[i][j] == "1" : 
                        dp[i][j] = 1 + min(
                            dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1] 
                        )

                # 更新目前看到的最大正方形
                best = max(best , dp[i][j]) 
        
        # 注意best是邊長 , 而題目要面積
        return pow(best , 2 ) 