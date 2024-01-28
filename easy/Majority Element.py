""" 
    思路 : 
        給定一個array , 返回array中的majority element 
        majority的定義是這個數字在array中的出現次數超過一半 
        
        這一題follow-up 希望可以用O(1) space來解
"""

""" 
    解法一. 
        先不考慮follow up的部份 , 依照定義 , majority element的出現次數會超過array的長度至少一半
        很直接的作法是hashtable , O(N)的時間與空間

        這個作法的速度跟空間就很不錯了
"""

from typing import List 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashtable = dict()
        size = len(nums) 
        
        
        for num in nums : 
            
            if num in hashtable: 
                hashtable[num] += 1 
                if hashtable[num] > (size//2) : return num 
            else :
                hashtable[num] = 1 
                if hashtable[num] > (size//2) : return num 

""" 
    解法二. 
        考慮看如何使用O(1) space , 
        我這邊的想法是先排序 , 然後去數數 , 如果一個數字的出現次數>size//2 , 那就是解答
        
        速度很差 , 但空間最優了
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() 
        
        probe = 0 
        size = len(nums) 

        prev = None 
        count = 0 
        
        while probe < size : 
            
            if not prev == None and nums[probe] == prev : 
                count += 1 
                if count > (size//2): return nums[probe]
                probe += 1 

            else : 
                prev = nums[probe]
                count = 1 
                probe += 1
            
        # 只有給一個數值的情況下會需要在return prev
        return prev 
                
                
                