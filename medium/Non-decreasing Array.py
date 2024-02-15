""" 
    題意:
        給定一個包含整數的array , 要求檢查是否可以修改一個整數使其變為 non-decreasing
        
    思路:
        題目的意思我認為可以當成 , 有一次出現decreasing的機會可以跳過 , 其他時候就都要保持non-decreasing
        
        我的解法是Linear traverse,  並且遇到 num[k-1] <= nums[k]  , nums[k] > nums[k+1] 的情況時
        就要額外檢查 nums[k-1] <= nums[k+1] , 若成立, 則用掉免死金牌 ,否則直接False  
        
        -- 我沒考慮到的狀況是 , 有些情況可能是要讓一個數字變小 , 但有些情況可能是要讓一個數字變大
        而應對方法就是 , 檢查 k+1與k-1的相對大小關係 , 以下假設在中間index觸發違規的情況 
        已知 nums[k] > nums[k+1] :
        Case.1  nums[k-1] <= nums[k+1]  小 大 中 , -> 把nums[k] 改成 nums[k-1]或nums[k+1]都可 
        Case.2  nums[k-1] > nums[k+1]   中 大 小 , -> 必須把nums[k+1]改成nums[k] 
        
"""

""" 
    解法一 . Follow上述思路 
"""
from typing import List 

class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        if len(nums) == 1 : return True 
        
        # 檢查第一個元素是不是就用掉免死金牌        
        if nums[0] <= nums[1] : 
            chance = True 
        else :
            nums[0] = nums[1]
            chance = False 
        
        
        
        for i in range(1,len(nums) - 1 ):  
            
            if nums[i] <= nums[i+1] : 
                pass 
            
            else : 
                # 關鍵在於怎麼決定把 nums[i+1]變成nums[i] , 或是反過來
                if chance :
                    
                    if nums[i+1] >= nums[i-1] : 
                        nums[i] = nums[i+1] 
                    
                    else : 
                        nums[i+1] = nums[i] 
                        
                    chance = False 
                
                else : 
                    return False 
            
        return True 
        