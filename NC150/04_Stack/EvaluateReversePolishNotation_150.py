"""
    題意 :
    給定字串陣列 tokens,代表一則以「逆波蘭表示法 (Reverse Polish Notation, 後綴表示法)」
    寫成的算式。求值並回傳結果整數。

    規則 :
      - 合法運算子為 '+' '-' '*' '/'
      - 每個運算元可以是整數,也可以是另一個(已求值的)子算式
      - 兩整數相除一律「向零截斷 (truncate toward zero)」
      - 保證不會出現除以零
      - 保證輸入是合法的 RPN 算式
      - 答案與所有中間計算結果都能以 32-bit integer 表示

    LeetCode 150 · Medium
    URL : https://leetcode.com/problems/evaluate-reverse-polish-notation/

    Example :
    tokens = ["2","1","+","3","*"] -> 9    ((2 + 1) * 3)
    tokens = ["4","13","5","/","+"] -> 6   (4 + (13 / 5))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22

    Constraint :
    1 <= tokens.length <= 10^4
    tokens[i] 是運算子 "+" "-" "*" "/",或是範圍在 [-200, 200] 的整數

    思路 :
    從題目觀察，看起來每一次遇到運算符的時候，就是從 stack 當中取出最頂的兩個已經算出來的數字，並根據運算子做計算，再放回 stack 當中繼續走。
    總共的操作次數會等同於整個給定輸入的 tokens 的長度 O(n)，而空間複雜度也 worst case 下也就等於 O(n)。

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] 
        operators = {
            "+" : lambda a , b : a+b ,
            "-" : lambda a , b : a-b ,
            "*" : lambda a , b : a*b , 
            "/" : lambda a , b : trunc(a/b)
        }

        # 題目確保 RPN 格式正確
        for t in tokens: 

            if t in operators: 

                # operand1  operator operand2
                operand_2 = stack.pop() 
                operand_1 = stack.pop()
                value = operators[t](operand_1 , operand_2)
                stack.append(value)
            else : 
                stack.append(int(t))

        return stack[-1]

if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((["2", "1", "+", "3", "*"],), 9),
        ((["4", "13", "5", "/", "+"],), 6),
        ((["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],), 22),
        ((["3"],), 3),                      # 邊界:只有一個運算元,沒有運算子
        ((["-2", "3", "*"],), -6),          # 負數運算元('-2' 不是運算子,別誤判)
        ((["7", "-3", "/"],), -2),          # ⚠️ 截斷 vs floor:7 // -3 == -3,正解 -2
        ((["-7", "3", "/"],), -2),          # ⚠️ 同上:-7 // 3 == -3,正解 -2
        ((["5", "2", "-"],), 3),            # 運算元順序:先 pop 的是右運算元
        ((["2", "5", "-"],), -3),           # 順序寫反的話這題會得 3
        ((["4", "2", "/"],), 2),
        ((["4","-2","/","2","-3","-","-"],),-7)
    ]

    for args, expected in test_set:
        result = c.evalRPN(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
