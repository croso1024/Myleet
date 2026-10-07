"""
    題意 :
    points[i] = [xi, yi] 是平面上的一個點,k 是要取的個數。
    回傳距離原點 (0, 0) 最近的 k 個點。

    距離是歐氏距離:sqrt( (x1 - x2)^2 + (y1 - y2)^2 )。

    回傳順序不限。
    除了順序之外,答案是唯一的:第 k 近的邊界上不會有距離打平、需要二選一的情況。

    LeetCode 973 · Medium
    URL : https://leetcode.com/problems/k-closest-points-to-origin/

    Example :
    points = [[1,3],[-2,2]], k = 1 -> [[-2,2]]
    points = [[3,3],[5,-1],[-2,4]], k = 2 -> [[3,3],[-2,4]]

    Constraint :
    1 <= k <= points.length <= 10^4
    -10^4 <= xi, yi <= 10^4

    思路 :
    直覺上覺得很Naive , 直接計算每一個點到原點的距離. 
    並以此維護一個大小為 K 的 Max Heap 即可!? 

    每個 element 保持紀錄座標位置,以及和原點的距離. 
    Max heap 紀錄前K個最靠近的值. 
    一但有新值出現,就和 Heap Top 比較 , 更小就納入,更大就跳過. 
    時間複雜度 : N組元素,但維護K的大小, 時間複雜度 O(NlogK) , 空間 O(K)

    但一次提交後發現空間上成績不太好,可以有些優化空間. 
    改用常數指標紀錄目前的守門員 (第K近是多近) , 然後 heap 可以直接作為答案. 不必重新建構 
    

    複雜度 : 時間複雜度 O(NlogK) , 空間 O(K)

    Trade-off :

"""

from typing import List
from heapq import heappop , heappush 
from math import pow

from collections import namedtuple 

# Solution 1 , 直覺的做法
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [] 

        for point in points : 

            x = point[0]
            y = point[1]
            # 既然大家都要開根號 , 那就省掉這一步驟
            distance_to_origin =  pow(x,2)+pow(y,2) 

            # 如果 Heap 大小目前小於 K , 就直接塞
            if len(heap) < k : 
                heappush( heap , ( -1 * distance_to_origin , ( x,y ) ) )
                continue

            # 如果已經大於K了 , 就先檢查頂端(距離原點剛好第K遠)的點是否比當前這個更近 
            # 如果當前節點更接近原點 , 則 pop -> push 
            if  -1 * heap[0][0] > distance_to_origin : 
                heappop(heap)
                heappush(heap ,( -1 * distance_to_origin , ( x,y ) ) ) 
        
        # 最後Heap內的就是前K個最接近的節點

        results = [] 
        for _ , coordinate in heap : 
            results.append([coordinate[0] , coordinate[1]])
        
        return results 



def canon(points):
    """點的回傳順序不影響對錯。"""
    if points is None:
        return None
    return sorted(tuple(point) for point in points)


if __name__ == "__main__":
    c = Solution()

    # (points, k, 預期, 說明)
    test_set = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]], "官方範例:只取最近的 1 個"),
        (
            [[3, 3], [5, -1], [-2, 4]],
            2,
            [[3, 3], [-2, 4]],
            "官方範例:順序可以相反",
        ),
        ([[1, -1]], 1, [[1, -1]], "邊界:只有一個點"),
        ([[0, 0], [1, 1]], 1, [[0, 0]], "原點本身最近"),
        (
            [[1, 1], [-1, -1], [2, 2]],
            3,
            [[1, 1], [-1, -1], [2, 2]],
            "k 等於點的個數,全部回傳",
        ),
        (
            [[-5, 0], [4, 0], [3, 0]],
            2,
            [[4, 0], [3, 0]],
            "負座標,最近的兩個都在正 x 軸附近",
        ),
        (
            [[10, 0], [0, 1], [0, -100]],
            1,
            [[0, 1]],
            "其餘兩點都遠很多",
        ),
        (
            [[0, 2], [2, 0], [5, 5]],
            2,
            [[0, 2], [2, 0]],
            "兩個點距離相同,而且都在最近的 k 個裡",
        ),
        (
            [[1, 2], [1, 2], [-10, 10]],
            2,
            [[1, 2], [1, 2]],
            "座標重複的兩個點都要留",
        ),
        (
            [[-1, -1], [1, 0], [2, -1], [0, 2]],
            1,
            [[1, 0]],
            "四個點裡只取距離平方為 1 的那個",
        ),
    ]

    for points, k, expected, note in test_set:
        result = c.kClosest([point[:] for point in points], k)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       k={k} | expected={expected}")
        print(f"       got     ={result}")
