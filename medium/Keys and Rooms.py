""" 
    思路: 
        這一題也是有趣的BFS , 給定一堆房間 , 只有房間0可以直接進去 , 
        其他每個房間都需要有鑰匙 , 而鑰匙也就放在這一些房間內 , 
        每個房間可能不只有一個鑰匙  ,而且我想這些鑰匙也有可能有重複的
        
        求問是否能到達所有房間
        
        這一題就是很直觀的DFS , 感受上應該蠻簡單的
"""



""" 
    解法一. DFS ,用一個visited 來maintain已經走過的房間 , 
        每次走到一個新房間就把還沒取得過得鑰匙拿起來 , 並把拿過鑰匙的房間標記到visited
        
        速度上普通,但空間上蠻不錯的
        
"""
from typing import List 

class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        stack = list() 
        visited = set()
        
        # 第0個房間不需要鑰匙 
        stack.append(0) 
        visited.add(0) 
        
        while stack : 
            
            key = stack.pop()
            room = rooms[key] 
            
            # 遍瀝該房間的所有鑰匙
            for next_key in room : 
                
                if not next_key in visited : 
                    stack.append(next_key) 
                    visited.add(next_key) 
        
        return len(visited) == len(rooms)
        
        
        
        