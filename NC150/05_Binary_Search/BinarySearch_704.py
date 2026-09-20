"""
    題意 :
    給定一個「升序排列」的整數陣列 nums 與整數 target,
    在 nums 中搜尋 target。存在則回傳其 index,否則回傳 -1。

    必須寫出 O(log n) 的演算法。

    LeetCode 704 · Easy
    URL : https://leetcode.com/problems/binary-search/

    Example :
    nums = [-1,0,3,5,9,12], target = 9 -> 4
    nums = [-1,0,3,5,9,12], target = 2 -> -1

    Constraint :
    1 <= nums.length <= 10^4
    -10^4 < nums[i], target < 10^4
    nums 中所有整數皆相異
    nums 為升序排列

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left , right = 0 , len(nums) - 1 

        while left <= right :
            
            mid = (right+left) // 2 
            value = nums[mid]
            if value == target : return mid 
            elif value > target : 
                # 到底該用 right = mid / mid + 1 
                right = mid - 1
            else : 
                # 到底該用 left = mid / mid + 1 
                left = mid + 1
        
        return -1 

if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
        (([5], 5), 0),                          # 邊界:單元素命中
        (([5], -5), -1),                        # 邊界:單元素未命中
        (([1, 2, 3, 4, 5], 1), 0),              # 命中最左端
        (([1, 2, 3, 4, 5], 5), 4),              # 命中最右端
        (([1, 2, 3, 4], 2), 1),                 # 偶數長度,mid 取捨
        (([1, 2, 3, 4], 7), -1),                # target 大於所有元素
        (([-10, -5, 0, 5, 10], -10), 0),        # 負數與命中最左端
        (([-10, -5, 0, 5, 10], 10), 4),
    ]

    for args, expected in test_set:
        result = c.search(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
