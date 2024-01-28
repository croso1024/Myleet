""" 
    思路 :  
        這一題要我們將給定的Matrix中, 四周完全被"X"包圍的"O" 翻轉為"X" , 這個四周包圍的定義不是只是單一塊的四周不要全都是"X" ,
        可以看範例 , 一塊被包在"X"中的孤島也要被翻轉
        實際上唯一安全的部份是"邊緣" , 只有能夠連通到邊緣的O是安全的 
        
        所以我的直觀想法是這樣 : 
        
        就針對Matrix的四個邊緣所有"O"展開DFS / BFS , 把可以連通得索引放進一個set 
        走完之後 , 所有不在安全區域的索引全都翻成"X"就可以了
                
"""

""" 
    解法一. DFS 走邊緣 
    速度和空間都非常優 , 就是程式碼寫得有點繁雜
"""

from typing import List 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        Stack = [] 
        m,n = len(board) , len(board[0]) 

        # 如果有一邊長度是<=2 , 那不可能被包圍而翻轉
        if m<=2 or n<=2 : return board 
        
        # 避免走回頭路
        Complete = set() 
        # Safe是用來保存安全區的索引 , 可以留在"O"
        Safe = set() 
        
        # 我們可以先把所有在邊緣的"O"放進Stack再開始 
        for i in range(m): 

            if board[i][0] == "O" : 
                Stack.append((i,0)) 
                Complete.add((i,0)) 
                Safe.add((i,0)) 
            
            if board[i][n-1] == "O": 
                Stack.append((i,n-1)) 
                Complete.add((i,n-1)) 
                Safe.add((i,n-1))

            if i == 0 or i == m-1 :     
                for j in range(1,n-1) : 
                    if board[i][j] == "O" :
                        Stack.append((i,j))
                        Complete.add((i,j))
                        Safe.add((i,j))
        
        while Stack : 
            
            cur_i, cur_j = Stack.pop()
            
            # 檢查四個方向 , 繼續做DFS 
            
            # 檢查上面 
            if cur_i - 1 >= 0 and board[cur_i-1][cur_j] == "O" and not (cur_i-1,cur_j) in Complete: 
                Stack.append((cur_i-1,cur_j)) 
                Complete.add((cur_i-1,cur_j))
                Safe.add((cur_i-1,cur_j))

            # 檢查下面 
            if cur_i + 1 < m and board[cur_i+1][cur_j] == "O" and not (cur_i+1,cur_j) in Complete: 
                Stack.append((cur_i+1,cur_j)) 
                Complete.add((cur_i+1,cur_j))
                Safe.add((cur_i+1,cur_j))
                
            # 檢查左邊 
            if cur_j - 1 >= 0 and board[cur_i][cur_j-1] == "O" and not (cur_i,cur_j-1) in Complete: 
                Stack.append((cur_i,cur_j-1)) 
                Complete.add((cur_i,cur_j-1))
                Safe.add((cur_i,cur_j-1))

            # 檢查右面 
            if cur_j + 1 < n and board[cur_i][cur_j+1] == "O" and not (cur_i,cur_j+1) in Complete: 
                Stack.append((cur_i,cur_j+1)) 
                Complete.add((cur_i,cur_j+1))
                Safe.add((cur_i,cur_j+1)) 
            
        # 走到這裡 , Safe保存的就都是滿足的解 
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == "O" and not (i,j) in Safe:
                    board[i][j] = "X" 
            
        
        return board 
                
""" 
    解法二. DFS , 不過修正了四方向探索 , 以及一開始把節點預先放入Stack的步驟 
    空間大幅度提高 , 可讀性也比較好 , 但因為判斷更加複雜 , 速度有掉
"""
from typing import List 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Stack = [] 
        m,n = len(board) , len(board[0]) 

        # 四方向尋訪列表
        sup = [ [0,1] , [0,-1] , [1,0] , [-1,0] ]
        
        # 如果有一邊長度是<=2 , 那不可能被包圍而翻轉
        if m<=2 or n<=2 : return board 
        
        # 避免走回頭路
        Complete = set() 
        # Safe是用來保存安全區的索引 , 可以留在"O"
        Safe = set() 
        
        for i in range(m): 
            for j in range(n) :  
                # 如果該點是"O" , 並且索引上他在邊緣 , 才可以加入Stack展開
                if board[i][j] == "O" and  (i==0 or i==m-1 or j==0 or j==n-1) and not (i,j) in Complete :   
                    Stack.append((i,j)) 
                    Complete.add((i,j))
                    Safe.add((i,j)) 
                    
                # 展開以剛剛找到的那個點為首的DFS 
                while Stack : 
                    
                    cur_i , cur_j  = Stack.pop() 
                    
                    for dir in sup : 
                        x = cur_i + dir[0]
                        y = cur_j + dir[1] 
                        if  ( 0 <= x < m and 0 <= y < n ) and board[x][y] == "O" and not (x,y) in Complete : 
                            Stack.append((x,y))  
                            Complete.add((x,y))
                            Safe.add((x,y)) 
        for i in range(m):
            for j in range(n) : 
                
                if board[i][j] == "O" and not (i,j) in Safe:                
                    board[i][j] ="X" 
                    
        
                        
                        
                    
                