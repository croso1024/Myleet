"""
    題意 :
    給定只含 '(' ')' '{' '}' '[' ']' 六種字元的字串 s,判斷其是否合法。
    合法的定義:
      1. 左括號必須由「相同型別」的右括號閉合
      2. 左括號必須以「正確的順序」閉合
      3. 每個右括號都要有相對應的同型左括號

    LeetCode 20 · Easy
    URL : https://leetcode.com/problems/valid-parentheses/

    Example :
    s = "()"     -> True
    s = "()[]{}" -> True
    s = "(]"     -> False
    s = "([])"   -> True
    s = "([)]"   -> False

    Constraint :
    1 <= s.length <= 10^4
    s 僅由 '()[]{}' 組成 (不會出現其他字元)

    思路 :
    這一題就是一個標準的 stack 題，在走訪的過程當中，
    持續地把左括號放進 stack，遇到右括號的時候，就從 stack 頂端開始做檢查。
    如果能夠配對成功，就可以從 stack 當中 pop 出去；如果配對失敗，就可以直接回 false。


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 
        ref = {")":"(" , "]":"[" , "}":"{"}

        for bracket in s : 

            if bracket in ["(" , "[" , "{"] : 
                stack.append(bracket) 
            # Stack 還在,遇到右括號才能比, 只有右括號能跟自己的那組配對時才可以過
            elif stack  and ref[bracket] == stack[-1]:
                stack.pop() 
            else : 
                return False 
        
        return False if stack else True 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (("()",), True),
        (("()[]{}",), True),
        (("(]",), False),
        (("([])",), True),
        (("([)]",), False),          # 型別交錯,順序錯誤
        (("(",), False),             # 邊界:只有左括號,結束時堆疊未清空
        ((")",), False),             # 邊界:只有右括號,堆疊為空時就要 pop
        (("]",), False),
        (("((((",), False),
        (("{[()]}",), True),         # 三層巢狀
    ]

    for args, expected in test_set:
        result = c.isValid(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
