""" 
    思路 : 
        給定一個Array ,  返回這個array組成目標數字k的 sub-array數 
        ,注意這個sub-array的定義是要continuous的array 

        -> 思路上我覺得可以用sliding window , 但實際上這一題的array裡面可能有正數也可能有負數 ,
        不容易去判斷擴展或縮小window的時機點. 
        
        暴力解就是用, 從大小等於 nums.length的視窗開始掃 ,-> nums.length -1 一路掃到大小為1的視窗 , 去統計個數 
        -> O(N^2) 時間複雜度
        
        思考一下方向 , 應該會需要先計算累積和 , 
        
        left_acc代表累計值 ,  我們要算的是 當前的left_acc - k , 是不是等同於先前曾經累加到的left_acc , 
        這就相當於  ,  0->i 的範圍 - k = 0->j  ( i>j ) , 這樣 i->j 的範圍就是解的概念
        
        

"""

""" 
    解法一. 暴力解 , 就是用不同大小的視窗去掃略 
"""

from typing import List 
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        size = len(nums) 
        sol = 0 
        
        for window_size in range(size-1) :  
            
            for i in range(  size - window_size ) :  
                
                window_content = nums[ i : i+window_size+1  ] 

                if sum(window_content) == k : 
                    sol += 1 
        
        
        return sol
    
    
""" 
    解法二. 預先算好presum , 然後把他們存入hashmap ,  
    
            當計算累計值到達第i個 , 我們回去看  累計到 " i的值 - 先前累計的某個結果 = k " 這件事情是否發生 , 即 i-k == 先前的某個累計位置
            
            # 這邊有個細節 , 我一開始是使用hashset來找上面這件事 , 但實際上可能會有 " i的值 - k 符合多組先前的累計位置 , 那這些都是合法的解答 " 
            因此需要改成使用hashmap , 去紀錄先前一共有多少組是該值 , sol要增加該值的組數 
"""
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        
        sol = 0 
        # 計算好left_acc 
        left_sum = 0 
        hashmap = dict() 
        hashmap[0] = 1 
        
        for i in range(size): 
            left_sum += nums[i] 
            
            
            if left_sum - k in hashmap : 
                sol += hashmap[left_sum-k] 
            
            if left_sum in hashmap: hashmap[left_sum] += 1 
            else : hashmap[left_sum] = 1  
            
        return sol 
        

import random 

test = [random.randint(-1000,1000) for i in range(pow(10,4))] 
k = random.randint(0 , 1000) 
S = Solution()
print(S .subarraySum(test , k ))