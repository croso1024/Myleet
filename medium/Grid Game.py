""" 
    題意:
        給定一個 2 x n 的 matrix , matrix[i][j]代表走到這格的分數 , 現在有兩台robot在走這個matrix
        機器人都只能往右或下走 , 第一台機器人走過得cell分數將會變為0 .
        
        兩台機器人都從 (0,0)出發要走到 (1,n-1) , 第一台機器人的目標是要'最小化'第二台機器人的得分 , 
        第二台機器人的目標則是要最大化自己的得分
        
    思路 :
        因為這一題的matrix實際上形狀為 2 x n , 因此第一台機器人的移動路線不外乎 Z字形狀或在兩端的L形狀
        直覺地可以去算第一台機器人會走他能拿到最高分的路線 , 
        但實際可以簡單的舉例得知 , 第一台機器人不一定要走最高分的路線來壓低第二台機器人. 
        
        反而應該是計算 "當機器人1走到終點 ,其路徑變為0後 , 剩下格子的總和" 
        仔細思考 L形與Z字型可以走得範圍 , 可以知道我們就是要計算兩row各自prefix sum 
        特別的點在於 first row的prefix sum要從 n-1 累加到 1 , second row的prefix sum則較為正常是 0 -> n-2
        算出prefix sum後就可以開始看怎樣的組合分數最高
        
"""

from typing import List 
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        size = len(grid[0])
        fr_prefix = [0 for i in range(size) ]
        sr_prefix = [0 for i in range(size) ]
        
        # 填充fr_prefix 
        acc = 0 
        for i in range(size):
            acc += grid[0][i] 
            fr_prefix[i] = acc  
        
        # 填充sr_prefix 
        acc = 0 
        for i in range(size): 
            acc += grid[1][i] 
            sr_prefix[i] = acc
        
        # 接著來算所有第二台機器人可能拿到的成績 , 從中選擇最小的
        scores = float("inf")
        # i代表機器人1是在第i格往下走 
        for i in range(size) :
            
            if i == 0 : 
                scores = min( fr_prefix[size-1] - fr_prefix[i]  , scores )
            elif i == size - 1 : 
                scores = min( sr_prefix[size-2] , scores ) 
            else : 
                scores = min(  

                        max( fr_prefix[size-1] - fr_prefix[i] , sr_prefix[i-1]   ) , scores 
                    
                        )
        
        return scores
            
            
            