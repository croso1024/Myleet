""" 
    思路 : 
        這一題看起來就是一般的Sort , 由小到大 , 題目要求 N log N 級別的算法 , 且不能用built-in 
        且要盡量不用到額外Space .
        
        某種程度上來說就是要自己手刻一些比較高級的sorted , 
        我這邊使用指標版 merge sort來完成.

"""



""" 
    解法一. 
        使用指標的Merge Sort , 我使用了一塊新的記憶體空間來做合併導致空間效果不太好
        速度則是表現的不錯 
        
        -> 在left-array或right-array有邊空掉後的操作 , index有出現小失誤要特別注意

"""
from typing import List 
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        # 分成拆分和合併兩個部份 , MergeSort(i,j)表示操作範圍的index兩端 [i,j] , 我是做封閉的 
        def MergeSort( left , right ): 
            
            if left > right : return None
            elif left == right : return [nums[left]] 
            
            
            mid = (left + right)//2 
            
            left_array = MergeSort(left , mid)
            right_array = MergeSort(mid+1 , right) 
            # 後半部做合併動作 
            # 使用一個新的空間
            if left_array and right_array : 
                merge_array = [None] * (len(left_array) + len(right_array))
                l , r = 0 , 0 
                
                while l < len(left_array) and r < len(right_array): 
                    
                    if left_array[l] < right_array[r] : 
                        merge_array[l+r] =  left_array[l]
                        l+= 1
                    else : 
                        merge_array[l+r] = right_array[r]
                        r += 1 
                
                # 加完後把剩下的補回去 
                if l < len(left_array) : 
                    merge_array[l+r:] = left_array[l:]
                else : 
                    merge_array[l+r:] = right_array[r:]

            else : 
                
                merge_array = left_array if left_array else right_array 
            
            return merge_array
        
        return MergeSort( 0 , len(nums)-1 )


