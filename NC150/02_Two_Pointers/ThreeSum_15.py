"""
    題意 :
    給定一個整數陣列 nums，找出所有 i != j != k 且 nums[i] + nums[j] + nums[k] == 0 的
    三元組（triplet），結果不可包含重複的三元組。

    Constraint :
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5

    思路 :
    要找出所有的三元組 ,可以視為 nums[i] = -1 * ( nums[j] + nums[k] ) , 
    那就是先固定第一個 Index , 之後如同 Two Sum 掃一次, 但掃的範圍會三角形縮小 , 並搜集過程中所有解答.

    
    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        for 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例
    test_set = [
        (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
        (([0, 1, 1],), []),
        (([0, 0, 0],), [[0, 0, 0]]),
    ]

    def normalize(triplets):
        # 三元組之間的順序、三元組內部的順序都不重要,排序後再比較
        return sorted(tuple(sorted(t)) for t in triplets)

    for args, expected in test_set:
        result = c.threeSum(*args)
        passed = result is not None and normalize(result) == normalize(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
