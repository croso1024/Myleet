"""
    題意 :
    cost[i] 是第 i 階樓梯的費用。付了這一階的費用後,可以再往上爬 1 階或 2 階。
    可以從第 0 階或第 1 階開始。
    樓頂在最後一階的再上面。
    回傳到樓頂的最低費用。

    LeetCode 746 · Easy
    URL : https://leetcode.com/problems/min-cost-climbing-stairs/

    Example :
    cost = [10,15,20] -> 15
    cost = [1,100,1,1,1,100,1,1,100,1] -> 6

    Constraint :
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999

    思路 :
    給定Cost陣列, cost[i] 表示要付多少錢才能走 , 每一次最多走一格或兩格. 
    起始能從第 0 or 1 格開始. 求走到頂最便宜的價格. 

    這一題就是標準1D DP , dp[i] 去紀錄走到這一格的最低價格.
    依照題目範例 cost=[10,15,20] , 1D DP應該是 [10,15,30] , 而答案則是 min( dp[-1] , dp[-2] ) 

    時間複雜度為 O(n) , 空間上只需要存兩格, 故也是O(1)

    Trade-off :

"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Given len(cost) >= 2 
        ref1 = cost[0]
        ref2 = cost[1] 

        for i in range(2,len(cost)): 
            # 到達 i 格最便宜的價格就是 cost[i] + min(ref1,ref2) 
            min_cost = cost[i] + min(ref1,ref2)  
            ref1 = ref2 
            ref2 = min_cost  
        
        return min(ref1 , ref2) 



if __name__ == "__main__":
    c = Solution()

    # (cost, 預期, 說明)
    test_set = [
        ([10, 15, 20], 15, "官方範例:從第 1 階付 15,一次跨到樓頂"),
        (
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
            6,
            "官方範例:避開三個 100",
        ),
        ([0, 0], 0, "邊界:兩階費用都是 0"),
        ([0, 1], 0, "從第 0 階付 0,一次跨兩階到樓頂"),
        ([1, 0], 0, "從第 1 階付 0,再爬一階到樓頂"),
        ([10, 15], 10, "兩階,從較便宜的那階直接跨到樓頂"),
        ([1, 2, 3], 2, "從第 1 階付 2,一次跨到樓頂"),
        ([999, 999], 999, "邊界:費用上限,兩階只能付一次"),
        ([1, 2, 1, 2], 2, "付第 0 階與第 2 階"),
        ([1, 100, 1, 100, 1], 3, "三個 1 都踩,兩個 100 都跳過"),
    ]

    for cost, expected, note in test_set:
        result = c.minCostClimbingStairs(list(cost))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={cost} | expected={expected} | got={result}")
