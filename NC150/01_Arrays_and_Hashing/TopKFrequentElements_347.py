"""
    題意 :
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.

    給定數字陣列和K , 要找出前K個出現最多次的.

 
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
 
    思路 :

    很Naive的想法是 , HashMap 走一輪存下每一個數字出現次數.
    時間O(N) + 空間O(N),
    接著初始化 MaxHeap , 把所有種數字都放進去, O(NLogN) , 再 swim K 次 O(KlogN) 
    這樣總時間 O(NLogN) , 空間 O(N)

    和AI討論後,可以使用 TopK Heap ,
    也就是每次 heappush 完成 , 檢查size踢掉最小的. 
    可以優化一下時間複雜/空間複雜度.
    設 U 為 Unique Number ,
    時間複雜度應該是 O(N) + O(ULogU) , 空間 O(U)

    ===

    和AI討論後的思路 Bucket Solution 應該是最優解
    已知最高頻率出現最多也就 N 個 ,
    先 Hashmap 把所有數字的頻率記錄下來 O(N)時間+O(U)空間,
    再一組 N+1 長度的 Array , 把出現 N ~ 0 次的數字寫進Array , 
    逐一挑K個出來. 
    這樣總時間空間都在O(N)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from typing import List 
from heapq import heappush , heappop


class item : 
    def __init__(self, num , value): 
        self.num = num 
        self.value = value 
    def __eq__(self , other): 
        return self.value == other 
    def __gt__(self,other): 
        return self.value > other 
    def __lt__(self,other): 
        return self.value < other 

# class Solution:

#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         hashmap = {} 
#         max_heap = [] 

#         for num in nums :
#             if num in hashmap : 
#                 hashmap[num] += 1 
#             else :
#                 hashmap[num] = 1 
        
#         for num in hashmap : 
#             heappush(max_heap , item( num , -1*hashmap[num]))
        
#         result = [  heappop(max_heap).num for i in range(k) ]
#         return result
        

class Solution : 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {} 
        size = len(nums) 
        # O(N) 時間空間 , 填充 hashmap 
        for num in nums : 
            if num not in hashmap: 
                hashmap[num] = 1 
            else : 
                hashmap[num] += 1 

        # N 個元素 , 元素則出現 0 ~ N 次
        bucket = [ [] for i in range(size+1)  ]

        # 回填 Bucket 
        for num in hashmap : 
            count = hashmap[num] 
            bucket[count].append(num) 

        # 選出 Top-N 
        results = [] 
        for i in range( size , -1 ,-1) : 

            while bucket[i] and len(results) < k : 

                results.append(bucket[i].pop()) 
        return results
            

c = Solution()
c.topKFrequent([1,1,1,2,2,3],2)
c.topKFrequent([1],1)
c.topKFrequent( [1,2,1,2,1,2,3,1,3,2],2)