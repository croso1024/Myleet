""" 
    思路 :  
        這一題算是經典面試題 , 可以使用的方法從暴力解到備忘錄解 , 
        以及最進階的雙指標數種。 
        
        "關鍵在於無論是哪種算法，必須先看得出來要怎麼計算每一格可以容納的水高度"

        每一格可以容納的水高度，可以從微觀的每一格來看 , 一個格子可以接的水高度等於 = min(左方最高 , 右方最高) - 自己的高度 
        如此就可以知道單一格子要怎麼計算容納水量 , 以此延伸出不同算法
        
        
"""




""" 
    解法一. 暴力解 , 雙迴圈O(N^2)時間 , O(1) 空間
"""
from typing import List 
class Solution:

    def trap(self, height: List[int]) -> int:
        
        solution = 0 
        # 實際上第一格和最後一格是不會有裝水
        for i in range(1,len(height) -1 ) : 

            # 計算水量 , 為左右兩邊最高的值的min - 自身高度 
            volume = min( max(height[:i]) , max(height[i+1:]) ) -height[i] 
            # 注意有可能自己這一格比周圍都高 
            if volume > 0 : 
                solution += volume
            
        return solution 
            

""" 
    解法二 , 
        透過備忘錄來加速 , 即先計算好在第i格左邊最高的 , i格右邊最高的 
        如此時間複雜度可以降到O(N) , 空間則是O(N) 
        
        這個解法提交出去的時間不是很好 , 但空間反而很不錯 , 時間不佳我猜是我用了太多個loop
"""
                
class Solution:

    def trap(self, height: List[int]) -> int:
        
        solution = 0 
        # 先建立在第i格時 , 左右兩邊最大的高度 
        max_height_left = [None for i in range(len(height))]
        max_height_right =  [None for i in range(len(height))]

        # 填充這個最大高度的陣列 
        temp = 0 
        for i in range(1,len(height)): 
            temp = max(temp , height[i-1])
            max_height_left[i] = temp 

        temp = 0 
        for i in range(len(height)-2 , -1 ,-1) : 
            temp = max(temp , height[i+1]) 
            max_height_right[i] = temp  
        
        # 取得這兩個array之後就可以開始計算最大容量
        
        for i in range(1 , len(height)-1): 
            
            volume = min( max_height_left[i] , max_height_right[i]) - height[i] 
            if volume > 0 : 
                solution += volume 
        
        return solution 
            
            

""" 
    微優化解法二  , 但實際上時間差不多
"""   
class Solution:

    def trap(self, height: List[int]) -> int:
        
        solution = 0 
        # 先建立在第i格時 , 左右兩邊最大的高度 
        max_height_left = [None for i in range(len(height))]
        max_height_right =  [None for i in range(len(height))]

        # 填充這個最大高度的陣列 
        temp1 , temp2 = 0 ,0
        for i in range(1,len(height)): 
            temp1 = max(temp1 , height[i-1]) 
            temp2 = max(temp2 , height[ len(height) - i ] )
            max_height_left[i] = temp1 
            max_height_right[len(height)-i-1] = temp2 

        # 取得這兩個array之後就可以開始計算最大容量
        
        for i in range(1 , len(height)-1): 
            
            solution += max( min( max_height_left[i] , max_height_right[i] ) - height[i]  , 0 )
        
        return solution 
            
            
        
""" 
    解法三. 雙指針解法
        這個解法相當tricky , 我們用左右指針向內縮的方式 , 
        指針本身maintain一路走來看到的最大值 , 
        
        而每當走到新的一步 , 我們先看 左指針目前的最大值與右指針目前的最大值"誰小" , 以小的為基準 
        在該格可以裝的水就是那個比較矮的高度-height[i] , 
        他的概念類似於 : 雖然比較高的那邊未必指向最高的值了 , 但能裝多少取決於最小值
        
        速度很優 , 空間極優
"""


class Solution:

    def trap(self, height: List[int]) -> int:
        
        left , right = 0 , len(height) - 1 
        
        left_max = height[left]
        right_max = height[right]
        
        solution = 0 

        # 先計算左右高度 , 來判斷目前要算那一格的裝水量 
        while (left < right) : 
            
            # 左邊比較低,代表這一輪以left+1 來計算裝水量 ,之後再更新left指標
            if left_max < right_max : 
                solution += max( left_max - height[left+1] , 0 )
                left_max = max(left_max , height[left+1])                
                left += 1  
            
            else : 
                solution += max(right_max - height[right-1] , 0  )
                right_max = max(right_max , height[right-1])
                right -=1 
        
        return solution 

            
            
            
            
            
            
        
        