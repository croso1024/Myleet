""" 
    思路 :  
        給定一個Array , 裡面有許多長度為n的binary string , 求任何一個並沒有出現在其中的binary string並返回
        題目給定n = 16 , 亦即 0 ~ (2^16-1)

        直觀的想法就是把字元轉換成數字 , 去放進set , 或著直接將原始nums array放入hashset , 
        再去比較
"""


""" 
    直觀作法 , 就是去比對 
"""

from typing import List 

class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        hashset = set()
        for binString in nums : 
            hashset.add(  int(binString , 2) ) 
        
        for i in range(pow(2,16)): 
            
            if not i in hashset : 
                
                sol = bin(i)[2:]             
                sol = "0" * (n-len(sol)) + sol 
                return sol 

""" 
    解法二. 
        很天才的作法  , 有點類似以前某個數學課的概念 , 我們在每一個步驟都選擇一個不同的數字 ,
        之所以可以這樣做 , 很重要的原因在於 nums.length = n , 一定可以找到每一位都不同的值
"""

class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums) 
        
        sol = "" 
        
        for i in range(n): 
            
            if nums[i][i] == "0":
                sol += "1" 
            else : 
                sol += "0"
        return sol 