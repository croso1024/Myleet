"""
    題意 :
    給定整數陣列 nums 與整數 k,回傳陣列中第 k 大的元素。

    這裡的「第 k 大」是排序後的第 k 名,不是第 k 個不重複的值。
    相同的值會各自佔一個名次。

    LeetCode 215 · Medium
    URL : https://leetcode.com/problems/kth-largest-element-in-an-array/

    Example :
    nums = [3,2,1,5,6,4],       k = 2 -> 5
    nums = [3,2,3,1,2,4,5,5,6], k = 4 -> 4

    Constraint :
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

    思路 :
    Native , 直接給一個Heap搞定.
    用 min heap , 最小的在最上面.
    如果遇到一個元素小於heap的頂 , 就可以加入. 
    只要確保維持 heap 大小為k , 結束後heap頂端就是第K大的數值

    複雜度 : 
    - N個元素進入 Heap , Heap只有K個元素 : O(NlogK) 
    - Heap內持續維持K個數值. 空間 O(K)

    Trade-off :

"""

from typing import List
from heapq import heappop , heappush

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [] 

        # Given 1 <= k <= len(nums) 
        # 逐一放入 Heap 
        for num in nums : 
            # heap沒有滿之前直接放 
            if len(heap) < k : 
                heappush(heap , num)
            
            # heap如果 == k 滿了,比較數值,若數值大於等於當前 heap頂端,就比較頂端
            elif  num >= heap[0]  :  
                heappop(heap)
                heappush(heap ,num) 
            
            #如果新元素小於heap頂端直接丟掉
            else : 
                pass 
        
        # 完成後, heap頂端就是答案. 
        return heap[0] 
                    




if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (([3, 2, 1, 5, 6, 4], 2), 5),                 # 官方範例
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),        # 官方範例,含重複值
        (([1], 1), 1),                                # 邊界:單一元素
        (([7, 7, 7], 2), 7),                          # 全部相同,重複值各佔一名
        (([1, 2, 2, 3], 2), 2),                       # 第 k 名正好落在重複值上
        (([-1, -2, -3], 1), -1),                      # 全負數,k = 1 是最大值
        (([-1, -2, -3], 3), -3),                      # 全負數,k = n 是最小值
        (([5, 4, 3, 2, 1], 1), 5),                    # 已降序,第 1 大
        (([1, 2, 3, 4, 5], 5), 1),                    # 已升序,第 n 大
        (([-10000, 10000, 0], 2), 0),                 # 數值上下限
        (([2, 1], 2), 1),                             # 長度 2,取較小的那個
    ]

    for args, expected in test_set:
        result = c.findKthLargest(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
