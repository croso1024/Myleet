"""
    題意 :
    給定一個只含正整數的陣列 nums。
    判斷能不能把它切成兩個子集,讓兩邊的元素和相等。
    每個元素只能放進其中一邊。

    LeetCode 416 · Medium
    URL : https://leetcode.com/problems/partition-equal-subset-sum/

    Example :
    nums = [1,5,11,5] -> True
    nums = [1,2,3,5]  -> False

    Constraint :
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

    思路 :
    這一題給出只能切一刀，能不能切出一刀讓兩邊大小相等的結果。
    在每一個元素有兩個選擇枝的情況下 , 暴力展開就是 2^200 , 

    想法上 , 先做 Sorted , 再嘗試走訪 , 假想將刀切在走訪位置 , 去算兩邊是否能平衡
    時間複雜度為 O(NLogN)  Sorting , 空間為 O(1)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sorted_nums = sorted(nums) 

        left = 0 
        right = sum(sorted_nums) 

        if left == right : return True 

        for i in range(len(sorted_nums)): 
            left += sorted_nums[i] 
            right -= sorted_nums[i] 
            if left == right : return True
        
        return  False 




if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([1, 5, 11, 5], True, "官方範例"),
        ([1, 2, 3, 5], False, "官方範例"),
        ([1, 2, 5], False, "三個正整數"),
        ([1, 2, 3, 4], True, "四個連續正整數"),
        ([2, 2], True, "兩個相同的數"),
        ([1, 1], True, "兩個 1"),
        ([100], False, "只有一個數"),
        ([1], False, "邊界:長度 1"),
        ([1, 1, 1, 1], True, "四個 1"),
        ([3, 3, 3, 4, 5], True, "五個數"),
        ([1, 2, 3, 6], True, "四個數"),
        ([2, 2, 2], False, "三個 2"),
        ([1, 5, 5, 11], True, "四個數,含重複"),
        ([10, 10], True, "兩個 10"),
        ([1, 1, 2], True, "三個數"),
    ]

    for nums, expected, note in test_set:
        result = c.canPartition(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
