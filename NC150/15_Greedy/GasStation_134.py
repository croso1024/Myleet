f"""
    題意 :
    環形路上有 n 個加油站。第 i 站有 gas[i] 單位的油。
    車子油箱沒有上限,從第 i 站開到下一站要消耗 cost[i] 單位的油。
    出發時油箱是空的,只能選一個站加油後再上路,而且只能順時針走。

    若存在一個起點,能繞完整圈回到該站,回傳那個起點的下標。
    若不管從哪一站出發都繞不完,回傳 -1。
    若存在可行起點,題目保證它是唯一的。

    LeetCode 134 · Medium
    URL : https://leetcode.com/problems/gas-station/

    Example :
    gas  = [1,2,3,4,5], cost = [3,4,5,1,2] -> 3
    gas  = [2,3,4],     cost = [3,4,3]     -> -1

    Constraint :
    n == gas.length == cost.length
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4

    思路 :
    直覺上會覺得，要盡可能保持油箱剩餘量最大, 剩餘量最大才有可能走得完.
    因為既然都要走一輪,所有的 cost[i] 都必然要走一次.

    因此最理想情況就是先找出某一格 , maximum( gas[i] - cost[i] ) , 從那一格出發.
    我們就有最多的郵箱冗餘. 以該格出發走一次,能走得完就可以,走不完就無法.

    上述想法有錯 , 因為以官方給的範例 : 
    gas  = [1,2,3,4,5], cost = [3,4,5,1,2] , 在我的解答方式下可以從 index = 3 / 4 開始,但只有從3開始可以. 
    因此思路稍微轉一下 , 變成要盡可能從 "接下來能累積最多Gas的位置出發" 
    gas - cost :  [-2,-2,-2,3,3] , 從右邊累加回來 : [0,2,4,6,3] ,因此應該從 index =3 出發
    假設 gas-cost [-2,3,5,-2,-2,-2] , [0,2,-1,-6,-4,-2] , 要從 index=1 出發
    

    複雜度 : 
    時間複雜度為 O(N) , 因為前面累積/找start index 跟實際測試是否可通都是線性掃描.
    空間複雜度 , 我這邊存 diff 需要用 O(N).
    第一版本解法 , 實際的表現是可以通過測資,但表現很差. 需優化. 

    仔細思考,不需要先做diff,才反向找尋. 完全可以在一個步驟內做這件事.
    而得到整圈瓦斯總量是否 T>=0後 , 從能累積瓦斯最多的點出發就必然能過

    Trade-off :

"""

from itertools import accumulate
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Find start point; 
        n = len(gas)
        # ======  原先找start index , 拆太多步驟 ========
        # start_index = None 
        # diff = [ gas[i]-cost[i] for i in range(n) ]
        # # 接著反向累積,找到值最大的index  , 直接改 diff 就好
        # for i in range(n-1,-1,-1): 
        #     if i == n-1 :continue
        #     diff[i] = diff[i] + diff[i+1] 
        # # 找出最大值作為 start_index 

        # maximum = float('-inf') 
        # for i in range(n): 
        #     if diff[i] >= maximum : 
        #         maximum = diff[i]
        #         start_index = i 
        # ======  原先找start index , 拆太多步驟 ========
        start_index = None 
        max_accumulate_diff = float("-inf")
        prev_diff = 0
        for i in range(n-1,-1,-1): 
            diff = gas[i] - cost[i] 
            accumulate_diff = diff + prev_diff 
            if accumulate_diff >= max_accumulate_diff : 
                max_accumulate_diff = accumulate_diff
                start_index = i 
            prev_diff = accumulate_diff
        
        # 最後一個 prev_diff 相當於整圈的 gas 總和與 cost  總和差
        if prev_diff < 0 : return -1 
        else: return start_index

        # 找到開始點之後,就可以嘗試走一圈
        current_gas = 0 
        step = 0 
        while step <= n : 
            
            current_index = ( start_index + step ) % n
            current_gas += (gas[current_index] - cost[current_index]) 
            if current_gas < 0 : return -1 

            step += 1 
        # 走完一圈沒有讓 current_gas 低於 0 過
        return start_index


if __name__ == "__main__":
    c = Solution()

    # (gas, cost, 預期, 說明)
    test_set = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3, "官方範例:從下標 3 出發剛好繞完"),
        ([2, 3, 4], [3, 4, 3], -1, "官方範例:總油量不足,任何起點都失敗"),
        ([5], [4], 0, "邊界:只有一站,油量足夠回到自己"),
        ([3], [4], -1, "邊界:只有一站,油量不夠出發"),
        ([3, 1], [1, 2], 0, "兩站,唯一可行起點在下標 0"),
        ([1, 2], [2, 1], 1, "兩站,下標 0 油不夠,只能從 1 出發"),
        ([2, 0, 3], [3, 1, 1], 2, "前兩站一出發就不夠,唯一起點在最後一站"),
        (
            [5, 1, 2, 3, 4],
            [4, 4, 1, 5, 1],
            4,
            "總油量剛好,中間多次見底,唯一起點在最後一站",
        ),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 3], -1, "總油量少於總消耗"),
        (
            [1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 1],
            5,
            "前五站都是負的,只能從最後一站出發",
        ),
        (
            [3, 1, 1, 10],
            [1, 2, 3, 4],
            3,
            "總油量有剩,但前三段會把油箱開成負的",
        ),
        ([5, 8, 2, 8], [6, 5, 6, 6], 3, "從下標 3 出發,中途油箱見底前都能維持非負"),
    ]

    for gas, cost, expected, note in test_set:
        result = c.canCompleteCircuit(gas, cost)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       gas={gas} cost={cost} | expected={expected} | got={result}")
