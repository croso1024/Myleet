
from typing import List 

from heapq import heappop , heappush 
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # heap solution , maintain a size k heap , and traverse all the element in the heap 
        heap = [] 

        for num in nums: 
            
            heappush(heap , num) 

            if len(heap) > k : heappop(heap) 

            
        return heap[0] 