"""
    題意 :
    有 n 個城市 (編號 0 ~ n-1),以若干航班連接。
    flights[i] = [from_i, to_i, price_i] 表示一班從 from_i 飛往 to_i、票價為 price_i 的單向航班。

    給定 src、dst、k,回傳從 src 到 dst「最多經停 k 站」的最便宜票價;
    若不存在這樣的路線,回傳 -1。

    (經停 k 站 = 中間經過 k 個城市 = 最多搭 k + 1 班飛機)

    LeetCode 787 · Medium
    URL : https://leetcode.com/problems/cheapest-flights-within-k-stops/

    Example :
    n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 -> 700
    n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1                    -> 200
    n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0                    -> 500

    Constraint :
    1 <= n <= 100
    0 <= flights.length <= (n * (n - 1) / 2)
    flights[i].length == 3
    0 <= from_i, to_i < n
    from_i != to_i
    1 <= price_i <= 10^4
    任兩個城市之間不會有重複的航班
    0 <= src, dst, k < n
    src != dst

    思路 :
    想法上,是找出 k 步內能從 src 抵達 dst 的路線,並評估這些路線的Cost , 找出 Cost 最低的那條. 
    只需要紀錄 Cost , 不用紀錄路徑.
    那這樣,從 src 開始做 k步 BFS , 一旦遇到 dst , 就將當前 BFS 累積的 cost 算一次最小值並更新答案.
    BFS 內的節點需要儲存 src 到該節點上當前的 cost 與路徑 ,基本上就是不能走回頭路而已.
    建立 Graph 本身需要 O(N^2) , BFS 展開需要 K 步,每一步最多 N^2 個走訪 , 所以是 O(K * N^2) ~= O(N^3)
    每一條走訪都需要維持一個 O(N) 的路徑集合, 故空間也是 O(N^3)

    一開始的解法不能直接過 , 後續優化,是考慮如何減少加入 queue 的節點數.
    方法是紀錄目前 src 出發到達每個點的最小 cost, 如果要加入的節點 cost 大於已知最小值,就不開放加入. 


    和 Claude 討論過後,這一題最大的優化關鍵在於其實不需要維護 Path Set,
    因為重複走訪的 cost 一定 > 初次走訪,既然我們存了 src 到每一個節點的 min cost ,
    就不必用 path set 鎖住,因為 path set 的複製與儲存平白吃掉每一條路徑時間/空間O(N) 

    拿掉 path_set , 時間複雜度基本上等於 O(k*E) , 空間則是 O(N + E) (Graph)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List,Dict,Set
from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        
        # Dict[int : Dict[int:int]]
        graph = { i : {} for i in range(n) } 
        min_cost_array = [ float('inf') for i in range(n)] 
        min_cost_array[src] = 0 
        queue = deque()
        # 填充 Graph : 
        for i in range(len(flights)): 
            from_i , to_i , price_i = flights[i] 
            graph[from_i][to_i] = price_i 
        

        # 從 src 開始走 BFS , 每一個節點紀錄當前路徑與Cost: 
        # 節點結構 : (編號,累積Cost)
        step = 0 
        minimum_cost = float("inf") 
        
        queue.append(
             (src ,set([src]) , 0)
        ) 

        # 一旦在 k 步內碰到 DST 就可以更新當前最小Cost
        while queue and step <= k : 

            size = len(queue) 

            for _ in range(size) : 

                node_index , path_set , accumulate_cost = queue.popleft()
                node_index :int 
                path_set : Set[int]

                # 從 Graph 裡找還能去的
                for next_index , cost in graph[node_index].items() : 

                    # 一旦下一個節點就是目標,就可以提早截斷了
                    if next_index == dst : 
                        minimum_cost = min(minimum_cost , cost+accumulate_cost)
                        continue

                    if next_index not in path_set  and  accumulate_cost + cost < min_cost_array[next_index]  : 
                        # 更新到每個節點的最短距離
                        min_cost_array[next_index] = min(min_cost_array[next_index] , accumulate_cost + cost)
                        path = path_set.copy()
                        path.add(next_index)
                        queue.append(( next_index , path , accumulate_cost + cost ))

            # step += 1 表示停了一站
            step += 1 


        if minimum_cost == float("inf"):return - 1 
        else : return minimum_cost 


if __name__ == "__main__":
    c = Solution()

    # (n, flights, src, dst, k, 預期, 說明)
    # 每次呼叫都複製 flights,實作改到測資本身不會留到下一題
    test_set = [
        # (
        #     4,
        #     [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
        #     0,
        #     3,
        #     1,
        #     700,
        #     "官方範例:0->1->3 (0->1->2->3 較便宜但經停 2 站)",
        # ),
        # (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200, "官方範例:經停一站比直飛便宜"),
        # (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500, "官方範例:k = 0 只能直飛"),
        # (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 2, 200, "k 比實際需要的還大"),
        # (2, [[0, 1, 5]], 0, 1, 0, 5, "邊界:只有一班直飛"),
        # (2, [], 0, 1, 1, -1, "邊界:沒有任何航班"),
        # (3, [[0, 1, 100]], 0, 2, 1, -1, "dst 完全到不了"),
        # (3, [[1, 2, 10]], 0, 2, 2, -1, "src 沒有任何出發航班"),
        # (3, [[0, 1, 10], [2, 1, 10]], 0, 2, 2, -1, "航班是單向的,反方向飛不過去"),
        # (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 0, 3, 1, -1, "唯一路線需要經停 2 站,超過 k"),
        # (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 0, 3, 2, 3, "唯一路線剛好經停 k 站"),
        # (
        #     4,
        #     [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 100]],
        #     0,
        #     3,
        #     1,
        #     100,
        #     "便宜的長路線超過 k,只能退而求其次搭直飛",
        # ),
        # (
        #     4,
        #     [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 100]],
        #     0,
        #     3,
        #     2,
        #     3,
        #     "同上,但 k 放寬後便宜的長路線可行",
        # ),
        # (
        #     5,
        #     [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
        #     0,
        #     2,
        #     2,
        #     7,
        #     "整體最便宜的路線 (成本 6) 需要經停 3 站,答案是 0->1->4->2",
        # ),
        # (
        #     3,
        #     [[0, 1, 1], [1, 0, 1], [1, 2, 10]],
        #     0,
        #     2,
        #     2,
        #     11,
        #     "圖中有環,不能無限繞圈",
        # ),
        (
            5,
            [[1,0,5],[2,1,5],[3,0,2],[1,3,2],[4,1,1],[2,4,1]],
            2,
            0,
            2,
            7,
            "線上失敗測資"
        )
        
    ]

    for n, flights, src, dst, k, expected, note in test_set:
        result = c.findCheapestPrice(n, [f[:] for f in flights], src, dst, k)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       n={n} src={src} dst={dst} k={k} flights={flights}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
