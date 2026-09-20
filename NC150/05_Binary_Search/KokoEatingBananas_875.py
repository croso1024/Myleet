"""
    題意 :
    Koko 面前有 n 堆香蕉,第 i 堆有 piles[i] 根。警衛會在 h 小時後回來。

    Koko 可以自行決定「每小時吃幾根」的速度 k。每個小時她挑一堆,從中吃掉 k 根;
    若該堆不足 k 根,就把整堆吃完,且該小時內不再吃其他堆(吃不滿也算用掉一小時)。

    Koko 想吃得越慢越好,但必須在警衛回來前把所有香蕉吃完。
    回傳能在 h 小時內吃完的「最小整數速度 k」。

    LeetCode 875 · Medium
    URL : https://leetcode.com/problems/koko-eating-bananas/

    Example :
    piles = [3,6,7,11],       h = 8 -> 4
    piles = [30,11,23,4,20],  h = 5 -> 30
    piles = [30,11,23,4,20],  h = 6 -> 23

    Constraint :
    1 <= piles.length <= 10^4
    piles.length <= h <= 10^9          (h 保證不小於堆數,所以必定有解)
    1 <= piles[i] <= 10^9

    思路 :
    

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


"""
這題要求一個最小值 , 讓猴子在 h 小時內能吃完所有 pile , 
每一次 Evaluate , 需要的時間為 O(N) 去算出當前速度k吃完要多少h , 是否<h 

我們用 Binary Search 去逼近這個最小值.屬於拿 Binary Search ,但不止找到target,還要逼近target極值的模式. 


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def can_finish_all_pile( k : int , h : int ) : 
            total_hours = 0 
            for pile in piles : 
                total_hours += (pile // k) if pile % k == 0 else (pile//k) + 1 
            return total_hours <= h 
        
        # Binary Search 逼近, 我們知道 k = max(piles)能在 len(piles) 小時去吃完
        left , right = 1 , max(piles) 
        
        while left < right : 

            k = (right+left)//2 
            # 可以完成,代表當前速度吃的完,繼續往下逼近,但當前速度k可能就是答案,留在 Search Space 
            if can_finish_all_pile( k , h )  : 
                right = k
            # 無法完成,才要做加速, k必然不是答案了
            else : 
                left = k + 1 
            
        return right 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30),
        (([30, 11, 23, 4, 20], 6), 23),
        (([1], 1), 1),                              # 邊界:最小輸入
        (([1, 1, 1, 1], 4), 1),                     # h 剛好等於堆數,k=1 即可
        (([3, 6, 7, 11], 4), 11),                   # h == len(piles):答案必為 max(piles)
        (([1000000000], 2), 500000000),             # 大數值:上界必須取到 max(piles)
        (([312884470], 968709470), 1),              # h 極大:答案收斂到下界 1
    ]

    for args, expected in test_set:
        result = c.minEatingSpeed(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
