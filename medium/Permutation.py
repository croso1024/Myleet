""" 
    思路 :
        此題為書本上回溯算法的框架示範 , 給定一組不包含重複元素的整數list , 列出有的排列組合 
        
"""
from typing import List 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==1 : return [[ nums[0] ]]
        # 用來保存backtrack算法的結果 
        result = list() 
        
        
        # 一個回溯算法的框架 , 在於在每一個遞迴的節點上都擁有目前可以做的動作以及已經選擇的動作
        def backtrack( actions , track ):
            # 這邊用到外部變數來比較 , 因為我們沒有要動action list內的元素(這樣比較麻煩)
            # 因此轉而以目前的軌跡是否已經和原始要排列的list一樣
            if len(track) == len(nums): 
                # print(track)
                result.append(list(track))
                return 

            # 從所有選擇中逐一選出可用動作 
            for number in actions :  
                
                # 如果該動作已經在軌跡中就跳過
                if number in track : continue

                # 在前序位置"做選擇" , 把動作加入track 
                track.append(number) 
                
                backtrack(actions , track)
                
                # 在後序位置要"撤銷選擇" ,移除最後一個element
                track.pop() 
            

        backtrack(nums , [])
        print(result)
        return result 
