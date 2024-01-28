""" 
    思路 : 
        感覺這一題難度是有的 , 給定n個city , 以及n-1條edge , 求最少的修改次數(把單向edge翻轉) , 使得所有節點都能通到節點0
        我的直觀想法是BFS , 先不考慮edge是有向的(先當作雙向) , 就統計從0出發到所有節點的步數 , 以及到達每一個節點有多少步驟是走反向edge
        只要拿這個反向Edge集合的最大值就是解
        
        -> 問題一. 這個解法會有一個問題 , 就是如example1 , 從任何一個節點到0的路徑最多只需要2次修改 , 但實際上答案是3次 

"""



""" 
    解法一. 先不用考慮過多優化 , 依照上面的概念去解出一個版本再說 

        這個解法會有上述的問題一
"""
from typing import List 
from collections import deque 
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # 單向的graph ( 原始graph ),因為只是要查找 , 用set()效率高 
        adajency_list = [set() for i in range(n)]
        # 雙向的graph , 用來traverse neighbor 
        graph = [[] for i in range(n)] 

        for (ai,bi) in connections: 
            adajency_list[ai].add(bi) 
            graph[ai].append(bi)
            graph[bi].append(ai) 

        Queue = deque() 
        # 因為我們主要使用雙向graph進行BFS , 還是需要visited set來避免回頭
        # 另外因為BFS的特性 , 我們在看到某個節點時一定是在最短路徑上看到 ,因此我這邊使用hashmap
        # 除了保存下已經拜訪過以外 , 也保存走到這個節點時 "經過的反向道路數"
        visited = dict() 
        Queue.append(0) 
        visited[0] = 0 
        
        while Queue : 
            
            size = len(Queue) 
            
            for i in range(size): 
                
                cur_node = Queue.popleft() 
                
                # neighbor 是無視方向可以走到的節點
                for neighbor in graph[cur_node] : 
                    # 如果是還沒有走到過得節點 , 就可以加進Queue , 同時更新hashmap 
                    if not neighbor in visited : 
                        Queue.append(neighbor) 
                        # 如果走到這個neighbor , 路徑是順向的 , 那就不用動
                        # 否則為了走到這個節點需要修改的路徑要+1 
                        if neighbor in adajency_list[cur_node] : 
                            visited[neighbor] = visited[cur_node] 
                        else : 
                            visited[neighbor] = visited[cur_node] + 1                 
        
        # 當我們走完整張Graph , visited內的最大值就是需要修改的次數
        return max(visited.values())
        


""" 
    解法二.
        BFS 
        寫完解法一後的感覺 , 因為這一題給定了 n個節點與n-1條edge , 實際上不會有cycle , 
        我們可以再擴展的路上每次遇到需要反轉的就增加外部變數
        
        這個解法的速度與空間都很優
"""
from typing import List 
from collections import deque 
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # 單向的graph ( 原始graph ),因為只是要查找 , 用set()效率高 
        adajency_list = [set() for i in range(n)]
        # 雙向的graph , 用來traverse neighbor 
        graph = [[] for i in range(n)] 

        for (ai,bi) in connections: 
            adajency_list[ai].add(bi) 
            graph[ai].append(bi)
            graph[bi].append(ai) 

        Queue = deque() 
        # 因為我們主要使用雙向graph進行BFS , 還是需要visited set來避免回頭
        # 另外因為BFS的特性 , 我們在看到某個節點時一定是在最短路徑上看到 ,因此我這邊使用hashmap
        # 除了保存下已經拜訪過以外 , 也保存走到這個節點時 "經過的反向道路數"
        visited = set() 
        Queue.append(0) 
        visited.add(0)
        
        sol = 0 
        
        while Queue : 
            
            size = len(Queue) 
            
            for i in range(size): 
                
                cur_node = Queue.popleft() 
                
                # neighbor 是無視方向可以走到的節點
                for neighbor in graph[cur_node] : 
                    # 如果是還沒有走到過得節點 , 就可以加進Queue , 同時更新hashmap 
                    if not neighbor in visited : 
                        Queue.append(neighbor) 
                        visited.add(neighbor)  
                        
                        # 如果這條路實際上是反向的 , 我們就要增加修路次數1
                        # 注意這裡的反向 , 我們是從0開始擴展BFS , 但在題目意思上 , 我們要的是指向0 
                        if  neighbor in adajency_list[cur_node] :
                            sol += 1 
        
        return sol 
    
    
    

""" 
    解法二.
        DFS , 因為這一題n節點 n-1 edge的特性 , 基本上DFS也是走最短路徑 , 所以這題可以用DFS
        
        解法的速度與空間和BFS差不多 , 都很好
"""
from typing import List 
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adajency_list = [set() for i in range(n)]
        graph = [[] for i in range(n)] 

        for (ai,bi) in connections: 
            adajency_list[ai].add(bi) 
            graph[ai].append(bi)
            graph[bi].append(ai) 

        Stack = [] 

        visited = set() 
        Stack.append(0) 
        visited.add(0)
        
        sol = 0 
        
        while Stack : 
            
            cur_node = Stack.pop() 
                        
            for neighbor in graph[cur_node] : 
                if not neighbor in visited : 
                    Stack.append(neighbor) 
                    visited.add(neighbor)  
                    
                    if  neighbor in adajency_list[cur_node] :
                        sol += 1 
        
        return sol 
        