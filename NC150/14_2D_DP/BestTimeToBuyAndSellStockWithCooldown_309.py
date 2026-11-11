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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


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
