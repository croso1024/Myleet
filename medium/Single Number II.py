""" 
    思路 : 
        給定一個Array , 在array中只有一個元素總共出現一次 , 其餘都是出現三次 , 
        題目希望我們使用O(N)時間 + O(1) 空間去找到是哪個元素出現一次而已

    這個題目讓我想到另外一種其餘元素都出現過2次的 , 可能可以用set , 遇到時將該元素加入 , 再次遇到剔除 , 最終跑完剩下的元素就是答案
    不過這樣要O(N)空間與時間 , 實際上這個思路用到這一題的三次也能有類似作法 ,
    在要求空間最佳的情況下 , 也可以考慮使用sort再線性搜索 , 但需要O(NlogN)的時間 
    
    因此這一題的難點在於要我們只用O(N)時間和O(1)空間 . 
    實際看了解答 , 這一題要達成上述條件必須使用bit operation , 有些複雜
    

"""


""" 
    解法一. 先無視空間拘束 , implement一個O(N)空間的查表解法
    
    遇到元素後 : 
        1. 若在table中 , 檢查計數器是否為2  ,是就砍掉 , 否則+1 
        2. 不在table中 , 放進table , 計數器為1 
    
    最後在table內的元素就是答案

    這個解在速度上很優 , 但空間上很差
    
"""
from typing import List 

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        
        table = dict() 
        
        for item in nums: 
            
            if item in table : 
                
                if table[item] == 2 : 
                    del table[item] 
                else : 
                    table[item] += 1 
            
            else : 
                table[item] = 1 
        
        return list(table.keys())[0] 
    
""" 
    解法二. 參考討論區別人寫的數學解 , 蠻有趣的 , space 要O(N/3)
"""

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        
        hashset = set() 
        sum = 0 
        uni_sum = 0 
        
        for item in nums: 
            
            if not item in hashset: 
                uni_sum += item 
                hashset.add(item) 
            sum += item 
    
        # sum代表整個array的總和  [a,a,a,b]
        # unisum代表array所有出現過的值的總和 [a,b]    
        
        # 將unisum 乘3倍 減去sum再除以2即為答案 
        
        return (uni_sum*3 - sum)  //2