""" 
    題意 :  
        這一題蠻特別的,給定公司有n個員工 , 每個員工都有一個直屬的manager ,同時有一個最大的員工head , 
        接下來訊息要從head開始散播 , head所散播的內容會使用 informTime[headId]的時間 傳撥給所有以headId
        作為manager的員工 , 而員工拿到消息後就可以馬上開始繼續散播 , 已知員工的關係一定是tree structure
        
    思路 : 
        這一題我自己是覺得有點像backtrack的展開那般 , 但應該可以直接DFS/BFS , 只是要連同"當下的時間一同存入"
        比較麻煩的應該是要找每個節點的child有誰 , 而這件事情我認為直接建立一個dict會快 , 在題目給定的條件下
        一個node一定只會有一個parent ,因此我們靠著表 , 從root開始就可以run DFS , 並一同把當前累積時間放入stack
        每一個DFS到底後就要統計一下總時間並更新最大時間

"""
from typing import List 


""" 
    解法一. 
        按照上面的思路, 針對manager的關係建立一個dict , 接著使用DFS 
        解的時間空間都很優秀 , 我自己覺得這一題解的也挺漂亮
        
"""
class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        solution = float("-inf")
        
        # 根據manager的關係建立關聯表 , 方便快速查詢
        relationship = dict() 
        for employeeID , managerID in enumerate(manager) : 
            # 跳過headID , 因為headID沒有parent (manager)
            if employeeID == headID : continue 
            
            if managerID in relationship : 
                relationship[managerID].append(employeeID) 
            else : 
                relationship[managerID] = [ employeeID ] 
                
        
        # 準備帶有時間的stack , 保存當前節點與目前累計時間 
        # cause it's tree structure , so we don't need the visited array to keep the traverse progress
        stack = list() 
        stack.append(   (headID , 0) ) 

        while stack :  
            
            employeeID , accTime = stack.pop() 
            
            # 檢查該node是否有下屬 , 如果沒有了就更新目前最大時間 
            if not employeeID in relationship : 
                solution = max(solution , accTime) 
            
            # 如果有下屬代表這還需要進一步傳遞 , 加上傳遞時間後繼續放回stack
            else : 
                
                accTime = accTime + informTime[employeeID]
                
                for subordinatesID in relationship[employeeID] : 

                    stack.append( (subordinatesID , accTime) )
                
        
        return solution
        

S = Solution() 
sol = S.numOfMinutes(
    # n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    n = 1, headID = 0, manager = [-1], informTime = [0]
)
      
print(sol)  