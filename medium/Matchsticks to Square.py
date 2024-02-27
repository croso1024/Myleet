""" 
    題意:
        給定 integer array : matchsticks , 
        題目要問我們是否可以在使用了'全部'的火柴棒的情況下去排出一個方形.
        注意我們不可以破壞火柴棒,但可以把兩隻火柴棒串連在一起加長
        
    思路:   
        因為我們必須使用到'全部'的火柴棒 , 而且這些火柴棒還不能被破壞
        如果從我們在每一個回合可以做的選擇這個角度出發. 
        我們能做的就是
        1.在現有方向擺上這一支火柴棒
        2.切換方向,把這隻火柴棒擺在轉90度的方向接在先前火柴棒的末端
        
        剩餘的就是在這個邏輯的基礎上加上一些參數來完成
        --------------------------------------------
        !!! 我寫完第一版本的解後才發現我有對題意理解有缺失 , 並沒有需要一定要按照他給的matchsticks順序來排.
        同時,如果這些火柴能夠排成一個正方型,那這個正方形的大小也會是唯一的,這一點也可以幫助我們去減枝 
        
        最終,這一題的邏輯根本就可以超級簡單的化為4個筒子,我們每一個回合就是將一個數字丟進筒子
        ,丟完後看看筒子是否都一樣大就好
        
"""
from typing import List 
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        size = len(matchsticks)
        if size < 4 : return False 
        solution = False 
        # 我們的backtrack給定的參數為 
        # 0.目前拿在手上的火柴編號
        # 1.目前的方向
        # 2.邊長設定為多少(在第一個方向完成後才會得到)
        # 3.目前正在走的邊其邊長為多少 , 加長的話就是把cur+手上的 ,轉彎就是把手上的放到轉彎後的第一個
        def backtrack(stick_id , direction , side_length , cur_length): 
            nonlocal solution 
            if solution : return 
            # 正在走第2,3,4條邊 
            if side_length : 
                
                # 最後一條邊了
                if direction == 4 : 
                    # 如果在最後一條邊用完了最後一支火柴,且長度剛好夠那就是解了
                    if stick_id == size :
                        if cur_length == side_length : 
                            solution = True 
                            return 
                        else : return 
                        
                    # 最後一條邊,還不是最後一支火柴 , 我們已經不能再轉彎了
                    else : 
                        if cur_length  >= side_length : return 
                        else : 
                            backtrack(stick_id+1 , direction , side_length , cur_length + matchsticks[stick_id])
                    
                # 走2,3邊
                else : 
                    # 沒有火柴了還在第二第三邊, or 如果這條邊的長度加上去會炸邊長,就鐵定不是解    
                    if stick_id == size or  cur_length  > side_length : return 
                    # 加長
                    elif cur_length  < side_length :  
                        backtrack(stick_id+1 , direction , side_length , cur_length + matchsticks[stick_id])  
                    # 這邊就一定是相等,必需要轉彎
                    else :
                        backtrack(stick_id+1 , direction+1 , side_length, cur_length = matchsticks[stick_id])

            # 目前還在走第一條邊
            else : 
                
                if stick_id == size : return 
                # 繼續加長        
                backtrack(stick_id+1 , direction , side_length , cur_length + matchsticks[stick_id])  
                # 轉彎 , 轉彎的條件是目前的cur_length > 0 , cur_length變為轉彎後的長度
                if cur_length > 0 :
                    backtrack(stick_id+1 , direction+1  , side_length=cur_length , cur_length=matchsticks[stick_id]) 
                
                
        backtrack(0 , 1 , None , 0 )
        return solution     
    
from typing import List 
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        solution = False 
        sum_length = sum(matchsticks)  
        if len(matchsticks) < 4 : return False 
        if sum_length % 4 != 0 : return False 
        side_length = sum_length // 4 
        
        step = 0 
        
        # 每一個節點都展開4個分支 , 最多就是 4^15次方個分支,但我們透過限制邊長來做剪枝
        def backtrack( i, a,b,c,d ):
            nonlocal solution,step 
            step += 1 

            if solution : 
                return 
            if i == len(matchsticks) : 
                if a==b==c==d==side_length :
                    solution = True 
                return 
            
            if a + matchsticks[i]<= side_length : backtrack(i+1 , a+matchsticks[i] , b,c,d)
            if b + matchsticks[i]<= side_length : backtrack(i+1  , a, b+matchsticks[i],c,d)
            if c + matchsticks[i]<= side_length : backtrack(i+1 , a,  b,c+matchsticks[i],d)
            if d + matchsticks[i]<= side_length : backtrack(i+1, a, b,c,d+matchsticks[i])
                    
            
        backtrack( 0,0,0,0,0)
        return solution


S = Solution() 
# print(S.makesquare([1,1,2,2,2,3,1,4,2,1,3,2,4,2,6]))
print(S.makesquare([5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]))
# [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]

            
            
        