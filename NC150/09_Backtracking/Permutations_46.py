"""
    題意 :
    給定一個由互異整數組成的陣列 nums,回傳它的所有排列。

    排列之間的順序不限。排列內部的元素順序有意義,
    [1,2,3] 與 [1,3,2] 是不同的排列。

    LeetCode 46 · Medium
    URL : https://leetcode.com/problems/permutations/

    Example :
    nums = [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    nums = [0,1]   -> [[0,1],[1,0]]
    nums = [1]     -> [[1]]

    Constraint :
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    nums 中的元素互異

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass


def canon(perms: List[List[int]]):
    """排列之間的順序不影響對錯;排列內部的順序要保留。"""
    if perms is None:
        return None
    return sorted(tuple(group) for group in perms)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出) —— 只忽略排列彼此的順序
    test_set = [
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),                                                    # 官方範例,3! = 6
        ([0, 1], [[0, 1], [1, 0]]),                           # 官方範例,含 0
        ([1], [[1]]),                                         # 官方範例,單一元素
        ([-1, 0], [[-1, 0], [0, -1]]),                        # 負數與 0
        ([1, 2], [[1, 2], [2, 1]]),                           # 長度 2
        ([-10, 10], [[-10, 10], [10, -10]]),                  # 數值上下限
        (
            [3, 1, 2],
            [[3, 1, 2], [3, 2, 1], [1, 3, 2], [1, 2, 3], [2, 3, 1], [2, 1, 3]],
        ),                                                    # 輸入未排序,仍要覆蓋全部順序
    ]

    for nums, expected in test_set:
        result = c.permute(nums)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={nums}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
