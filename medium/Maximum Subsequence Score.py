""" 
    思路: 
        這題給定兩個長度一樣的Array,其中的元素都是positive integer , 
        要我們計算選擇k個index之後 , 將這些index對應在array1的元素加總 * array2對應的k個元素的最小值 , 
        這樣計算方式可以得到的最大分數 , 注意不必要是連續的k個元素 , 即只要sub-sequence 

    思路:
        我的想法是prefix , 先針對nums2進行sorting , 並同時將num1以對應nums2值大小的方式sort
        這樣就可以將nums2變為由小到大的array, 在這個array中使用大小為k的window , 
        可以快速得到window中num2的最小值 ,
        
        而較為麻煩的部份是要計算nums1在對應範圍的總和 ,因為在上述方式中,我們已經選定要以哪個值作為nums2的最小值,
        因此要在剩餘還可用的nums2範圍對應的nums1中選擇k-1個最大值來作為加總.
        
        這邊我想了很久還是有點複雜,因此看Solution ,這邊比較tricky的解法是用prefix sum+heap 
        在traverse的過程中 ,將nums1的元素不斷加入heap.同時更新prefix_sum 當heap滿到了有k個值後 
        就利用當前的nums2值乘以prefix_sum來更新解
        
        但這邊最tricky的地方在於,這個作法要將nums1 , nums2陣列做reverse traverse , 因為按照上面的作法,
        在heap沒有k個值以前是不會更新解的 , 就相當於nums2最大的前k-1個值永遠不會被作為最小值使用到
        
        
"""

from typing import List 
from heapq import heappop , heappush
class Solution:

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # 將nums1以對應nums2的值來做sort , 接著再對nums2做sort
        nums1 = [  nums1[i] for i in sorted( list(range(len(nums1))) , key = lambda i : nums2[i])   ]        
        
        nums2.sort() 
        sol = float('-inf')
        heap = [] 
        
        prefix_sum = 0 
        for i in range(len(nums1)-1 , -1 ,-1): 
            
            prefix_sum += nums1[i] 
            heappush( heap ,  nums1[i] ) 
            
            if len(heap) == k : 
                
                sol = max(sol , nums2[i] * prefix_sum )  
                
                prefix_sum -= heappop(heap)
       
        return sol 
S = Solution() 
print(S.maxScore([2,1,14,12] , [11,7,13,6] , k=3))