"""
    題意 :
    給定兩個已排序(升序)的陣列 nums1、nums2,長度分別為 m、n。
    回傳這兩個陣列合併後的「中位數(median)」。

    整體演算法的時間複雜度必須是 O(log(m+n))。

    LeetCode 4 · Hard
    URL : https://leetcode.com/problems/median-of-two-sorted-arrays/

    Example :
    nums1 = [1,3],   nums2 = [2]     -> 2.00000
    nums1 = [1,2],   nums2 = [3,4]   -> 2.50000
    nums1 = [],      nums2 = [1]     -> 1.00000
    nums1 = [2],     nums2 = []      -> 2.00000

    Constraint :
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -10^6 <= nums1[i], nums2[i] <= 10^6
    nums1 與 nums2 皆為升序排列

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([1, 3], [2]), 2.00000),
        (([1, 2], [3, 4]), 2.50000),
        (([], [1]), 1.00000),                            # 邊界:一個陣列為空
        (([2], []), 2.00000),                            # 邊界:另一個陣列為空
        (([1], [1]), 1.00000),                           # 邊界:兩個長度皆為 1
        (([1, 2], [1, 2]), 1.50000),                     # 兩陣列元素完全重疊
        (([0, 0], [0, 0]), 0.00000),                     # 全相同值
        (([-5, -3, -1], [-4, -2, 0]), -2.50000),         # 全負數
        (([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), 5.50000),  # 兩陣列不重疊,長度相同
        (([1, 3, 5, 7, 9], [2]), 3.00000),               # 長度差距極大
        (([100000], [-1000000, 1000000]), 100000.0),     # 邊界:數值極端,中位數落在單一陣列的元素上
    ]

    for args, expected in test_set:
        result = c.findMedianSortedArrays(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
