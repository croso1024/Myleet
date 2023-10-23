
""" 
    思路 :  
        這一題蠻直觀的是back track的問題 , 題目給定的matrix蠻小的且要找的目標字串也不長
        不過因為這一題給訂了target sequence , 所以也不是完全盲目的找 . 
        必須要在當前cell的周圍不斷的找對應的值 , 類似抵銷的概念 , 將當前word傳入 
        
        在展開的過程中需要確認當前走到的cell == word中剩餘的第一個字母 , 一直走到word為空
        這一題只有展開中有找到任一組就可以直接return 

"""

""" 
    解法一 . Backtrack 
        我這邊嘗試使用maintain一個hashset作為該展開分支已經走過的cell , 
        
        軌跡 : 這邊並不是尋常增加式的軌跡 , 而是使用遞減式的 (消除式)
        因此滿足動作空間的清單為節點的上下左右四個中, 不在hashset中並且等於當前軌跡第一個值的cell才能選
        
        定義backtrack參數 : 1. hashset , 支援做選擇與撤銷選擇 2. track , 要消除的內容     
        
        在加速的部份 , 保存一個外部變數在我們找到結果後可以提前撤出   
"""


from typing import List 

class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        solution = False 
        
        def backtrack( i,j, hashset :set , track:list ) :
            nonlocal solution
            if not track : 
                solution = True  
                return 
            # 檢查上下左右的範圍 , 確認不在hashset,並且可以消除track的話就展開
            # 檢查上面 
            if (i-1 >= 0) and (not (i-1,j) in hashset ) and (board[i-1][j] == track[0]): 
                hashset.add( (i-1,j) ) 
                backtrack(i-1,j , hashset , track[1:])
                hashset.remove((i-1,j))
            # 檢查下面 
            if (i+1 < len(board)) and (not (i+1,j) in hashset ) and (board[i+1][j] == track[0]): 
                hashset.add( (i+1,j) ) 
                backtrack(i+1,j , hashset , track[1:])
                hashset.remove((i+1,j))

            # 檢查左邊
            if (j-1 >= 0) and (not (i,j-1) in hashset ) and (board[i][j-1] == track[0]): 
                hashset.add( (i,j-1) ) 
                backtrack(i,j-1 , hashset , track[1:])
                hashset.remove((i,j-1))
            
            # 檢查右邊
            if (j+1 < len(board[0])) and (not (i,j+1) in hashset ) and (board[i][j+1] == track[0]): 
                hashset.add( (i,j+1) ) 
                backtrack(i,j+1 , hashset , track[1:])
                hashset.remove((i,j+1))
    
    
        Table = set() 
        
        for i in range(len(board)):
            for j in range(len(board[0])) : 
                if solution : return True 
                if board[i][j] == word[0] : 
                    Table.add((i,j))
                    backtrack(i,j , Table, word[1:] )
                    Table.remove((i,j))
                    
        return solution