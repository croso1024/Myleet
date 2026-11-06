"""
    題意 :
    給定一個整數陣列 coins,代表各種不同面額的硬幣,以及一個整數 amount 代表總金額。
    回傳湊出 amount 的組合數。湊不出來就回傳 0。

    每種面額的硬幣數量無限。
    只看組合、不看順序:1 + 2 與 2 + 1 算同一種。
    答案保證落在 32-bit 有號整數範圍內。

    LeetCode 518 · Medium
    URL : https://leetcode.com/problems/coin-change-ii/

    Example :
    amount = 5,  coins = [1,2,5] -> 4
    amount = 3,  coins = [2]     -> 0
    amount = 10, coins = [10]    -> 1

    Constraint :
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    coins 裡的面額互不相同
    0 <= amount <= 5000

    思路 :
    直覺上好像可以 Back tracking 往下鑽,但時間複雜度和深度這兩個問題沒有解掉. 

    這一題走 DP 填表.關鍵是要找出狀態轉移的方式. 
    按照我們 backtracking 的參數 , 使用 coins[i:] , 去湊 rest_amount 的值去想. 

    2D DP 就使用 len(coins) x amount 去建表. 
    舉例 , coins = [1,2,5] , amount = 5  , 定義每一格 dp[amount][i] 就是在可以使用 coins[:i+1] 的情況下湊出 amount 的方法數
    那麼 dp[amount][i] 等於多少!? 

    先手動填表 :

      1 2 5
    0 1 1 1 
    1 1 1 1
    2 1 2 2
    3 1 2 2  # (1+1+1) , (1+2)
    4 1 3 3  # (1+1+1+1) , (1+1+2) , (2+2)
    5 1 3 4  # (1+1+1+1+1) , (1+1+1+2) , (1+2+2) , (5)

    去觀察這個表 , 用 coins[:i+1] 湊出 amount 的方法數量 
    ==  coins[:i] 湊出 amount 的方法數 +  coins[:i+1] 湊出 amount-coins[i] 的方法數
    dp[amount][i] = dp[amount][i-1] + dp[amount-coins[i]][i] 
    所以要用到左側,跟往上的情況. 

    複雜度 : 時間複雜度 O( amount x len(coins)) , 空間複雜度一樣
    進一步走 1D 壓縮,空間複雜度可以壓制到 O(amount)

    Trade-off :

"""

from typing import List

# 解法一 , 可以過的邏輯,但時間複雜度和遞迴深度會炸裂. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total_method = 0 
        # i : index , 表示還可以使用的有 coins[i:] 
        # rest_amount : 還要湊的金額 
        def backtracking(i :int , rest_amount :int) : 

            nonlocal total_method

            if rest_amount == 0 :
                total_method += 1 
                return 
            elif rest_amount < 0 : 
                return 

            for j in range(i , len(coins)): 
                backtracking(j , rest_amount=rest_amount-coins[j]) 
            
        backtracking(0 , rest_amount=amount)
        return total_method

# 解法二 , 走 2D DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # 建立表 , 列為 amount , 行為 coins
        dp = [ [0 for i in range(len(coins)) ] for _ in range(amount+1) ] 
        
        # 針對第一行 dp[:][0] , 先預算好 , dp[i][0] = 1 if i % coins[0] == 0
        for i in range(amount+1): dp[i][0] = 1 if i % coins[0] == 0 else 0 
        
        # 走訪過程就是正常走訪雙 loop 即可 , 每一跳需要的是左側與上方. 
        for i in range(amount+1):
            for j in range(1,len(coins)): 

                if i-coins[j] >= 0 : 
                    dp[i][j] = dp[i][j-1] + dp[i-coins[j]][j] 
                else : 
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]

# 解法三 , 壓縮為 1D DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 預先建立好第一層 , 在只有第一個硬幣的情況下,面對每一個 amount 怎樣組
        dp = [ 1 if i % coins[0] == 0 else 0  for i in range(amount+1)  ]
        
        # dp[i] 表示在當前這一次迭代可用的 coins 範圍中 , 湊出 i 的組合數
        # dp[i] = dp[i] (前一次迭代可用的coins的組合數) + dp[i-coins[j]] 
        for j in range(1,len(coins)): 

            for i in range(amount+1): 

                dp[i] = dp[i] + dp[i - coins[j]]  if i - coins[j] >= 0 else dp[i]

        return dp[-1] 



if __name__ == "__main__":
    c = Solution()

    # ((amount, coins), 預期, 說明)
    test_set = [
        ((5, [1, 2, 5]), 4, "官方範例"),
        ((3, [2]), 0, "官方範例:湊不出來"),
        ((10, [10]), 1, "官方範例:單一面額剛好湊出"),
        ((0, [7]), 1, "邊界:amount 為 0"),
        ((0, [1, 2, 3]), 1, "邊界:amount 為 0,多種面額"),
        ((4, [1, 2]), 3, "1+1+1+1 / 1+1+2 / 2+2"),
        ((4, [1, 2, 3]), 4, "比上一題多一種面額 3"),
        ((5, [2, 3]), 1, "只有 2+3 一種"),
        ((7, [2, 4]), 0, "全是偶數面額,湊不出奇數"),
        ((6, [1, 5]), 2, "全用 1 / 1+5"),
        ((10, [2, 5, 3, 6]), 5, "四種面額,輸入沒有排序"),
        ((5, [5, 1, 2]), 4, "同官方範例,面額順序打亂"),
        ((100, [99, 1]), 2, "大面額只能用一次"),
    ]

    for args, expected, note in test_set:
        amount, coins = args
        result = c.change(amount, coins[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={args} | expected={expected} | got={result}")
