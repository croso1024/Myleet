
""" 
    思路 :  
        這一題有點不像easy , 給定兩個Array , nums1,nums2 , 
        要返回一個長度等於nums1的array , 裡面的每個值是 nums1的元素對應到nums2的next greater element索引 
        
        抽象一點的解法應該是 , 先針對nums2做 單調堆疊 , 以O(nums2.length)去解出next greater element , 再把他們存在hashmap 
        之後O(nums1.length)就可以取得解
        
        這樣total time complexity就是題目要的 O(nums1.length + nums2.length) , 但空間要 O(nums2.length) 
"""


""" 
    解法一. 單調堆疊 , 時間複雜度很優 , 但我用了hashmap存 , 導致空間不佳
"""

from typing import List 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # 先計算nums2的 next greater element : 
        sol = [0 for i in range(len(nums2))] 
        stack = [] 

        for i in range( len(nums2)-1 , -1 ,-1 ): 
            
            while stack and stack[-1] <= nums2[i] : 
                stack.pop() 
                
            sol[i] = stack[-1] if stack else -1 
            stack.append( nums2[i] )    
            
        # 此時sol就是 nums2的 next greater element array , 我們要將其放進hashmap 
        # hashmap : key為原始nums2的元素 , value為他們在nums2內對應的next greater element  
        hashmap = { nums2[i]:sol[i] for i in range(len(nums2))} 
        
        return [ hashmap[element] for element in nums1 ]


""" 
    解法二. 
        同解法一,略微的優化空間 , 只存必要的(nums1中有的值)對應的next greater element
        同樣我們也不需要保存完整的solution array , 這邊實際上有利用到dict創建使用 list comprehensive ,
        所以在key的順序是符合nums1的
    
"""

from typing import List 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # 先計算nums2的 next greater element : 
        stack = [] 

        ref = { element : None for element in nums1}
        
        for i in range( len(nums2)-1 , -1 ,-1 ): 
            
            while stack and stack[-1] <= nums2[i] : 
                stack.pop() 
                

            if nums2[i] in ref : ref[nums2[i]] = stack[-1] if stack else -1 
             
            stack.append( nums2[i] )    
            
        return list(ref.values())
        