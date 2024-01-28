from typing import List 

from heapq  import heappush , heappop ,heappushpop
class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        # 第k個大的元素 , 是在sort完成第k大 ,因此可能有多個相同元素在前    
        heap = [] 
        
        # 我們要找第k大的數值 , 因此keep一個heap , 限制heap的大小為k , 然後走過一遍 ,目標是要讓heap維持整個array前k大的值 
        # 最終 heap頂端就是我們要找的
        
        # 先把前k個值放入heap ;  heapq套件預設是min heap 
        for i in range(k) : 
            heappush(heap , nums[i])  
            
        # 此時heap頂端就是heap中的最小值 
        
        # 把剩下的加進去 
        for i in range(k , len(nums)): 
            
            # 如果新的值大於heap的最小值 , 將其加入 
            if nums[i] > heap[0] : 
                heappushpop(heap , nums[i])  
            else : 
                pass 
            
        # 走完後 , heap就保留了整個array中前k大的數字 
        return heap[0]


test = [3,2,3,1,2,4,5,5,6]
k = 2 
S = Solution() 
print(S.findKthLargest(test , 4))