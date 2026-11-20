"""
    題意 :
    給定一個整數陣列 nums 與一個整數 target。
    你要在 nums 的「每一個」數字前面各加上 '+' 或 '-' 其中一個符號,
    然後把它們串起來求值。例如 nums = [2, 1],可以組成 "+2-1" = 1。

    回傳「有幾種符號組合」能讓運算結果恰好等於 target。

    LeetCode 494 · Medium
    URL : https://leetcode.com/problems/target-sum/

    Example :
    nums = [1,1,1,1,1], target = 3 -> 5
        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3
    nums = [1], target = 1 -> 1

    Constraint :
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000

    思路 :
    有20個數字,每一個都能給 +/- , 全展開是 2^20 好像在暴力解可以觸及的範圍.
    另一條思路是 DP , 
    但 DP 要存的東西可能是從 target 範圍 -1000 ~ 1000 , 以當前的 nums 陣列大小可以組合成的方式.
    從二維 DP 出發 , dp[i][j] => 使用 nums[:i+1] 範圍中 , 湊到 j 值的方法數. 
    dp[i][j] = 這一輪多了 nums[i] 可用, 從前一輪 dp[i-1][j] 中去看 j + nums[i] , j - nums[i] 的方法數合併即可. 
    這樣,時間複雜度為 O(N x range) , range 就是 target 的範圍,空間複雜度也為 O(N x range) ,
 

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

# 先嘗試看看暴力展開. 
# nums 只會有 20 個, 因此直接遞回就好
# 可以過測資,在我的 Mac 上 nums = 20 也能順利過,但網站上會卡住
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0 
        size = len(nums) 

        def _recursive_search( index : int , total_sum : int): 
            nonlocal count 
            if index == size :
                if total_sum == target: count+=1
                return 
            _recursive_search(index + 1 , total_sum= total_sum + nums[index])
            _recursive_search(index + 1 , total_sum= total_sum - nums[index])
        
        _recursive_search(0 , 0)
        return count

# 走 DP 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [  [ 0 for j in range(2000+1)] for i in range(len(nums)) ] 

        offset = 1000 

        # dp[i][j] 表示在使用到 nums[:i+1] 的範圍下,要湊出 j 值的方式數
        # 初始化,在僅使用 nums[0] 的情況下只有 -1 * nums[0] / 1 * nums[0] 的方法數為 1 

        # 陷阱 : nums[0] = 0 時 , 應該有 +0 / -0 兩種方法 
        dp[0][ nums[0] + offset  ] += 1 
        dp[0][ -1*nums[0] + offset  ] += 1 

        # 開始走 loop , 每一格子依賴的是前一輪的方法數
        for i in range( 1 , len(nums)) : 

            for j in range(2000+1): 
                # 迭代的方式是截止前一輪 ,  要湊到與 j 差 nums[i] 的方法數加總
                # dp[i][j] = dp[i-1][ j - nums[i] ] + dp[i-1][ j + nums[i] ] 
                a1 = dp[i-1][j-nums[i]] if j - nums[i] >= 0 else 0 
                a2 = dp[i-1][j +nums[i]] if j + nums[i] <= 2000 else 0 
                dp[i][j] = a1 + a2 
        
        return dp[len(nums)-1][target + offset]


if __name__ == "__main__":
    c = Solution()

    # (nums, target, 預期, 說明)
    # 每次呼叫都複製 nums,實作改到測資本身不會留到下一題
    test_set = [
        ([1, 1, 1, 1, 1], 3, 5, "官方範例:五個 1 湊出 3"),
        ([1], 1, 1, "官方範例:單一元素"),
        ([1], 2, 0, "target 大於所有數字總和,不可能達成"),
        ([1], -1, 1, "target 為負數"),
        ([1, 2], 2, 0, "總和 3 與 target 2 的奇偶性不同,不可能達成"),
        ([2, 2], 0, 2, "+2-2 與 -2+2 是兩種不同的組合"),
        ([1, 2, 3], 0, 2, "+1+2-3 與 -1-2+3"),
        ([1, 1, 2, 3], 1, 3, "有重複數字:不同位置的 1 視為不同的組合"),
        ([0], 0, 2, "邊界:元素為 0,+0 與 -0 各算一種"),
        ([1, 0], 1, 2, "含 0:0 前面的符號有 2 種選擇"),
        ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256, "多個 0:每個 0 各自乘以 2 種符號,2^8"),
        ([0, 1], 1, 2, "多個 0:每個 0 各自乘以 2 種符號,2^8"),
        ([1] * 20, 0, 184756, "規模上限:20 個 1,恰好 10 個正 10 個負,C(20,10)"),
        ([1, 2, 7, 9, 981], 1000, 1, "target 等於總和:只有全部取正這一種"),
        ([1, 2, 7, 9, 981], -1000, 1, "target 等於負的總和:只有全部取負這一種"),
        ([40,19,30,48,8,50,13,31,29,38,35,31,40,47,7,16,31,33,45,6] , 49 ,5305 , "會錯的測資" )
    ]

    for nums, target, expected, note in test_set:
        result = c.findTargetSumWays(nums[:], target)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       nums={nums} target={target}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")

