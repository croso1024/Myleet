""" 
    思路 : 
        這一題說明我們拿著array中最大的兩個數字進行碰撞 , 如果兩個數字相同,那兩顆數字都會消失
        否則會剩下一個數字 , 值為相減的結果 
        求給定array經過這個規則結束後最終剩下的那個數字的值 , 如果沒有剩下石頭就是0
        
        這題的思路 , 如果採用暴力解的話 , 我們再每一輪的比較中至少可以減少stones.length的1個元素 , 題目給定stones.length <= 30 
        這樣的話暴力解可能是一個結果 , 速度上
        先做排序 -> O(NlogN) , 挑出後兩個來碰撞 , 得到新的值直接用O(N)做insert (已經排序過) 這樣子run到結束就好
        total time complexity應該算O(N^2)
"""


""" 
    解法一. 先進行排序 , 後續插入使用線性插入
        接著每一Round就是取兩個最大的值出來做碰撞 , 碰撞的結果再插入回去 , 
        往復直到stones.length == 0 or 1 結束
        速度很慢 , 但空間有很大優勢 ,
"""


from typing import List 
class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        stones.sort() 
        
        
        while len(stones) > 1 : 
            
            bigger = stones.pop() 
            smaller = stones.pop() 
            
            # bigger一定大於等於smaller
            if bigger == smaller : pass 

            # 如果相撞後還有剩下的值 , 我們要做插入的動作 ( O(N) )
            # 插入後原先的排序性質仍然存在
            else : 

                new_stone = bigger - smaller

                index = 0 
                while index < len(stones) : 
                    if stones[index] >= new_stone : 
                        stones.insert(index, new_stone)
                        break 
                    else : 
                        index += 1 
                
                # 如果前面都沒插入到
                if index == len(stones) : stones.append(new_stone)
            
        # 最後 stones 一定是空了或剩下一個
        
        return stones[0] if len(stones) == 1 else 0
                
                



""" 
    解法二. 先進行排序 , 後續插入改用Binary Search來加速
    空間一樣優 , 時間有進步到還不錯
"""

class Solution:
    
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        stones.sort() 
        
        
        while len(stones) > 1 : 
            
            bigger = stones.pop() 
            smaller = stones.pop() 
            
            # bigger一定大於等於smaller
            if bigger == smaller : pass 

            # 如果相撞後還有剩下的值 , 我們要做插入的動作 ( O(N) )
            # 插入後原先的排序性質仍然存在
            else : 
                new_stone = bigger - smaller
                # 做Binary search來插入 , 我們要找的是new stone的插入位置
                left , right = 0 , len(stones) - 1 
                
                while left <= right : 
                    
                    mid = (left+right)//2
                    
                    # 如果等於 , 那其實就直接插入在這就好
                    if stones[mid] == new_stone :
                        stones.insert(mid , new_stone) 
                        break 
                    elif stones[mid] > new_stone : 
                        right = mid - 1 
                    else : 
                        left = mid + 1 
                
                # 如果走完while , 還沒有找到插入位置 , 此時left就是要插入的位置 
                if left > right : stones.insert(left , new_stone)
                
                                
                
        # 最後 stones 一定是空了或剩下一個
        
        return stones[0] if len(stones) == 1 else 0
                