""" 
    在一條數線上,我們一開始在0的位置 , 並且目標是要到達一個特定數字target 
    我們的目標是走共numMove步到達target  , 移動的規則如下 : 
    
    - 每一次移動都可以選擇要往左或往右 
    - 在第i次移動的時候 , 我們都可以在選定的方向上走i步 
    
    我們的目標是走盡可能少的次數到達target , 因此要返回mimum number到target 
"""

""" 
    思路 : 
        這一題在概念上蠻複雜的 , 第一個想法可能是BFS爆搜一波 , 但因為target可以到10^9 ,
        因此靠+1,+2... 需要10^4次以上的層 , 一定炸開 . 

        這一題的關鍵比較數學 , 假設我們一直往正向走, 
        走到大於target d步 ,
        - 當d等於偶數 , 那只需要在前面d/2步的時候改成走反的就可 , 
        - 當d等於奇數 , 我們就再走下一步 , 看一下差值d會不會是偶數 ,
            如果是即為答案 , 如果不是則需要再走一步 , 此時差值必是偶數 
            
        因此解題的關鍵在於要湊出走到超越步數為偶數
        
"""


class Solution:
    
    def reachNumber(self, target: int) -> int:
        
        # 要使用我們的解法 , 需要先確保target為正數 
        target = target if target > 0 else  -1 * target 
        
        pos = 0 
        count = 0 
        step_size = 1 
        
        # 我們的目標是要些走到,下一步就會超出target的地方 
        while pos + step_size < target : 
            pos += step_size 
            count += 1 
            step_size += 1 
        
        # 到此 , 我們的下一步就會超出target 
        
        # 如果超出的大小為偶數d , 只要翻轉前面d/2的那一步就為解 
        if ( pos+ step_size - target) % 2 == 0 : return count  +  1  

        # 接下來的情況就是超出的步數是奇數的情況 
        # 再走出一步看看是否是偶數 , 如果是的話一樣是翻轉先前其中一步就好 
        # 因為我們的步伐是奇偶相間 , 因此 假如超過距離為d為奇數 , 
        # 而下一步是偶數 , 則還會是奇數 , 但再下一步就必然是奇數了 
        else : 
            if ((pos+(2*step_size)+1) - target) % 2 == 0 : return count + 2 
            
            else: return count + 3 