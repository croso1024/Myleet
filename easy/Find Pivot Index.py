""" 
    思路 : 
        此題給定一個array ,  要找出一個index , 
        使得左側的值與右側的值完全相等 . 
        
        最直觀與好寫的解法是 O(N) 時間&空間 , 就是紀錄array由左至右與反過來的累積 
        但可以延伸為只存單邊 , 即少一半空間 , 或著先計算sum , 接著就可以用常數空間去做計算 
        
        這邊直接使用計算sum , 然後常數空間去操作的方法 
        
"""

from typing import List 


""" 
    解法一. 常數空間  , 走兩次O(N) , 
        --> 速度很優,空間普通 , 不過基本上這算是空間optimal的algorithms了
"""
class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        
        # 初始化index左方與右方的累積值 , 這邊take O(N)去算acc_right
        acc_left , acc_right = 0 ,sum(nums)             
        
        # 題目有給說如果有解,回傳最靠左的答案 , 否則為-1 
        # 從index = 0 開始 
        for i in range(len(nums)): 
            
            # 這邊在比較時 , 注意acc_right實際上是有算到目前的值
            if acc_left == acc_right-nums[i] : return i 
            
            # 調整acc_left與acc_right 
            acc_left += nums[i] 
            acc_right -= nums[i]
        
        return -1 