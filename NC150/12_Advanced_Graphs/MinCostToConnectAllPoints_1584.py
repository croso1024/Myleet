"""
    題意 :
    給定 2D 平面上的 n 個點 points,points[i] = [xi, yi]。
    連接兩點 (xi, yi) 與 (xj, yj) 的成本是它們的曼哈頓距離 |xi - xj| + |yi - yj|。

    回傳讓「所有點彼此連通」的最小總成本。
    連通的定義:任兩點之間「有且只有一條」簡單路徑。

    LeetCode 1584 · Medium
    URL : https://leetcode.com/problems/min-cost-to-connect-all-points/

    Example :
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]] -> 20
    points = [[3,12],[-2,5],[-4,1]]           -> 18

    Constraint :
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    所有點 (xi, yi) 互不重複

    思路 :
    這一題應該屬於最小生成樹 MST , 採用從已知節點找下一個最近節點的方案. 

    首先 , 先建立所有點之間的 Graph , 這一步驟需要 O(N^2) , 
    接下來 , 維護兩個 Set , 分別是已經被連接的以及尚未被連接的. 
    我認為還需要一個 Heap , 儲存 "已經連接(走過)的節點"到其他節點之間的距離,採用 Min-Heap , 先存最小的. 

    接著從任意一個節點出發 , 加入其到 visited set , 並把所有該節點能走的 Edge ,以 visited_set 過濾加入 Heap , 
    之後從中選擇最小cost的edge , 如此往復即可. 後續遇到 heap 的目標節點是在 visited set 就直接濾掉. 

    這樣 , 總時間複雜度有 :
    建立 Graph O(N^2) , 我們把 N^2 設置為 E , 即 Edges 數 
    所有 Edge 需要進入一次 Heap , 出來一次 , 故為 O(ElogE)  
    空間上 , 需要儲存 O(E) 的 Heap  ,還有 O(N) 的兩個 set , 攤下來是 O(E) , 

    故這一題的時間複雜度為 O(ElogE) , 空間為 O(E) , E ~= N^2


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List
from heapq import heappush , heappop


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # graph : dict[int : dict[ int : int  ]]  (  source : { target : cost } )
        graph = {} 
        cal_distance = lambda x1,x2 , y1,y2 : abs(x1-y1) + abs(x2-y2) 

        # 建立 Graph  

        # 已知 point 不會重複  , 每一次連接都雙向連接
        for i in range(len(points)) : 

            x1 , x2  = points[i]

            if i not in graph : graph[i] = {} 

            for j in range(i+1 , len(points)) : 

                y1 , y2  = points[j] 

                if j not in graph : graph[j] = {} 

                graph[i][j] = cal_distance(x1,x2,y1,y2)
                graph[j][i] = cal_distance(x1,x2,y1,y2)
                
        # 用索引來放
        visited  = set()
        unvisted = set( range(len(points )) ) 

        heap = [] 
        # 初始化節點 , 隨意選一個 
        init_node_index = unvisted.pop() 
        visited.add(init_node_index)

        # 把該節點可以去到的 Edge 都納入 heap 
        for target_index , cost in graph[init_node_index].items() :  
            heappush(heap , (cost , target_index))

        total_cost = 0 
        # 只要 heap 還有就要走 , 
        while heap : 

            cost , next_index = heappop(heap)
            if next_index in visited : continue 

            visited.add(next_index)
            unvisted.remove(next_index) 
            total_cost += cost 
            # 把該節點可以去到的位置加入 
            for target_index , cost in graph[next_index].items() :
                heappush(heap , (cost, target_index))

        return total_cost



# 想像中的優化版,不特別先建立圖. 
# 而是在尋訪過程動態補
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        cal_distance = lambda x1,x2,y1,y2 : abs(x1-y1) + abs(x2-y2) 

        visited = set()
        unvisited = set(range(len(points))) 
        heap = [] 
        init_index = unvisited.pop()
        visited.add(init_index)

        for i in range(len(points)):
            if i == init_index : continue 
            cost = cal_distance( points[init_index][0] , points[init_index][1] , points[i][0] , points[i][1]  )
            heappush(heap , (cost , i)) 
        
        total_cost = 0 

        while unvisited : 

            cost , next_index = heappop(heap)

            if next_index in visited : continue 

            visited.add(next_index)
            unvisited.remove(next_index)
            total_cost += cost 

            # 補上 edge 
            for i in range(len(points)): 
                if i in visited : continue 
                cost = cal_distance( points[next_index][0] , points[next_index][1] , points[i][0] , points[i][1]  )
                heappush(heap , (cost , i)) 
        
        return total_cost



if __name__ == "__main__":
    c = Solution()

    # (points, 預期, 說明)
    # 每次呼叫都複製 points,實作改到測資本身不會留到下一題
    test_set = [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20, "官方範例:5 個點"),
        ([[3, 12], [-2, 5], [-4, 1]], 18, "官方範例:3 個點,含負座標"),
        ([[0, 0]], 0, "邊界:只有一個點"),
        ([[0, 0], [1, 1]], 2, "邊界:兩個點,只有一條可選的邊"),
        ([[0, 0], [1, 0], [2, 0], [3, 0]], 3, "4 個點共線,間距皆為 1"),
        ([[0, 0], [0, 1], [1, 0], [1, 1]], 3, "單位正方形的 4 個頂點,四條邊長度相同"),
        (
            [[0, 0], [2, 0], [-2, 0], [0, 2], [0, -2]],
            8,
            "原點加上四個方向各距離 2 的點",
        ),
        (
            [[0, 0], [1, 1], [1, 0], [-1, 1], [3, 3]],
            8,
            "5 個點,多條邊的成本相同",
        ),
        (
            [[-1000000, -1000000], [1000000, 1000000]],
            4000000,
            "邊界:座標範圍的兩個對角端點",
        ),
    ]

    for points, expected, note in test_set:
        result = c.minCostConnectPoints([p[:] for p in points])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       points={points}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
