"""
    題意 :
    給定一個整數陣列 nums。
    找出一個連續子陣列,使它的元素乘積最大,回傳那個乘積。
    子陣列至少要有一個元素。

    LeetCode 152 · Medium
    URL : https://leetcode.com/problems/maximum-product-subarray/

    Example :
    nums = [2,3,-2,4] -> 6
    nums = [-2,0,-1]  -> 0

    Constraint :
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    任一子陣列的乘積都落在 32-bit 整數範圍內

    思路 :

    直覺看上去是 1D DP , 狀態與選擇是甚麼? 
    思路是 :  假設以 nums[i] 為入選子陣列最後一個元素 ,那麼其可構成的子陣列最大值為 : max(nums[i] , nums[i] * 以前一個元素收尾的連續子陣列最大乘積 )
    因為子陣列不能拆 , 不是子集. 

    以這個想法就能寫出狀態轉移 : 
    dp[i] = max( nums[i] , dp[i-1] * nums[i] ) , 搭配狀態壓縮與 hook 來記最大值. 
    以上, 僅這樣寫會卡在 [-2,-3,-4] / [2,3,-2,4,-1] 這一種先取小,後面有機會更大的題目. 

    ===
    所以需要思考, 考慮到乘法的特性 ,要正確推出以 i 結尾的子陣列最大值. 還需要甚麼? 
    我的想法是還需要記最小值 , 因為最小值有可能下一輪被翻成最大值. 
    每一輪同時要記住以 i 結尾子陣列的"最小 & 最大"

    故本身要記住的是 prev_max / prev_min 
    cur_max = max( nums[i] , nums[i] * prev_max , nums[i] * prev_min )
    cur_min = min( nums[i] , nums[i] * prev_max , nums[i] * prev_min )
    而最佳解來自最好的 cur_max 

    
    時間複雜度 O(N) , 
    空間複雜度 O(1)

    Trade-off :

"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        biggest_multiple_sum = nums[0] 
        prev_max = nums[0]
        prev_min = nums[0]
        for i in range(1 , len(nums)) : 

            cur_max = max( nums[i] , nums[i] * prev_max , nums[i] * prev_min ) 
            cur_min = min( nums[i] , nums[i] * prev_max , nums[i] * prev_min )
            
            biggest_multiple_sum = max(biggest_multiple_sum , cur_max ) 
            prev_max = cur_max 
            prev_min = cur_min 
        
        return biggest_multiple_sum


if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    # 每次呼叫都複製 nums,實作改到測資本身不會留到下一題
    test_set = [
        ([2, 3, -2, 4], 6, "官方範例:正數段 [2,3]"),
        ([-2, 0, -1], 0, "官方範例:0 隔開兩個負數,答案是 0"),
        ([-2], -2, "邊界:只有一個負數"),
        ([0], 0, "邊界:只有一個 0"),
        ([2], 2, "邊界:只有一個正數"),
        ([-2, -3], 6, "兩個負數相乘轉正"),
        ([-2, -3, -4], 12, "三個負數,取尾端兩個"),
        ([0, 2], 2, "前導 0,答案在 0 的右邊"),
        ([2, 0, 3], 3, "0 把陣列切開,取較大的那一段"),
        ([3, -1, 4], 4, "跨過負數會變小,答案是單一正數"),
        ([2, -5, -2, -4, 3], 24, "奇數個負數,要丟掉一個負數"),
        ([1, -2, 3, -4], 24, "偶數個負數,整段乘起來最大"),
        ([-1, 0, -2], 0, "負數被 0 隔開,沒有正的乘積"),
        ([2, 3, -2, 4, -1], 48, "尾端再乘一個負數,整段變成最大"),
    ]

    for nums, expected, note in test_set:
        result = c.maxProduct(nums[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
