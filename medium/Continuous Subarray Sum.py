from typing import List 

""" 
    思路: 
        給定一個Array nums 以及constant k , 問這個nums中是否存在"good subarray" , 
        good subarray的定義為:   
            - 長度至少>=2的sub-array 
            - sub-array的總和為 k的倍數 (也可以是0) 
        
        這一題的特殊在於因為目標是要湊K的倍數 , 因此不能像其他subarray sum的題目那樣 , 如果範圍內的sum > target 就縮小範圍(sliding window)
        最naive的解法雙loop需要take O(N^2) , 應該是不需要才對
        
        
        
"""


""" 
    解法一. 雙loop solution , 邏輯是對的 , 但會time exceed limit
        使用prefix快速的計算某段的sum為和
"""
class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1 : return False 
        
        prefix = [None for i in range(len(nums))]

        temp = 0 
        for i in range(len(nums)): 
            temp += nums[i]
            prefix[i] = temp 
        
        # 用prefix去快速計算某一段的sum
        # ex.  要計算 nums[u:v+1] => prifix[v] - prifix[u] + nums[u]
        
        # 雙loop主體 , 要來找good subarray , 範圍從2 ~ len(nums) ,在此就是 +1格 到+ len(nums)-1 格
        for window_size in range(1 , len(nums)):   
            
            # 要去計算從 i ~ i+window_size 
            for i in range(  len(nums) - window_size ): 
                
                subarray_sum = prefix[i+window_size] - prefix[i] + nums[i] 
                if subarray_sum % k == 0 : return True 
        
        return False 
    
""" 
    解法二.  Remainder hashmap , 
        這個解法是看別人的solution得知 , 我覺得相當tricky , 我們用一個hashmap去存 "累計餘數:index" 
        以原始問題作為例子 :
        nums = [23,2,4,6,7] , k = 6 
        
        - 第一次累積 23 , 23%6 = 5 , hashmap = { 5 : 0 } 
        - 第二次累積 25 , 25%6 = 1 , hashmap = { 5 : 0  , 1 : 1 }  
        - 第三次累積 29 , 29%6 = 5 , -> 當5已經出現在hashmap , 代表前面某一段也累積到餘數為5 , 
          這代表說這一次累積與上一次累積到5的過程 , 就是一個 %k = 0的數值 , 因此當前index和先前累積的index差值>=2就是解 
    
        速度提升到O(N) , 空間則是O(K) , 最佳解    
"""

class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1 : return False 
        # 這代表餘數為0的index在-1 , 就是還沒有任何值開始納入 , 如果 nusm[0] = 0 , 那也會因為 0 - (-1) 只有一個值而無法作為解
        hashmap = {0 : -1 }
        
        
        cumulative_sum = 0 
        for idx in range(len(nums)):  
            
            cumulative_sum += nums[idx] 
            remainder = cumulative_sum % k 
            
            if remainder in hashmap and idx - hashmap[remainder] >= 2 :  
                return True

            elif not remainder in hashmap : 
                hashmap[remainder] = idx 
        
        return False 