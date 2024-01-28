""" 
    思路 :
        給定一組Sorted array , 範圍可能是從負到正 , 要返回裡面的值經過平方後的sorted array
        ex. [-4,-1,0,3] -> [0,1,9,16] 
        
        直接做follow-up , 題目要求O(n)的時間 , 但沒有需要不需要in-place操作
        
        我的思路是 , 平方完成後的最小值可能會出現在原始array的中央 , 在這個最小值兩側的數字平方後都有可能成為更大
        因此先走O(N) , 找到array的最小值 , 同時初始化兩個指標在此 
        create new array , 透過比較平方大小,將值逐一加入並移動指標
"""

""" 
    解法一. 
        採用上述的思路 , 但實現雙指標擴張跟填充的部份不是非常漂亮 , 時間和空間都蠻差的讓我有點意外,
        時間上可能是我用了太多次的while , 空間的話看起來這題的最佳解應該不能額外create array
"""
from typing import List 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # 尋找最小值
        min_index = 0
        for i in range(len(nums)):  
            if abs(nums[i]) < abs(nums[min_index]):  
                min_index = i 
        
        # 初始化兩個指標在min_index
        left = min_index -1 
        right = min_index + 1 
        sol = [None for i in range(len(nums))] 
        sol[0] = pow(nums[min_index], 2)
        
        # 逐一比較兩個指標指向的平方值 , 並將值加入sol 
        probe = 1
        while left >= 0 and right < len(nums) : 
            
            if pow(nums[left],2) < pow(nums[right],2) :  
                sol[probe] = pow(nums[left],2)
                left -= 1 
            else : 
                sol[probe] = pow(nums[right],2) 
                right += 1 
            
            probe += 1         
        
        while left >= 0  :
            sol[probe] = pow(nums[left],2) 
            left -= 1 
            probe += 1 
            
        while right < len(nums) : 
            sol[probe] = pow(nums[right] , 2) 
            right += 1 
            probe += 1 
        
        
        return sol 

""" 
    解法二. 
        看了一下Solution , 雙指標作法基本上都要create new array , 但我先找最小值這件事情實際上不必 
        反而可以想成 "array的最大值會在兩端" , 我們從兩端開始填就好 
        
        計算速度上 ,有明顯提昇 , 但整體來說還是不佳 , 空間則很差
"""

from typing import List 

class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        size = len(nums) 
        sol = [None for i in range(size)] 
        
        left = 0 
        right = size -1 
        
        probe = size -1 
        
        while probe >= 0 : 
            
            if abs(nums[left]) > abs(nums[right]) :  
                sol[probe] = nums[left]**2
                left += 1 
            else : 
                sol[probe] = nums[right] ** 2 
                right -= 1 
            
            probe -= 1 
        
        return sol 

""" 
    解法三. 
        built-in function , O(nlogn) time , O(1) space (in-place) 
        結果這個解法在速度上反而快過上面O(N) , 我猜測是因為測資的範圍太小 , 只到10^4
"""
from typing import List 

class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted( [x**2 for x in nums])
        