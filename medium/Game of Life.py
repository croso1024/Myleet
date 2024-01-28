""" 
    思路 : 
    
        本題給定一個 m x n 的board , 板子上的數值 0/1代表格子生死  (0:死 , 1:活)
        follow以下的規則 , neighbor 的定義是每個格子的周圍8格 
        1. 對於活著的格子,除非他的鄰居只有2,3個活著 , 否則下一輪他就掛
        2. 對於死掉的格子,若他周圍有三個鄰居是活的 , 下一輪就會活

        注意死跟活是可以同時發生 .
        
        
        這一題最暴力解法就是一個function去檢查鄰居 , 確認鄰居的生死數後去操作 , 這樣take O(MxN) 
        注意這一題要in-place的操作 , 所以難點在於我們如果提前更新board會導致後續判斷麻煩 
        
"""

""" 
    解法一. naive解法 , 
        就是先初始化一個ref array , 然後一個function判斷周圍八格去計算後填入ref_array
        這個作法在空間上不太優 , 速度上更差
"""
from typing import List 
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m , n  = len(board) , len(board[0])
        
        ref_array =  [  [0 for i in range(n)] for j in range(m) ]  
        
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1] ]
        
        # 判斷周圍八格有幾個活的值
        def live_neighbor(i,j) : 
            live = 0
            for dir in direction: 
                neighbor_i = i + dir[0] 
                neighbor_j = j + dir[1] 
                # 檢查其沒有超出index範圍
                if 0 <= neighbor_i < m  and 0 <= neighbor_j < n :  
                    if board[neighbor_i][neighbor_j] == 1 : live += 1 
            return live 
        for i in range(m): 
            
            for j in range(n): 
                # 對於死掉的格子來說 , 如果周圍剛好三個活 , 就可以翻轉
                if board[i][j] == 0  and  live_neighbor(i,j) == 3  : 
                    ref_array[i][j] = 1 
                    continue
                # 對於活著的格子來說 , 需要活鄰居剛好是2,3個
                if board[i][j] == 1 and  2<=live_neighbor(i,j)<=3 :  
                    ref_array[i][j] = 1 
                    continue
        # 計算得到ref_array , 做in-place的替換
        for i in range(m): 
            for j in range(n): 
                board[i][j] = ref_array[i][j]
        
        
""" 
    解法二. 加值解法 , 
        這邊使用加上浮點數的方式來做 , 走到一個 board[i][j] - 1 >= 0的位置 , 就在周圍8格+0.1 
        最終走完後 , 格子如果是1.2/1.3和0.3的留下 , 
        
        主要是解決說如果是+1 , 會在走到1的時候不曉得他是原本就為1,還是周圍鄰居幫他加到1的 , 因為一個值最多8個鄰居 ,
        故我的這個解法最多就是加到1.8
        
        這邊會遇到python的浮點數相加的小bug , 0.1+0.2 = 0.300000000000004 , 需要round function去解決
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
                
                
        m , n = len(board) , len(board[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1] ]
        for i in range(m): 
            for j in range(n): 
                # 如果是遇到原本就活的值 
                if board[i][j] >= 1 : 
                    # 在內部做鄰居的加值 
                    for dir in direction: 
                        neighbor_i = i + dir[0] 
                        neighbor_j = j + dir[1] 
                        # 檢查其沒有超出index範圍
                        if 0 <= neighbor_i < m  and 0 <= neighbor_j < n :  
                            board[neighbor_i][neighbor_j] += 0.1 
                # 遇到死值(<1)
                else : pass  
        
        # 接著把值等於1.2,1.3還有0.3當活的
        
        for i in range(m): 
            for j in range(n): 
                print(i,j , round(board[i][j],1) ) 
                if round(board[i][j] ,1) in [0.3 , 1.2 ,1.3] : 
                    board[i][j] = 1 
                
                else :
                    board[i][j] = 0


S = Solution()
S.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])