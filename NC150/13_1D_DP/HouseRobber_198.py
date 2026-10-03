"""
    題意 :
    一條街上有一排房子,nums[i] 是第 i 間房子裡的金額。
    不能偷相鄰的兩間,否則會觸發警報。
    回傳今晚能偷到的最高金額。

    LeetCode 198 · Medium
    URL : https://leetcode.com/problems/house-robber/

    Example :
    nums = [1,2,3,1]   -> 4
    nums = [2,7,9,3,1] -> 12

    Constraint :
    1 <= nums.length <= 100
    0 <= nums[i] <= 400

    思路 :
    這一題看起來是標準的DP , 但需要思考一下怎樣做紀錄. 
    在紙上做個筆記.可以比較直觀的推出來.
    將 [1,2,3,1] 拆開成,
    如果只有 [1] , 在偷了這個Array最後一間房/沒偷的情況下可以拿到的最高金額. 

    Array_n 可以偷到的最高金額 : 
    - 偷 nums[n] : max( nums[n] + Array_(n-1) 不偷 nums[n-1] 的情況下最高 )
    - 不偷 nums[n] : Array_(n-1) 可以偷到的最高金額
    
    複雜度 :
    實作上,時間複雜度O(N), 而空間Naive解答是O(N), 但應該可以只追蹤前兩格降到O(C)

    Trade-off :

"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # record : List[Tuple] ,
        # record[i][0] : 偷nums[i] 的情況下最高金額 
        # record[i][0] : 不偷 nums[i]的情況下的最高金額 /
        record = []

        for i, num in enumerate(nums) :  

            maximum_amount_with_num_i = num + max(record[i-2]) if i-2>=0 else num
            maximum_amount_without_num_i = max(record[i-1]) if i-1 >= 0 else 0
            record.append((maximum_amount_with_num_i ,maximum_amount_without_num_i))
        
        return max(record[-1])


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明)
    test_set = [
        ([1, 2, 3, 1], 4, "官方範例:偷第 1、3 間"),
        ([2, 7, 9, 3, 1], 12, "官方範例:偷第 1、3、5 間"),
        ([0], 0, "邊界:只有一間,金額是 0"),
        ([400], 400, "邊界:只有一間,金額上限"),
        ([2, 1], 2, "兩間相鄰,只能偷金額較高的那間"),
        ([1, 2], 2, "兩間相鄰,偷第二間"),
        ([2, 1, 1, 2], 4, "頭尾不相鄰,可以一起偷"),
        ([0, 0, 0], 0, "每一間都是 0"),
        ([1, 3, 1, 3, 100], 103, "最後一間很大,中間要讓路"),
        ([100, 1, 1, 100], 200, "兩端都可以偷"),
        ([2, 1, 1, 2, 1], 4, "五間,頭尾那組較高"),
        ([400, 400, 400], 800, "金額上限,隔一間偷"),
    ]

    for nums, expected, note in test_set:
        result = c.rob(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
