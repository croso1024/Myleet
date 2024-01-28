""" 
    思路: 
        這題給定兩個Array , 要我們計算 , 從array1選擇k個元素總和 * array2同樣的k個元素的minimum 的最大值 , 
        注意不必要是連續的k個元素 , 即只要sub-sequence 
        

        
"""


""" 
"""

from typing import List 
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
