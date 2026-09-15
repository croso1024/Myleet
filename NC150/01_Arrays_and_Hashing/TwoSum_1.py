"""
    題意 :
    給定一個整數陣列 nums 和一個整數 target。
    請找出陣列中「兩個數字」，使其相加等於 target，回傳這兩個數字的 index。
    同一個元素不能使用兩次，題目保證恰好存在一組解，回傳的 index 順序不限。

    Constraint :
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    只會有一個有效答案

    思路 :

    已知Array無序,可以先做一次sorted , 那就變成有序 -> 做Sliding Windows,
    在此情況下時間變成排序 O(NlogN) , 空間做 O(1) 存指標. 
    應該要嘗試找看看 時間 , O(N) 空間 O(1) 的解法.

    思考了一下有想到這是經典題 , 用一個Hashmap去存看過的,
    後面再算 Target - 當前看得值時就能從Hashmap用 O(1) 去找. 
    而寫 HashMap O(1) , 使得算法複雜度為 O(N) , 空間則為 O(N) 

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Seen number : index 
        seen = dict() 
        for index in range(len(nums))  : 
            residual = target - nums[index] 
            if residual in seen : 
                return [ seen[residual] , index ]
            seen[nums[index]] = index 
        # Un-reachable
        return [-1,-1] 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例
    test_set = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ]

    for args, expected in test_set:
        result = c.twoSum(*args)
        # 回傳的兩個 index 順序不拘,用 sorted 比較
        passed = result is not None and sorted(result) == sorted(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
