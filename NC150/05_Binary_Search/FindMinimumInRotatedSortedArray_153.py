"""
    題意 :
    有一個長度為 n、原本為「升序排列」的陣列,被旋轉了 1 到 n 次。
    例如 nums = [0,1,2,4,5,6,7] 可能變成 :
      - [4,5,6,7,0,1,2]  (旋轉 4 次)
      - [0,1,2,4,5,6,7]  (旋轉 7 次,等於轉回原樣)

    旋轉一次的定義 : [a[0], a[1], ..., a[n-1]] -> [a[n-1], a[0], a[1], ..., a[n-2]]

    給定這個「已排序並旋轉過」且元素皆相異的陣列 nums,回傳其中的最小元素。

    必須寫出 O(log n) 的演算法。

    LeetCode 153 · Medium
    URL : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    Example :
    nums = [3,4,5,1,2]     -> 1
    nums = [4,5,6,7,0,1,2] -> 0
    nums = [11,13,15,17]   -> 11

    Constraint :
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums 中所有整數皆相異
    nums 為升序排列後旋轉 1 到 n 次的結果

    思路 :
    最小值應該出現在斷點後第一格. 或著根本沒有斷點. 
    而如果最後一個元素 > 第一個元素 , 代表相當於完全沒有轉.

    至於搜尋的迭代 , 找出當前位置的 mid 後 , 實際解答應該在哪一塊!? 
    => 檢查和 mid 值差距較大的指標 ,那塊才應該有斷點. 
    


    複雜度 : Time O(?) / Space O(?)
    時間複雜度為 O(logN), 空間複雜度O(1)

    Trade-off :

"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left = 0 
        right = len(nums) - 1 
        # Binary Search 
        while right >= left : 

            left_value = nums[left]
            right_value = nums[right]

            if right_value > left_value : return left_value 

            mid = ( right + left ) // 2 
            mid_value = nums[mid]

            # 比較mid value和左/右指標的數值差距誰大. 
            diff_with_right = abs( right_value - mid_value ) 
            diff_with_left = abs( left_value - mid_value ) 

            # 若 mid 和右指標差值大 , 則斷點在 mid ~ 右指標之間 
            if diff_with_right > diff_with_left : 
                # 核心關鍵 ,  mid 和右邊差距較大的情況 , left 可以多走一格,因為最小值一定在其右側範圍
                left  = mid + 1 
            
            # 若 mid 和左指標差值大 , 則斷點在 左指標 ~ mid 之間  
            elif diff_with_right < diff_with_left: 
                # 這裡不收一步 , 因為 mid 仍然有可能是最小值
                right = mid 
            # 差值一樣表示收斂了
            else : 
                break 
        
        return nums[left]
            


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([3, 4, 5, 1, 2],), 1),
        (([4, 5, 6, 7, 0, 1, 2],), 0),
        (([11, 13, 15, 17],), 11),
        (([1],), 1),                                    # 邊界:單元素
        (([2, 1],), 1),                                 # 邊界:兩元素,有旋轉
        (([1, 2],), 1),                                 # 邊界:兩元素,未旋轉
        (([5, 1, 2, 3, 4],), 1),                        # 最小值落在 index 1
        (([2, 3, 4, 5, 1],), 1),                        # 最小值落在最末端
        (([3, 1, 2],), 1),                              # 奇數長度,最小值在中間
        (([-5000, 5000],), -5000),                      # 邊界:數值上下限
        (([-1, 0, 1, 2, -3, -2],), -3),                 # 全區間含負數
        (([4, 5, 6, 7, 8, 1, 2, 3],), 1),               # 偶數長度,旋轉點偏右
    ]

    for args, expected in test_set:
        result = c.findMin(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
