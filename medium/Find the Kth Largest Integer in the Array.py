"""
    題意: 給定一個array裡面裝有str-type的數字 ,以及整數k 
        要求返回第K大的數字 , 注意: 如果同個數字出現兩次 , 也要算入, ex: ["1","2","2"] , 當中第二大的數字為"2"
    
    思路:
        看到要找第k大的數字 , 蠻直覺會去想到使用heap , 我用一個size為k的min heap來存數值 , 
        並且走O(N)走過整個array , 將每個數值與min heap頂端做比較 , 若大於min-heap頂端(heap中的最小值) , 則對heap做pop push 
        走完後heap就保存了整個array中前k大的數值 , 而heap頂端就是答案
    
"""
from typing import List 


""" 
    解法一. 就是很簡單的heap經典操作 , TC:O(N)  , MC:O(K)
    
        實際的速度空間都很優
"""
from heapq import heappop , heappush ,heappushpop

class Solution:

    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        minHeap = [] 
        
        # 先在heap中裝入k個值 
        for i in range(k) : heappush(minHeap , int(nums[i])) 
        
        
        for i in range(k , len(nums)):   
            
            # 如果新的數值比heap頂端更大 , 將其加入heap
            if int(nums[i]) > minHeap[0] :   heappushpop(minHeap , int(nums[i]))  
            
        # 走完後heap的頂端就是解
        return str(minHeap[0])

                
            
            
            
            
        