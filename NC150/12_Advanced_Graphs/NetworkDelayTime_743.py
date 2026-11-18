"""
    題意 :
    給定一個有 n 個節點的網路,節點編號 1 到 n。
    times[i] = (ui, vi, wi) 表示一條「有向邊」:訊號從 ui 傳到 vi 需要 wi 單位時間。

    現在從節點 k 發出訊號,回傳「所有節點都收到訊號」所需的最短時間。
    若有任何節點收不到訊號,回傳 -1。

    LeetCode 743 · Medium
    URL : https://leetcode.com/problems/network-delay-time/

    Example :
    times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 -> 2
    times = [[1,2,1]], n = 2, k = 1                 -> 1
    times = [[1,2,1]], n = 2, k = 2                 -> -1

    Constraint :
    1 <= k <= n <= 100
    1 <= times.length <= 6000
    times[i].length == 3
    1 <= ui, vi <= n
    ui != vi
    0 <= wi <= 100
    所有 (ui, vi) 組合互不重複(沒有重邊)

    思路 :

    這一題算是有趣的 Graph 題目, 我的預期是先建立 Edge 表, 
    訂出每一個節點可以去的清單,以及時間開銷.

    接著從給定結點出發 , 使用 Set 維護 visited , 使用 Min Heap 去維護接下來可以尋訪的節點清單. 
    同時給一個全域計時器. 
    每當走到一個節點並更新可尋訪節點清單後 , 從 Min-Heap 吐出下一個最快可以尋訪的節點清單(可能不止一個),並將這些節點納入下一輪搜索,同時更新計時器
    直到所有節點走完,此時計時器就是答案.
    或著可尋訪清單清空,還沒走完所有節點就回 -1 

    複雜度 : 

    # 建立 Graph : O(E) , 
    # 每一個節點要進入一次 Heap / 出來一次 Heap : O(NlogN) 
    # 每一個節點都要 for-loop 一次所有邊, 但總 loop 數量受限於邊 , O(E)
    # 故時間複雜度 O(E) + O(NlogN) 

    # 空間複雜度 , 我們就是存節點 O(N)
    
    Trade-off :

"""

from typing import List , Dict 
from heapq import heappop , heappush 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        time_counter = 0 

        # 建立圖 : 從節點 ui 出發 , 可以抵達的 vi 和對應 Cost 
        graph : Dict[ int , Dict[ int , int ]] = {}
        # heap , 用來維護最快可以繼續出發的節點 , 資料結構 ( current_time + wi , vi) , Cost 在前用於排序,後者節點編號. 整體保證不需要處理 tie-breaker , 
        # 注意權重是以拜訪到該節點的時間當下 + wi
        heap = []
        # visited : 用來維護踩過的點
        visited = set()

        for ui , vi ,wi in times : 
            if ui not in graph : graph[ui] = {} 
            graph[ui][vi] = wi 

        # wi 可以是 0 
        
        # 接著從給定目標節點開始出發 , 先初始化可以到達的點 , 踩過的點.並開始準備遍瀝
        for node in graph.get(k,[]) : heappush(heap , ( graph[k][node] , node ))
        visited.add(k) 

        # 只要還有可以走的點
        while heap : 
            # print(f"Current Heap : {heap} , Visited : {visited}")

            next_nodes = [] 

            # 檢查 heap 最頂端 ( 最快可以走的節點 ) , 和 time_counter 
            while heap and heap[0][0] <= time_counter : next_nodes.append(heappop(heap)[1])

            # 如果這一輪 next_node 已經有東西,就可以開始走訪. 否則要刷新 time_counter 硬拿.
            if not next_nodes :
                time_counter = heap[0][0] 
                while heap and heap[0][0] <= time_counter : next_nodes.append(heappop(heap)[1])

            # 走訪 next_nodes 
            for node in next_nodes : 
                if node in visited : continue
                visited.add(node) 
                # 檢查 Graph 內還有的節點. 
                for next in graph.get(node,[]) : 
                    if next not in visited :
                        heappush( heap , ( time_counter + graph[node][next] , next )) 

            # 全部走完 , 如果拜訪節點數量等同總節點數量 , 就回傳 time_counter 作為答案.    
            if len(visited) == n : return time_counter
        
        return -1 


if __name__ == "__main__":
    c = Solution()

    # (times, n, k, 預期, 說明)
    # 每次呼叫都複製 times,實作改到測資本身不會留到下一題
    test_set = [
        ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2, "官方範例:從 2 出發,最遠的 4 要 2"),
        ([[1, 2, 1]], 2, 1, 1, "官方範例:單一條邊"),
        ([[1, 2, 1]], 2, 2, -1, "官方範例:有向邊,反方向傳不過去"),
        (
            [[1, 2, 10], [1, 3, 1], [3, 2, 1]],
            3,
            1,
            2,
            "陷阱:直達邊較慢,繞路 1->3->2 才是最短",
        ),
        (
            [[1, 2, 1], [1, 3, 4], [2, 3, 1], [3, 4, 1]],
            4,
            1,
            3,
            "陷阱:3 先以距離 4 進 heap,後來被 2 更新成 2,舊的那筆要跳過",
        ),
        (
            [[1, 2, 3], [1, 3, 5], [1, 4, 2]],
            4,
            1,
            5,
            "星狀圖:答案是最短距離的最大值,不是總和",
        ),
        ([[1, 2, 1], [2, 3, 1]], 4, 1, -1, "節點 4 完全孤立,沒有任何邊"),
        ([[1, 2, 1], [3, 2, 1]], 3, 1, -1, "節點 3 只有出邊,從 1 到不了"),
        ([[1, 2, 1], [2, 3, 1], [3, 1, 1]], 3, 1, 2, "圖中有環,不能無限繞圈"),
        ([[1, 2, 0], [2, 3, 0]], 3, 1, 0, "邊界:權重為 0,全部瞬間收到"),
        (
            [[3, 1, 5], [3, 2, 2], [2, 1, 2]],
            3,
            3,
            4,
            "起點不是 1:3->2->1 比 3->1 快",
        ),
        (
            [[1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100]],
            5,
            1,
            400,
            "邊界:權重上限的長鏈",
        ),
    ]

    for times, n, k, expected, note in test_set:
        result = c.networkDelayTime([edge[:] for edge in times], n, k)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       n={n} k={k} times={times}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
