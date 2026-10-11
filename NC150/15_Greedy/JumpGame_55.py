"""
    題意 :
    給定一個非負整數陣列 nums。一開始站在第一個位置。
    nums[i] 表示從下標 i 最多可以往右跳幾個位置。
    若能到達最後一個下標,回傳 True,否則回傳 False。

    LeetCode 55 · Medium
    URL : https://leetcode.com/problems/jump-game/

    Example :
    nums = [2,3,1,1,4] -> True
    nums = [3,2,1,0,4] -> False

    Constraint :
    1 <= nums.length <= 10^4
    0 <= nums[i] <= 10^5

    思路 :
    每一步應該都可以記錄下當前最高可以到達的步數.
    依據題目給的範例; 
    step 0 : 最遠可以到2 , 
    step 1 : 最遠可以到4 , 
    也就是在走的過程持續更新目前可以抵達的最遠位置. 
    如果能全部走完則完成, 時間複雜度 O(N) , 空間O(1)


    Trade-off :

"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_index_can_reach = 0 
        current_index = 0 
        while current_index <= maximum_index_can_reach : 
            maximum_index_can_reach = max(maximum_index_can_reach , current_index + nums[current_index]) 
            if maximum_index_can_reach >= len(nums) - 1 : return True 
            current_index += 1 
        return False 


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期, 說明)
    test_set = [
        ([2, 3, 1, 1, 4], True, "官方範例:有一種跳法能到終點"),
        ([3, 2, 1, 0, 4], False, "官方範例:卡在值為 0 的位置"),
        ([0], True, "邊界:只有一格,一開始就在終點"),
        ([1, 0], True, "跳一格剛好到終點"),
        ([0, 1], False, "起點是 0,而且後面還有格子"),
        ([2, 0, 0], True, "起點一次跳過中間的 0"),
        ([1, 0, 1], False, "跳到中間的 0 之後出不去"),
        ([2, 0, 1, 0], True, "起點跳到下標 2,再跳到終點"),
        ([1, 1, 0, 1], False, "走到下標 2 的 0,到不了最後一格"),
        ([1, 1, 1, 1], True, "每次只跳一格,仍能走完全程"),
        ([4, 0, 0, 0, 0], True, "起點的步數剛好等於到終點的距離"),
        ([3, 2, 1, 0, 0], False, "最遠只能到倒數第二格"),
    ]

    for nums, expected, note in test_set:
        result = c.canJump(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
