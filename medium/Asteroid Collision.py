""" 
    題意 :
        給定一個array : asteroids,當中的每個元素都是代表著一台向右飛行的飛機的大小 ,以+- sign來表示飛行方向(+代表向右)
        而所有飛機都有著一樣的速度 , 當兩台飛機因為飛行方向相反而相撞 , 則保留比較大的那台 , 如果兩台飛機相等則都保留
        題目給定的array代表飛機的初始狀態 , 題目要求最終狀態
        
    思路 : 
        這一題因為飛機都是往右飛 , 因此我的想法是從array的尾端開始 , 利用stack去保存往相反方向(left)的飛機 
        當遇到一台飛機是往右 , 則檢查往左的飛機是否存在 , 若有則依照飛機大小進行處理  
        若一台往右的飛機都沒有往左的去阻擋了 , 那就將其加入solution array , (但這邊因為我們是reverse traverse給定array , 因此最後要再做reverse)
"""


""" 
    解法一:
        使用一個stack去存那些往左飛的飛機 , 用類似monostack的方式去和往右的飛機做碰撞並選擇保留
        其中我的操作步驟我認為有點不是最精簡 , 但比較詳細 
        
        TC:O(N) , MC:O(N)
"""
from typing import List 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # use stack to store the asteroid that flying in reverse direction 
        stack = list()    
        solution = list()
        # Reverse order traverse 
        for i in range(len(asteroids) - 1 , -1 , -1 ) : 
            
            # check the direction of asteroids 

            # Fly to right : 
            if asteroids[i] > 0 :  
                
                if not stack :

                    solution.append(asteroids[i]) 

                # if stack exist , that mean have a inverse-direction asteroids in front of this asteroids
                else : 
                    
                    solution.append(asteroids[i])
                    while stack :  
                        
                        # two asteroids have same size  , both explode , 
                        if asteroids[i] == abs(stack[-1])  : 
                            stack.pop()      
                            solution.pop() 
                            break 
                        
                        elif asteroids[i] > abs(stack[-1]) : 
                            stack.pop() 
                        
                        else :  
                            solution.pop()
                            break 
                    
            
            # Fly to left : 
            else : 
                
                stack.append(asteroids[i]) 
            
            
        if stack : 
            
            for i in stack : solution.append(i) 
            
        # return the solution list by reverse order ! 
        return [solution[i] for i in range(len(solution)-1 , -1 , -1)] 