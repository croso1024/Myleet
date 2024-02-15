""" 
    題意:   
        給定一個circular array num of length n , 返回可得到subarray的最大總和
        note. 題目的subarray看起來就是連續的一段array element
    
    思路:
        這一題的暴力解看起來可以O(N^2)硬來 , 而實際的解法蠻tricky的 , 要分成兩段
        因為這一題是circular array , 對此最大的subarray有兩種情況 , 分別是沒有橫跨斷點 , 以及需要橫跨
        - 1.在沒有橫跨的case ( Maximum sum of subarray ) 我們可以用DP去輕易得到解.
        - 2.而對於有橫跨的case , 我們可以利用DP的手法去找 Minimum sum of subarray , 
            並用整個array的sum去扣除他來找橫跨的部份 , 但這邊依據test case有個很容易疏忽的部份 ,
            即我們在計算minimum sum of subarray的時候,若這個最小subarray用到了整個array , 那會導致用array sum去扣時得到0
            但會有這種情況就是array中所有元素都小於0 , 在這種情況下答案會錯
            
            因此第二部份計算的 minimum sum of subarray , 就不是"全範圍"找minimum sum , 而是在略過兩邊邊界的情況找
            這樣就會讓第二部份只有找"真的有橫跨的case" (至少要在左右兩端各取一個元素才叫做橫跨)
            
            
            
            
            
            
"""
from typing import List 


""" 
    解法一. 暴力解,展開所有的可能解 , 注意我使用 nums[(i+j+N)%N] 來透過j自然地繞circular array
        但這個解法會Time limit exceed 
"""
class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        N = len(nums) 
        sol = float("-inf")
        
        for i , num in enumerate(nums) : 
            
            j = 0 
            temp = 0 
            while j < N : 
                temp += nums[ (i+j+N) % N ] 
                sol = max(sol , temp) 
                j += 1 
                
        return sol 

""" 
    解法二.
"""
class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if len(nums) == 1 : return nums[0]
        # 使用DP去解Case1的情況, 在case1. 我們想像是一個正常array而非circular array
        # dp[i] : 以i為subarray結尾的情況下最大的值
        dp = [None for i in range(len(nums))]  
        dp[0] = nums[0] 
        
        sol = nums[0]
        
        for i in range(1 , len(nums)) : 
            
            if dp[i-1] > 0 :  
                dp[i] = dp[i-1] + nums[i]
            else : 
                dp[i] = nums[i] 
                
            sol = max(sol , dp[i]) 
        # 第二部份 , 我們改成求 minimum sum of subarray 來找有被切分的maximum sub array
        dp = [None for i in range(len(nums))] 

        dp[1] = nums[1] 

        array_sum = sum(nums) 
        sol = max(sol , array_sum - nums[1])
        
        for i in range(2 , len(nums)-1): 
            
            if dp[i-1] > 0 : 
                dp[i] = nums[i] 
            else : 
                dp[i] = dp[i-1] + nums[i] 

            sol = max(sol , array_sum - dp[i] ) 
            
        return sol 

C = Solution()
print(C.maxSubarraySumCircular([-3,-2,-3]))

            
            