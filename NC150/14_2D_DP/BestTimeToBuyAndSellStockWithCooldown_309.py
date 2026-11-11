"""
    題意 :
    給定每一天的股價 prices[i]。
    可以買賣任意多次,但手上同時最多只持有一股,賣出之前不能再買。
    賣出之後的下一天是冷卻日,那天不能買進。

    回傳能得到的最大利潤。沒有任何一筆獲利的交易時,回傳 0。

    LeetCode 309 · Medium
    URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    Example :
    prices = [1,2,3,0,2] -> 3
    prices = [1]         -> 0

    Constraint :
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

    思路 :
    直覺上需要記住幾條不同情境下的最大獲利陣列.
    - 第i天手上持有股票的情況下的最大獲利
    - 第i天手上沒有股票的情況下的最大獲利 (這也是答案所在) 
    
    再分別解析這兩種情況怎算,考慮到題目規定賣完隔天不能買 , 這表示第i天要持有股票 , 那 i-1 天不可能賣掉股票

    - 第 i 天手上持有股票的最大獲利 = max(
        第 (i-2) 天沒有股票的最大獲利 - 第i天的股票價格,  
        第 (i-1) 天持有股票的最大獲利 
        )
    - 第 i 天手上沒有股票的最大獲利 = max(
        第 (i-1) 天沒有股票的最大獲利 , 
        第 (i-1) 天有股票的最大獲利 + 第i天的股票價格 
    )
    每一輪迭代,都需要往前看兩格. 所以初始條件需要給定兩格. 


    時間複雜度為 O(N) , 空間則為 O(N) , 這一題可以做空間壓縮進一步拉到 O(1) 

    Trade-off :

"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1 : return 0 
        
        # let dp[i][j] :  i 表示天數 , j=0表示沒拿股票 , j=1 表示有拿股票
        dp = [ [None , None] for i in range(len(prices)) ]

        # Given len(prices) >= 1 
        # 第一天沒拿股票最大獲利是0 , 有拿的話變成 -1 * prices[0]
        dp[0][0] = 0 
        dp[0][1] = -1 * prices[0]  

        # 考慮前看兩格, 這邊直接處理 dp[1] 的狀況. 
        dp[1][0] = max(dp[0][0] , dp[0][1] + prices[1]) 
        dp[1][1] = max(dp[0][1] , dp[0][0] - prices[1])

        # 接著開始走 loop 

        for day in range(2 , len(prices)):

            dp[day][0] = max(
                dp[day-1][0] , 
                dp[day-1][1] + prices[day]
            )
            dp[day][1] = max(
                dp[day-1][1] , 
                dp[day-2][0] - prices[day]
            )
        
        # 最終結果就是到最後一天 , 沒有股票的最大獲利
        return dp[len(prices)-1][0]




if __name__ == "__main__":
    c = Solution()

    # (prices, 預期, 說明)
    test_set = [
        ([1, 2, 3, 0, 2], 3, "官方範例:賣出後冷卻一天,再做第二筆"),
        ([1], 0, "官方範例:只有一天,無法賣出"),
        ([1, 2], 1, "兩天,買進後隔天賣出"),
        ([2, 1], 0, "價格下跌,不做交易"),
        ([5, 4, 3, 2, 1], 0, "一路下跌"),
        ([1, 2, 4], 3, "一路上漲,持有到最後一天再賣"),
        ([2, 1, 4], 3, "先跌再漲,只做一筆"),
        ([1, 3, 2, 8], 7, "中間的小波段比持有到最後差"),
        ([3, 2, 6, 5, 0, 3], 7, "第一筆賣出後冷卻,再接第二筆"),
        ([6, 1, 3, 2, 4, 7], 6, "低點買進後持有到最後"),
    ]

    for prices, expected, note in test_set:
        result = c.maxProfit(list(prices))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={prices} | expected={expected} | got={result}")
