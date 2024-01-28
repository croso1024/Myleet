from typing import List 
""" 
    思路: 
        這一題有點小複雜 , 給定一個directed graph , 共有n個節點並從0到n-1被編號 , 
        所有個節點最多只有一條outgoing edge , 或是沒有往外的edge . 
        給定一個array edge , edge[i]代表了第i個節點指向的節點 , edge[i]=-1代表該節點沒有outgoing edge  
        另外給定node1, node2 , 我們要去找到一個節點
        
        他可以從node1到達也可以從node2到達 , 並且滿足 min(  max(node1->dst , node2->dst)  )
        note : 題目告知graph中可能包含了cycle
        
        這一題直覺思路可能就是走BFS , 由node1,node2個別擴張一次 , 紀錄下他們可以達到的節點與距離 
        這邊需要的BFS每次需要O(N) ,
        
        接著traverse一次所有節點 , 透過前一步BFS紀錄的內容來找最佳解

"""

""" 
    解法一. 
        follow上述的思路 , 其實答案的時間與空間都很不錯 , 
        我想應該還存在些微優化空間 , 但基本上time/space complexity應該就是BFS框架的O(N)了

"""
from collections import deque
class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        
        def BFS(src) :
            queue = deque() 
            visited = dict() 
            
            queue.append(src)
            visited[src] = 0  
            step = 1
            while queue : 
                
                size = len(queue) 
                
                for _ in range(size): 
                    
                    cur_node = queue.popleft() 
                    # 因為一個節點最多只有連接到另一個節點
                    next_node = edges[cur_node]
                    
                    if next_node != -1 and not next_node in visited: 
                        queue.append(next_node)
                        visited[next_node] = step                     
                
                step += 1 
                
            return visited

        node_map1 = BFS(node1) 
        node_map2 = BFS(node2) 
        
        # 接下來要開始找node1,node2都能到達的節點 , 並計算最佳解
        best_index = -1 
        best_value = float("inf")
        
        for i in range(len(edges)):  
            
            if i in node_map1 and i in node_map2 : 
                obj = max( node_map1[i] , node_map2[i] )
                if obj < best_value : 
                    best_value = obj 
                    best_index = i 
        
        return best_index
                
                 
            
            
