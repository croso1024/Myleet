"""
    題意 :
    給定一個 Array[int] , 每一個數字代表bar的高度. 
    去尋找給定 Array[int] 當中可以達到的最大水量. 

    最大水量 = 寬 x min( bar1 , bar2 ) 
    Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104


    思路 :

    水量 = 寬 x min(bar1 , bar2) 
    寬 : abs(index1-index2) 

    直覺想法是雙指標從兩端或Sliding Window.
    兩招都需要找個想法來讓每指標移動.

    這邊採左右雙指標.每一次動之前嘗試紀錄最大值.
    接著評估動哪一邊 ,優先動較低的,保持較高的還在.並重新評估.
    關鍵是細節處理處 , 兩邊只要 right-left > 1 就還能再動
    

    複雜度 : Time O(?) / Space O(?)

    此雙指標方式 , 時間複雜度O(N)  , 空間O(C)

    Trade-off :

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        size = len(height) 
        left , right = 0 , size-1 
        max_volume = float("-inf")

        while left < right : 

            max_volume =max( max_volume,  (right-left) * min(height[left],height[right]) ) 
            # Compare the next step of the left/right pointer 
            if right - left > 1 : 

                if height[right] > height[left] : 
                    left += 1 
                else :
                    right -= 1 
            else :
                return max_volume
        return max_volume
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([6,9,2,5,3,1]))
print(s.maxArea([6,9,2,5,4,1]))
print(s.maxArea([5,2,4,2]))
print(s.maxArea([8,7,2,1]))
