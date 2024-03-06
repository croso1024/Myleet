""" 
    題意:   
        給定兩個integer array spell , potion 分別長度為n,m . 
        spells[i] , 代表第i個spell的強度
        potions[i] , 代表第i個potion的強度 
        同時給定一個數值success value , 一個spell和一個potion的組合要被視為success需要他們強度的乘積 >= success value
        題目要返回一個長度為n的array pair , "pair[i]代表第i個spell可以和幾個potion組合達到success" 
        
    思路:
        稍微看過一下範例, 我認為可以先針對potions進行sort ,接下來最naive的作法就是
        針對第i個spell , 走O(m)去找到第幾個potion開始可以搭配成功 , 這樣overall time complexity就是O(mn)
        稍微改進一下用binary search去找第幾個potion開始可以搭配成功, 這樣overall time complexity就是 O(n log m)  ,
        最後加上一開始的sort , 整體TC : O( (n+m) log m )  
        
"""


""" 
    解法一. 跟隨我直覺的思路 , 對portion做sort後用binary search
"""
from typing import List 
class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # solution array 
        result = [] 
        # sort the potions
        potions.sort() 
        
        # perform binary search on sorted potions , return the leftmost index that satisify spell[i] * potions[index] >= success
        def binarySearch(spell): 
            
            left , right = 0 , len(potions) - 1 
            
            while left <= right : 
                
                mid = left + (right-left)//2 
                
                # compress the search interval 
                if spell * potions[mid] >= success : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
            
            return left 
        
        for i in range(len(spells)): 
            
            result.append( len(potions) -  binarySearch(spells[i]))

        return result
            