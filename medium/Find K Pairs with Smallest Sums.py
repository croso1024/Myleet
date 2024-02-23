""" 
    Given two sorted array nums1,nums2 and an integer k . 
    And then , we define a 'pair' is (u,v) , u from nums1 , v from nums2.
    Our goal is find out the first K pair have smallest u+v sum

    First approach i try is use 4 pointer , and use some rule to compare pair value
    and move the pointer , but this approch is pretty complex so can't complete for me.

    The more efficient approach is use heap , and it genius method.
    !!! The core concept is that :
    
    for ( nums1[a] , nums2[b] ) , the next bigger pair must in 
    (nums[a+1] , nums2[b] ) or ( nums[a] , nums2[b+1] ) . 

    so we can use a heap and a set to complete this problem.
    every step:
    we retrieve a pair from the top of heap (a,b)
    and put (a+1,b) , (a,b+1) into heap if the pair not in the visited set.   

"""
from typing import List 
from heapq import heappop , heappush 
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        visited = set()
        heap = [  ( nums1[0]+nums2[0] ,0 ,0   )    ]
        visited.add( (0,0) )
        sol = [] 

        while len(sol) < k : 

            pairInfo = heappop(heap) 

            (_ , u,v) = pairInfo

            sol.append([ nums1[u], nums2[v] ]) 
            if u+1 < len(nums1) and not (u+1,v) in visited: 
                heappush(  heap ,  (nums1[u+1] + nums2[v]  , u+1 , v) )
                visited.add((u+1,v))

            if v+1 < len(nums2) and not (u , v+1 ) in visited:
                heappush( heap , (nums1[u] + nums2[v+1]  , u , v+1) )
                visited.add((u,v+1))

        return sol
