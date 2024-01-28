""" 
    思路 : 
        要找出兩個array各自不存在對方那邊的數值 , 
        注意相同的數字(如果不存在於另一個array) , 在答案中也只要列出一次 
        
        直覺上是hashtable , 兩次O(N) 去建立
        接下來第一個解就是 尋訪在nums1 hashset的key(如此確保不會遇到重複數字) , 如果不在nums2的hashset內就做添加
"""

from typing import List 
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        hashset1 = { i for i in nums1 }
        hashset2 = { i for i in nums2 }

        sol1 , sol2 = [] , []
        
        
        for item in hashset1 : 
            if not item in hashset2 : sol1.append(item)
        
        for item in hashset2 : 
            if not item in hashset1 : sol2.append(item) 
            
        return [sol1,sol2]