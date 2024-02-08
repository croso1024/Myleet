""" 
    題意:
        給定一組string array , 裡面的元素代表token , 遵循reverse polish notation 
        包含了數字與四則運算符號 , 我們要根據這串notation表達式去計算出數字
        規則包含 :
        -The valid operators are '+', '-', '*', and '/'.
        -Each operand may be an integer or another expression.
        -The division between two integers always truncates toward zero.
        -There will not be any division by zero.
        -The input represents a valid arithmetic expression in a reverse polish notation.
        
        example . 
            Input: tokens = ["2","1","+","3","*"]
            Output: 9
            Explanation: ((2 + 1) * 3) = 9
    
    思路:   
        我最直觀的思路是recursion拆分 , 看起來這所謂的reverse polist notation需要我從後面開始看
        一旦看到符號 , 就將符號的前一個元素與其餘元素做該符號的運算 , 如上面的例子 , 但在題目給的第二個例子中我發現這個規則好像不是那麼明確
        可能會出現連續兩個符號的情況.
        
        利用測資去try run ,可以總結出每當看到運算符號出現 , 就是一個由小括號包起的運算式 ,看起來用遞迴是不太好寫
        
        再次觀察一下題目,又可以發現使用stack , 從tokens開頭一直push東西進去, 一旦遇到運算符號,就將stack最上方的兩個數字拿出來計算並push回去
        這個思路看起來在給定的3個example上的可以適用
        
        
        
"""
from typing import List 
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = list() 
        
        operator = {
            "+" : lambda a,b : a+b , 
            "*" : lambda a,b : a*b , 
            "/" : lambda a,b : int(a/b) ,
            "-" : lambda a,b : a-b 
        }
        
        for token in tokens : 
            
            if token in operator :   
                b = stack.pop() 
                a = stack.pop() 
                stack.append(operator[token](a,b)) 
            
            else : 
                stack.append(int(token)) 
        
        return stack[0]
                
[0,]
        