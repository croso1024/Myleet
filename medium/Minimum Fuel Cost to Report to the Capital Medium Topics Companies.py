""" 
    題意:
        給定一張有n個節點的graph , 其中只有n-1條edge , 沒有任何cycle存在.
        每個節點代表一個城市 , 並且每個城市都有一輛車,
        參數seats代表車輛的座位數來達到共乘,要求讓所有的城市都派人前往city0的最低cost

    思路:
        為了讓cost最小化 , 應該在座位數量允許的情況下'優先讓離city0最遠的節點往前塞' ,
        塞到前面的城市後再一起共乘回來. 
        
        因此我的思路是DFS展開,在展開的每個步驟都要紀錄目前離city的距離,接著往下展開
        每個dfs都回傳該節點上目前有多少乘客以及距離capital的距離.
        
        如果下一個節點的乘客數量+目前節點的乘客數量>seats數,就需要先派一台車回去
        派一台車的cost即 cost +1 + distance , 同時剩下的乘客數為 當前+下個節點-seats
        最後,我們需要手動將剩下距離capital為1的那些節點開回來(其他到達這些節點但乘客數量超過的都加過了)
"""

from typing import List 
class Solution:

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        if len(roads) == 0 : return 0 
        # build the graph first ; 
        graph = dict() 
        for (ai,bi) in roads : 
            if ai in graph : graph[ai].append(bi)
            else : graph[ai] = [bi]
            if bi in graph : graph[bi] .append(ai) 
            else : graph[bi] = [ai] 

        # base case : 
        # if the node only have one neighbor -> leaf 
        # if the prev_node
        
        # dfs :-> return the passenger at this node & distacne between the node with capital
        def dfs(node , distance , prev_node): 
            nonlocal cost 
            # leaf 
            if len(graph[node])  == 1 : return 1 , distance  
            
            total_passenger = 1 
            for neighbor in graph[node]: 

                if neighbor == prev_node : continue        
        
                next_passenger , next_distance = dfs(neighbor , distance+1 , node)

                if total_passenger + next_passenger <= seats : 
                    cost += 1 
                    total_passenger += next_passenger 
                else : 
 
                    cost += 1 
                    cost += distance 
                    total_passenger = (next_passenger + total_passenger - seats)
            
            return total_passenger , distance 
        
        cost = 0 
        
        for src_node in graph[0] : 

            next_passenger , next_distance = dfs(src_node , 1 , 0) 
            cost += 1 
        
        return cost  
        
        
S = Solution()
print(S.minimumFuelCost(roads = [[0,1],[0,2],[1,3],[1,4]] , seats=5))

print(S.minimumFuelCost([[0,1],[2,1],[3,2],[4,2],[4,5],[6,0],[5,7],[8,4],[9,2]] , seats=2))

print(S.minimumFuelCost([[1,0],[1,2],[0,3],[4,3],[5,2],[4,6],[1,7],[8,6],[9,6],[1,10],[6,11],[1,12],[13,9],[4,14],[3,15],[2,16],[5,17],[3,18],[6,19],[6,20],[21,16],[18,22],[0,23],[24,1],[25,12],[26,24],[9,27],[28,23],[29,25],[6,30],[31,21],[32,21],[33,23],[19,34],[5,35],[36,7],[25,37],[0,38],[1,39],[6,40],[41,3]]
,seats=5                        ))

""" 
    些微優化參數
"""

from typing import List 
class Solution:

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        if len(roads) == 0 : return 0 
        # build the graph first ; 
        graph = dict() 
        for (ai,bi) in roads : 
            if ai in graph : graph[ai].append(bi)
            else : graph[ai] = [bi]
            if bi in graph : graph[bi] .append(ai) 
            else : graph[bi] = [ai] 

        # base case : 
        # if the node only have one neighbor -> leaf 
        # if the prev_node
        
        # dfs :-> return the passenger at this node & distacne between the node with capital
        def dfs(node , distance , prev_node): 
            nonlocal cost 
            # leaf 
            if len(graph[node])  == 1 : return 1  
            
            total_passenger = 1 
            for neighbor in graph[node]: 

                if neighbor == prev_node : continue        
        
                next_passenger = dfs(neighbor , distance+1 , node)

                if total_passenger + next_passenger <= seats : 
                    cost += 1 
                    total_passenger += next_passenger 
                else : 
 
                    cost += 1 
                    cost += distance 
                    total_passenger = (next_passenger + total_passenger - seats)
            
            return total_passenger  
        
        cost = 0 
        
        for src_node in graph[0] : 
            next_passenger  = dfs(src_node , 1 , 0) 
            cost += 1 
        
        return cost  
        