""" 
    思路 : 
        此題給定一個Array 和數值 k , 要我們return array中第k大的數字 , 注意不是第k個不同的數字 
        題目給的範圍 , array長度在 10^5 級別 , 看起來是可以直接做sort再取值 , 但題目希望我們不做sort
"""


""" 
    解法一. 就先做sort 
"""

from typing import List 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

""" 
    解法二. 不用Sort 但實際上就是建立一個Heap , 把每個元素放進去 , 最後pop k次
"""

from heapq import heapify , heappop , heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [] 
        heapify(heap) 
        
        for num in nums : 
            heappush(heap , -num)  
        
        for i in range(k):         
            result = heappop(heap)  
        
        return -1 * result 
    
""" 
    解法三. 參考別人的解答 , 更加優化一些的使用heapq 
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 一開始只放進 總數-k 的element數量  , 並轉換成heap (min-heap)
        heap = nums[:k]
        heapify(heap) 
        
        # 接下來走過剩餘的元素( 沒被放進 heap 的 )
        # 將這些元素和heap的頂端進行比較 
        # 如果該元素大於這個heap的最小值 , 拿出這個最小值,把新值加入heap

        # --> 換句話說我們的heap最終會keep 前 k 個最大值 ,而頂端是這k個最大值中最小的 , 恰好是題目要的k-th largest element
        for num in nums[k:]: 
            
            if num > heap[0] : 
                heappop(heap) 
                heappush(heap , num)

        return heap[0]
    
    
    
    
    

import heapq 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 把前k個數字放進heap , 我們就是在maintain 一個有k個元素的heap 
        heap = nums[:k]
        heapq.heapify( heap ) 

        for i in range(k , len(nums)): 
            
            element = nums[i] 
            
            if element > heap[0] : 
                heapq.heappop(heap)
                heapq.heappush(heap , element) 
        
        return heap[0]