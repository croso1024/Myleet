"""
    題意 :
    給定 n 個非負整數構成的高度圖 height,每根柱子寬度均為 1,
    計算下雨過後總共能接住多少單位的水。

    LeetCode 42 · Hard
    URL : https://leetcode.com/problems/trapping-rain-water/

    Example :
    height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
    height = [4,2,0,3,2,5]             -> 9

        以 [0,1,0,2,1,0,1,3,2,1,2,1] 為例 ('#' 為柱子,'~' 為積水):

              3               #
              2       #  ~  ~ #  #  ~  #
              1    #  #  ~  # #  #  #  #
              0 _  #  _  #  # #  #  #  # #
                0 1  0  2  1 0  1  3  2 1  2  1


    Constraint :
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5

    思路 :

    每一格能累積的水相當於自身左側數來最高的,和右側數來最高的當中取小 , 減掉自身高度. 
    => 因此核心是要記錄,每一格以來的最高 (從左數來 & 右數來)
    第 i 格的水 : max( 0,   min(  max(height[:i]) , max(height[i+1:]) ) - height[i] ) 
    實際時間複雜度 , 可以走三次O(N)搞定, 儲存則 O(N)
    極端一點 , 可以走兩次O(N) , 第二次就順便持續累算最高+計算每格

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        # array1[i] : 0~(i-1) 格最高的 
        array1 = [0 for i in range(len(height))]
        # array1[i] : (i+1)~(len(height)-1) 格最高的 
        array2 = [0 for i in range(len(height))]

        highest = float("-inf")
        for i in range(len(height)) : 
            if i == 0 : continue 
            highest = max( highest , height[i-1] ) 
            array1[i] = highest
        highest = float("-inf")
        for i in range(len(height) -1 , -1 ,-1 ): 
            if i == len(height) - 1 : continue 
            highest = max(highest , height[i+1])
            array2[i] = highest 
        
        # 最後計算答案 
        # 第 i 格能裝的水 =  max (0 ,   ( min( array1[i] , array2[i] ) - height[i] ) )
        total_volume = 0 
        for i in range(len(height)): 
            total_volume += max( 0 , ( min( array1[i] , array2[i] ) - height[i] ) ) 
        return total_volume

if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
        (([4, 2, 0, 3, 2, 5],), 9),
        (([1],), 0),                    # 邊界:單根柱子,無法形成容器
        (([1, 2, 3, 4],), 0),           # 嚴格遞增,接不到水
        (([4, 3, 2, 1],), 0),           # 嚴格遞減,接不到水
        (([0, 0, 0],), 0),              # 全為 0
        (([2, 0, 2],), 2),              # 最小的凹槽
        (([5, 0, 5],), 5),              # 單一深槽
        (([3, 0, 0, 2, 0, 4],), 10),    # 多層階梯,右牆最高
        (([4, 2, 3],), 1),              # 短牆決定水位(取 min 而非 max)
    ]

    for args, expected in test_set:
        result = c.trap(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
