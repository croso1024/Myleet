""" 
    思路 : 
        這一題為東哥在Union Find 演算法的範例之一 ,
        這一題給定了許多變數的"相連"與"不相連"關係 , 而我們要判斷的就是這些變數是否是互相滿足邏輯
        
        從抽象的角度來看這一題可以想成我們要判斷兩個變數之間究竟有沒有連通關係 , 而這種情況就非常適合使用union-find演算法
        透過題目給定的連接關西將一個個數值串連起來進行判斷
"""


""" 
    Union-find 演算法
    Union-find 演算法需要實現的內容包含: 
        1. union(a,b) -> 將a和b進行連接 
        2. connect(a,b) -> 檢查a,b是否是相連的
        3. count -> 返回目前的連通個數(在這一題用不到)
"""
from typing import List 
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        class UnionFind: 
            # 給定節點塊的數量 , 進行初始化 
            def __init__(self ):
                # 初始狀態下所有節點的paraent都是自己 , 建立"a" 到 "z" 的節點forest
                self.parent = [ i for i in range(26) ] 
                # rank 用來判斷在union時 , 那一個tree要接在哪一個下 
                self.rank = [0 for i in range(26)]
            
            # 使用了路徑壓縮的技巧 , 觀察這個函式的語意
            # find本身是要找到自身的root , 如果自身的parent不是自己(只有root是自己) ,
            # 那就把自身的parent設定為root ,之後回傳
            def find(self,node): 
                if not self.parent[ node ] == node : 
                    self.parent[node] = self.find( self.parent[node] )
                return self.parent[node]     
            
            
            def union( self ,a , b ) : 

                # 這邊回傳的就是0-25的編碼了
                root_a = self.find(a) 
                root_b = self.find(b) 

                # 已經相連了
                if root_a == root_b : return 
                
                # 透過rank去判斷說誰要接在誰身上 
                # rank小的接在大的身上
                
                if self.rank[root_a] > self.rank[root_b] : 
                    self.parent[root_b] = root_a
                elif self.rank[root_a] < self.rank[root_b] : 
                    self.parent[root_a] = root_b 
                else : 
                    self.parent[root_a] = root_b 
                    self.rank[root_b] += 1 
                    
            # 如果相連 , 代表他們root相同
            def connect(self,a,b):                     
                root_a = self.find(a)
                root_b = self.find(b) 
                return True if root_a == root_b else False 
        
        # 開始實際處理這個演算法題
        UF = UnionFind() 
        
        # 先把所有應該要等於的union起來 
        for eq in equations : 
            if eq[1] == "=" : 
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                
                UF.union(a,b)
        
        for eq in equations : 
            
            # 他們應該要不等於, 但在Union Find中卻是相連 -> False
            if eq[1] == "!" : 
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if UF.connect(a,b) : return False 

        
        return True 
                
                
            