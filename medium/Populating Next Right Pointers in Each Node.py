from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


""" 
    思路: 
        此題基本上就是階層尋訪 , 把相同層的用一個next串在一起 ,最後返回已經串好next的原始root
        , 我寫兩種作法來玩 
        1. 記錄錄深度保存分level節點 ,接著後處理串接
        (1的變化型). 只保存每個深度前一個節點 , 並且在遞迴過程當場串接
        2. BFS直接操作 , 

"""


""" 
    解法一. 分層紀錄後操作  
    
        --> 速度空間都不優 , 空間上我們用dict存內容為O(n) 
        , 時間上遞迴O(n) ,後處理O(n),感覺時間問題更像是LeetCode這一波剛好比較慢
        
"""
class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        
        # 我們定義depth=1為root
        self.levelTable = dict() 
        self.depth = 0 
        
        
        # 在pre-order , post-order的位置操作深度 , 
        # 更新level-table的時機基本上是都可以 , 在此就在in-order部份更新 
        def traverse(node): 
            if node is None : return 
            
            self.depth += 1
            traverse(node.left) 

            if self.depth in self.levelTable : 
                self.levelTable[self.depth].append(node)
            else :
                self.levelTable[self.depth] = [node]
            
            traverse(node.right)
            self.depth -= 1
        
        # 執行遞迴,拿到階層表self.leveltable , 紀錄每一個深度的節點由左到右的內容
        traverse(root)
            
        # 接下來就依層取出 , 走一個內迴圈把所有的next接上即可 
        for sameLevel in self.levelTable.values() : 
        
            # 如果該層只有一個節點(root) , 那就下一層 , 因為預設節點的next就是None
            if len(sameLevel) == 1: continue                
            
            # sameLevel內保存了相同階層的節點 , 並且由左到右 
            for node_idx in range( len(sameLevel)-1 ):  
                sameLevel[node_idx].next = sameLevel[node_idx+1]
        
        return root
                
""" 
    解法二. 改良解法一,我們只存各階前一個node , 大幅來減少空間複雜度到O(h) 
    
    --> 速度跟時間都有大幅成長 , 這個算法就相當優了
"""

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        
        # 我們定義depth=1為root
        self.levelTable = dict() 
        self.depth = 0 
        
        # 在pre-order , post-order的位置操作深度 , 
        def traverse(node): 
            if node is None : return 
            self.depth += 1
            traverse(node.left) 
            if self.depth in self.levelTable: 
                self.levelTable[self.depth].next = node 
                self.levelTable[self.depth] = node 
            else : 
                self.levelTable[self.depth] = node
            traverse(node.right)
            self.depth -= 1
        
        traverse(root)
        
        return root 
    
""" 
    解法三. BFS  , 每一次在for-loop裡面都是拿出同一階層的節點  
    --> 速度和空間有略好一解法一 , 不如解法二 , 但可能還有優化空間
"""

from collections import deque

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        
        if root is None : return 
        
        self.queue = deque()
        self.queue.append(root) 
        
        # 當queue還有節點要尋訪
        while self.queue : 
            # 取得這一層的節點數量 , 好讓待會用for-loop去尋訪同一層節點
            sameLevelSize = len(self.queue) 
            
            
            # 依照這一層的節點數sameLevelSize , 來尋訪
            for i in range(sameLevelSize-1) : 
                
                # 將同一層節點的child依序放入queue中
                node = self.queue.popleft()
                # 把next設置為同一層下一個節點
                node.next = self.queue[0]
                
                
                if node.left  : self.queue.append(node.left)
                if node.right : self.queue.append(node.right) 
            
            #最後一個節點我們要手動加入他的child , 因為我們不能動到他的next 
            node=self.queue.popleft() 
            
            if node.left  : self.queue.append(node.left)
            if node.right : self.queue.append(node.right) 
        
        return root
                

"""
    解法四.    
        將整棵tree當作三元樹 , 這個三元樹的root是原先root的兩個child作為root
        注意這一題有給定我們的tree是complete binary tree , 因此只要有child就必定是左右都有
    
"""

class Solution:

    def connect(self, root: Optional[Node]) -> Optional[Node]:

        
        def traverse(nodeLeft , nodeRight): 
            
            if nodeLeft is None : return None 
            
            # pre-order位置將左節點連接到右節點 
            nodeLeft.next = nodeRight
            
            traverse(nodeLeft.left , nodeLeft.right)
            traverse(nodeLeft.right, nodeRight.left)
            traverse(nodeRight.left , nodeRight.right)
    
        # 如果root是空的就直接返回就滿足題目要求
        if root is None : return root 
    
        # root的child才是這一棵三元樹的root            
        traverse(root.left , root.right)
            
        return root