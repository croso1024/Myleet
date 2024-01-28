""" 
    思路 :  
        給定一個Array , array[i]代表這一格的水果種類 , 假設我們只有兩個籃子 , 
        也就是最多裝兩種水果,但同一種水果可以無限制的放進籃子 , 我們可以從任意點出發 , 一旦結束或著遇到籃子無法再放(第三種水果) 
        就要結束 , 試問最多可以裝多少水果

        這一題是直觀上的sliding window , 按照sliding window的思路不用特別去考慮題目說 , 一旦結束就無法再放這件事
        就從index=0開始 , 只要籃子還沒超過兩類 , 就往右 , 並更新目前的解答 , 
        
        一旦遇見了第三種 , 開始縮小左半邊

"""


""" 
    解法一. 就是標準sliding window , 這一題在maintain window上很簡單 
"""

from typing import List 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0 
        right = 0 
        size = len(fruits) 

        sol = float("-inf")
        # 實做window的資料結構 , 使用dict() 
        basket = dict() 
        # valid , 用來驗證當前籃子的水果種類
        valid = lambda : len(basket.keys()) <= 2 


        # 實做開放區間 sliding window [left , right) 
        while right < size : 
            
            next_fruit = fruits[right] 
            
            if next_fruit in basket : 
                basket[next_fruit] += 1 
            else : 
                basket[next_fruit] = 1 
                
            legal_basket = valid()
            
            # 驗證有效性 , 如果無效就要開始縮小 
            while not legal_basket and left <= right  : 
                
                remove_fruit = fruits[left] 
                # 如果籃子裡面該種水果只剩下一個 , 那就把key給砍了 
                if basket[remove_fruit] == 1 :  
                    del basket[remove_fruit] 
                # 如果該水果的數量大於1個 , 那就-=1 
                else : 
                    basket[remove_fruit] -= 1 
                    
                left += 1 
                legal_basket = valid()

            # 確認籃子內的內容是有效的 , 去更新當前最大值 
            sol = max(sol ,  sum(basket.values()) )
            right += 1 
            
        return sol 
    
    

""" 
    解法二. 略為優化 window 的有效性 , 內容計算 ,
        速度和空間都很優
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0 
        right = 0 
        size = len(fruits) 

        sol = float("-inf")
        # 實做window的資料結構 , 使用dict() 
        basket = dict() 
        type_in_basket = 0 
        basket_size = 0 

        # 實做開放區間 sliding window [left , right) 
        while right < size : 
            
            next_fruit = fruits[right] 
            
            if next_fruit in basket : 
                basket[next_fruit] += 1 
            else : 
                basket[next_fruit] = 1 
                type_in_basket += 1 

            basket_size += 1 
            
            # 驗證有效性 , 如果無效就要開始縮小 
            while not type_in_basket <= 2  and left <= right  : 
                
                remove_fruit = fruits[left] 
                # 如果籃子裡面該種水果只剩下一個 , 那就把key給砍了 
                if basket[remove_fruit] == 1 :  
                    del basket[remove_fruit] 
                    type_in_basket -= 1 
                # 如果該水果的數量大於1個 , 那就-=1 
                else : 
                    basket[remove_fruit] -= 1 
                
                basket_size -= 1
                left += 1 
                

            # 確認籃子內的內容是有效的 , 去更新當前最大值 
            sol = max(sol ,  basket_size )
            right += 1 
            
        return sol 