""" 
    思路 : 
        
        題目所定義的next permutation意義上就是將可用數字進行排列組合後 , 以數值大小進行sort 
        next permutation指的就是在數值上排列大於給定arr的結果 , 如果arr已經是排序的最大值 , 則改為返回最小
        
        目前的思路要分為兩個階段求解 ,
        - 第一階段使用兩個指標從最後往前(滑動視窗) , 一旦遇到左側的值小於右側 , 就從右側開始找到一個大於左側最少的值做調換 ,
        - 調換完後 , 從調換處開始做對右方所有元素做sort 即為結果 
        - 如果整條序列左側的值一直都大於右側 , 返回這條序列的反轉 
    
        這個解法在計算速度上就蠻優的了,儘管我使用一個O(N^2)的排序算法 , 空間部份則較差
    
"""

from typing import List 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1 : return nums 
        
        left,right  =  len(nums) - 2 , len(nums) - 1
        
        # 雙指標的前進速度一樣 , 因此確保左指標不要超出邊界就好 
        while left >= 0 :
            
            # 遇到left 小於 right 就準備做調換 ,調換的對象是right開始大於left最少的元素 
            # 調換後, 接著對從right到最後的元素做排序
            if nums[left] < nums[right] :  
                # 尋找大於left最少的元素 : 
                diff = nums[right] - nums[left] 
                target = temp = right 
                while  temp < len(nums) : 
                    if  nums[temp] > nums[left]  and nums[temp] - nums[left] < diff :
                        diff = nums[temp] - nums[left]
                        target = temp 
                    temp += 1 
                # 將left與target進行對調 , 接著sorted 右半邊
                nums[left] , nums[target] = nums[target] , nums[left]
                # 題目看起來嚴格要求 in-place操作  , 因為時間已經很晚了 , 這邊簡單實現in-place select sort 
                # nums = nums[:right] + sorted(nums[right:])
                
                # 針對right開始的右半做原地排序 
                for i in range( right , len(nums) ) : 
                    
                    min_index = i
                    
                    for j in range(i+1 , len(nums)) :                     
                    
                        if nums[j] < nums[min_index] : 
                            min_index = j 
                    
                    nums[i] , nums[min_index] = nums[min_index] , nums[i] 
                return 
                
            else :  
                left -= 1 
                right -= 1 
        
        nums.reverse()
        
        
C = Solution()
print(C.nextPermutation(nums=[3,2,1]))