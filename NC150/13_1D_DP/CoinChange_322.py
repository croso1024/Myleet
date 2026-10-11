"""
    題意 :
    coins 是不同面額的硬幣,每種面額都可以用無限多次。
    要湊出金額 amount,回傳所需的最少硬幣數。
    湊不出來就回傳 -1。
    amount 為 0 時,不需要任何硬幣,回傳 0。

    LeetCode 322 · Medium
    URL : https://leetcode.com/problems/coin-change/

    Example :
    coins = [1,2,5], amount = 11 -> 3
    coins = [2], amount = 3      -> -1
    coins = [1], amount = 0      -> 0

    Constraint :
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4

    思路 :
    這一題印象中就是DP , 但該如何走 Divide-Conquer 需要思考. 
    是 Bottom Up 從 amount = 1 開始往上推, 還是遞迴拆成樹狀的往下!? 

    先定義狀態與狀態遷移 , 狀態 DP(N) , 應該是用 coins 湊出 N 塊錢的最佳解. 
    DP(N) = 1 + DP(N - coin) for any coin in coins , 而 DP(N) = 0 表示湊不出來. 可以用None表示!? 
    基於上述想法 , 從 DP(1) 開始往上推 , 就會需要 O(coins) 的時間複雜度. 
    總時間複雜度就是 O( Coins x Amount size ). 空間複雜度則主要是 O(Amount Size)
    以這個方案 , 大概就能先通過題目. 


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Dict 


from typing import List, Dict 


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {coin : 1 for coin in coins} 
        dp[0] = 0

        for i in range(amount+1): 

            for coin in coins : 
                
                min_val =  min(
                    dp[i] if  i in dp else float("inf") , 
                    1 + dp[i-coin] if i-coin in dp else float("inf")
                )

                if min_val != float("inf")  : 
                    dp[i] = min_val 
                # 如果湊不出前面一組就略過. 
        
        return dp[amount] if amount in dp else -1






if __name__ == "__main__":
    c = Solution()

    # ((coins, amount), 預期, 說明)
    test_set = [
        (([1, 2, 5], 11), 3, "官方範例:5 + 5 + 1"),
        (([2], 3), -1, "官方範例:面額湊不出 3"),
        (([1], 0), 0, "官方範例:金額是 0"),
        (([2], 0), 0, "金額是 0,硬幣面額大於 0 也不影響"),
        (([1], 1), 1, "剛好一枚"),
        (([1], 2), 2, "只能用面額 1"),
        (([2], 4), 2, "兩枚相同面額"),
        (([2], 1), -1, "最小面額仍大於金額"),
        (([5], 3), -1, "只有一種面額,而且大於金額"),
        (([1, 3, 4], 6), 2, "兩枚 3,比 4 + 1 + 1 少"),
        (([3, 5], 11), 3, "5 + 3 + 3,兩枚湊不出 11"),
        (([4, 5], 8), 2, "兩枚 4"),
        (([4, 5], 7), -1, "4 和 5 的組合都湊不出 7"),
        (([1, 5, 10], 12), 3, "10 + 1 + 1"),
    ]

    for args, expected, note in test_set:
        result = c.coinChange(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={args} | expected={expected} | got={result}")
