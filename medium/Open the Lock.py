from typing import List 

""" 
    思路: 
        此題為書本示範BFS的第二題 , 較為進階且加入了限制條件。 
        
        給定一組4位數轉盤 , 每一位可以顯示0-9 , 共10個數字 
        假設給定一組目標數字target , 並且從0000開始 , 最少要轉幾步才能到達target?
        同時此題還加入了 deadends 列表 , 代表著不能被轉到的數字
        
        - 我們先假設沒有deadends這個拘束 , 單純考慮原始問題。  
            我們的起始位置為0000 , 每一次只能轉動一個號碼盤 ,"並且轉動指的是往上或往下一格"
            如此一來在0000,我們實際上有8個動作(每個位置往上或往下)的選擇 , 
            
            --> 我們就能以此建構一個graph ,每個node有8個鄰居 , 此時這個問題就可以透過簡單的BFS框架解了
"""

""" 
    我們先就上面的作法依據概念自己手刻python版本的BFS大致框架
"""


from collections import deque
class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        if target == "0000" : return 0        

        queue = deque()  
        queue.append("0000") 
        step = 0 
        
        
        # 輔助函數 , 用來轉動玻盤
        def moveUp(num , pos):
            num = list(num) 
            num[pos] =  "0" if int(num[pos]) == 9 else str(int(num)+1) 
            return "".join(num)
        
        def moveDown(num , pos): 
            num = list(num)
            num[pos] = "9" if int(num[pos]) == 0 else str(int(num[pos])-1)
            return "".join(num)
        
        
        while queue : 
            
            size = len(queue)  
            
            for i in range(size): 
                # 取出的節點 , 在其四個位置都有往上或往下的選擇可以做 , 因此每個節點有8個鄰居 
                node = queue.popleft() 
                
                # 找到目標 , 就可以直接返回了
                if node == target : return step 

                # 依序從第1到第4個位置轉動撥盤
                for i in range(4): 
                    queue.append( moveUp(node , i)  )
                    queue.append( moveDown(node , i))
            
            step += 1
                

""" 
    上面這個版本 , 已經完成了整個演算法的大致框架 , 但仍有幾個問題 
        -1.會產生死循環 , 我們沒有鎖住節點往回走的行為 , 這會導致BFS產生close-loop 
        -2.還沒有加入deadends , 因此會隨意的走
    只要解決第一個缺陷 , 這個演算法就能在沒有拘束的情況下計算從特定初始位置到任意目標位置的最短步數,
    不過以下就直接解決這兩個缺陷 , 因為在這一題中deadends只是一個不能進入的節點 , 
    代表我們不能基於deadends擴展 , 謹此而已 . 
    
    note : 
    對於deadends , 我認為取鄰節點時發現為deadend ,不放入queue / 從queue拿出來發現是deadend後跳過
    兩者應該是一樣的 , 下面實做拿出來後發現是deadend再處理跳過 , 程式碼比較清晰 
    ( 對於visted 也是一樣 )
"""

from collections import deque
class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        if target == "0000" : return 0        

        queue = deque()  
        queue.append("0000") 
        # 我們用集合來保存拜訪過的節點以及deadends , 這樣在查找上快上很多 
        visted = set() 
        deadends = set(deadends) 
        step = 0 
        
        # 輔助函數 , 用來轉動玻盤
        def moveUp(num , pos):
            num = list(num) 
            num[pos] =  "0" if int(num[pos]) == 9 else str(int(num[pos])+1) 
            return "".join(num)
        
        def moveDown(num , pos): 
            num = list(num)
            num[pos] = "9" if int(num[pos]) == 0 else str(int(num[pos])-1)
            return "".join(num)
        
        
        while queue : 
            
            size = len(queue)  
            
            for i in range(size): 
                # 取出的節點 , 在其四個位置都有往上或往下的選擇可以做 , 因此每個節點有8個鄰居 
                node = queue.popleft() 
                
                # 檢查拿出來的node是否在deadends或visted內 , 是的話就可以跳過了
                if node in visted : continue 
                if node in deadends : continue
                visted.add(node)
                
                # 找到目標 , 就可以直接返回了
                if node == target : return step 

                # 依序從第1到第4個位置轉動撥盤
                for i in range(4): 
                    queue.append( moveUp(node , i)  )
                    queue.append( moveDown(node , i))
            
            step += 1
        
        return -1 
    

""" 
    實做一個版本 , 除了上面的功能還能額外返回轉到目標的軌跡 , 只要將visted改為dict用來紀錄 ,
    同時把visted的更新放到探索,擴展節點時 . 
"""

from collections import deque
class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        if target == "0000" : return 0        

        queue = deque()  
        queue.append("0000") 
        visted = dict() 
        deadends = set(deadends) 
        step = 0 
        
        # 輔助函數 , 用來轉動玻盤
        def moveUp(num , pos):
            num = list(num) 
            num[pos] =  "0" if int(num[pos]) == 9 else str(int(num[pos])+1) 
            return "".join(num)
        
        def moveDown(num , pos): 
            num = list(num)
            num[pos] = "9" if int(num[pos]) == 0 else str(int(num[pos])-1)
            return "".join(num)
        
        
        while queue : 
            
            size = len(queue)  
            
            for i in range(size): 
                # 取出的節點 , 在其四個位置都有往上或往下的選擇可以做 , 因此每個節點有8個鄰居 
                node = queue.popleft() 
                
                # 檢查拿出來的node是否在deadends或visted內 , 是的話就可以跳過了
                if node in deadends : continue 
                
                # 找到目標 , 除了返回步數,還可以返回軌跡
                if node == target : 
                    trajectory = list() 
                    trajectory.append(node)
                    while not node == "0000": 
                        node = visted[node]
                        trajectory.append( node ) 
                        
                    trajectory.reverse()
                    # 打印出從0000到目標的軌跡
                    print(trajectory)
                    return step 

                # 依序從第1到第4個位置轉動撥盤
                for i in range(4): 
                    upNode = moveUp(node,i) 
                    if not upNode in visted : 
                        visted[upNode] = node
                        queue.append(upNode)                        
                    
                    downNode = moveDown(node , i )                     
                    if not downNode in visted: 
                        visted[downNode] = node 
                        queue.append(downNode)
            
            step += 1
        
        return -1 