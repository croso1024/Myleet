"""
    題意 :
    給定一個長度為 n 的整數陣列 nums (0-indexed),一開始站在 nums[0]。

    nums[i] 代表從 index i 往前跳的「最大」長度,
    也就是站在 i 時,可以跳到任何 i + j,其中 0 <= j <= nums[i] 且 i + j < n。

    回傳抵達 nums[n - 1] 所需的「最少跳躍次數」。
    題目保證一定能抵達 nums[n - 1]。

    LeetCode 45 · Medium
    URL : https://leetcode.com/problems/jump-game-ii/

    Example :
    nums = [2,3,1,1,4] -> 2   (0 -> 1 -> 4)
    nums = [2,3,0,1,4] -> 2

    Constraint :
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 1000
    保證可以抵達 nums[n - 1]

    思路 :
    這一題看起來好像很單純,
    走訪過程中隨時記錄步數與當前可到達的最大範圍. 

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1 : return 0 

        cur_index = 0 
        maximum_arrival = nums[0]
        step = 0 

        while maximum_arrival < len(nums) - 1 : 

            current_maximum_arrival = maximum_arrival 

            for i in range(cur_index , current_maximum_arrival+ 1 ): 

                maximum_arrival = max(maximum_arrival , i + nums[i])

            step += 1 
        
        return step + 1 



if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([2, 3, 1, 1, 4], 2, "官方範例"),
        ([2, 3, 0, 1, 4], 2, "官方範例:中間有 0"),
        ([0], 0, "邊界:只有一個元素,已經在終點"),
        ([1], 0, "邊界:只有一個元素,數值不為 0"),
        ([1, 2], 1, "兩個元素"),
        ([1, 1, 1, 1], 3, "每次只能跳一格"),
        ([5, 1, 1, 1], 1, "第一步就能越過終點"),
        ([1, 2, 3], 2, "第一步只能跳一格"),
        ([3, 0, 0, 1, 1], 2, "中間連續的 0"),
        ([1, 2, 1, 1, 1], 3, "多種路線,步數相同"),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2, "第一步差一格到不了終點"),
        ([3, 4, 3, 1, 0, 7, 0, 3, 0, 2, 0, 3], 3, "較長的陣列"),
        ([1] * 10, 9, "全部是 1,跳 n - 1 次"),
    ]

    for nums, expected, note in test_set:
        result = c.jump(nums[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       nums={nums}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
