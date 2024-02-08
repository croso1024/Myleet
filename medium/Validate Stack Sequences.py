""" 
    題意:  
        給定pushed , popped 兩組array,當中所有的元素都是unique , 要求回傳一個boolean去判斷
        在給定的兩個array操作下 , stack是否可以回到原先空的狀態
    
    思路: 
        使用兩個probe去指向pushed , popped現在的進度 ,並實際maintain一個stack 
        不斷參照stack的頂端值,以及目前popped的目標 , 當有出現stack頂端等於popped目標時就進行pop
        -> 更新stack與popped指標
"""

""" 
    解法一.
        follow上述思考方向 , 使用兩個指標去儲存當前要被加入stack的值以及如果出現要被pop的值 
"""
from typing import List 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # 2 probe as indicator 
        push , pop = 0 , 0 
        
        stack = [] 
        
        while push < len(pushed) : 
            
            # 如果stack有值並且頂端就等於當下要pop的 , 就執行pop
            if stack and stack[-1] == popped[pop] : 
                stack.pop() 
                pop += 1 
            
            # 剩下只有stack是空 , 或著頂端不是可以pop的
            else : 
                stack.append(pushed[push]) 
                push += 1 
        
        # 到此push已經全部進去, 剩下pop , 要看能否全部pop完
        
        while pop < len(popped): 
            
            if stack and stack[-1] == popped[pop] : 
                stack.pop()
                pop+=1 
            
            else : 
                return False 
        
        return True 
        