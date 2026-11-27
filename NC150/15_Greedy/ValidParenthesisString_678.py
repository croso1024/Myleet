"""
    題意 :
    給定一個只含 '('、')'、'*' 三種字元的字串 s,判斷它是否合法。

    合法的規則:
    - 每個 '(' 都必須有一個對應的 ')'。
    - 每個 ')' 都必須有一個對應的 '('。
    - '(' 必須出現在與它對應的 ')' 之前。
    - '*' 可以視為一個 ')'、一個 '(',或空字串 ""。

    LeetCode 678 · Medium
    URL : https://leetcode.com/problems/valid-parenthesis-string/

    Example :
    s = "()"   -> True
    s = "(*)"  -> True
    s = "(*))" -> True

    Constraint :
    1 <= s.length <= 100
    s[i] 只會是 '('、')' 或 '*'

    思路 :

    直覺上是雙指標,兩邊靠外指然後從合法集合往內縮.但這條解好像會因為 "*)*" 這樣的情況失敗. 
    所以應該採用順向走,順便用一個 stack 去疊加.(空間能不能優化後續討論) 
    如此一來時間複雜度 O(N) , 空間也最多 O(N) 

    想法上是讓 "(" , "*" 都加入 stack , 遇到 ")" 就消掉.
    額外儲存一個 counter , 如果是使用 "*" 來消除,就遞增此counter. 
    一但最後全部走完 , stack 還有剩, 則檢查剩餘的 "(" 數量是否 <= counter , 是的話代表那些counter都可以直接當成空字串.
    如果消不掉就直接炸裂. 


    想了半天這一題有一堆 Edge Case,先嘗試暴力解.
    還是去翻過往的解答才想出來,關鍵在走到 ")" , 優先拿最靠近的 "(" 去對消. 
    如果能全部消完, stack 只剩下 "(" , "*" , 再走一個 stack 做確認
   
    時間複雜度 , Worse Case O(N^2) , 空間複雜度 O(N)


    Trade-off :

"""



class Solution:
    def checkValidString(self, s: str) -> bool:

        lp = 0 
        stack = [] 
        for i in range(len(s)): 
            char = s[i] 
            if char == "(" : 
                lp += 1 
                stack.append(char) 
            elif char == "*" : 
                stack.append(char) 
            else : 
                if not stack : return False 
                if lp > 0 : 
                    c = 0 
                    while stack : 
                        item = stack.pop()
                        if item == "*" : c += 1 
                        else : 
                            lp -= 1 
                            break 
                    for i in range(c) : stack.append("*") 
                else : 
                    stack.pop() 
        
        # 走完之後只剩下 lp , * , 而且消除的時候優先使用 lp 去消
        wildcard = 0 
        while stack :
            char = stack.pop() 
            if char == "("  : 
                if wildcard == 0 : return False 
                else : wildcard -= 1 
            else : 
                wildcard += 1 
        
        return True
                
                
                        
                
            

            
        





if __name__ == "__main__":
    c = Solution()

    # (s, 預期, 說明)
    test_set = [
        ("()", True, "官方範例"),
        ("(*)", True, "官方範例"),
        ("(*))", True, "官方範例"),
        ("*", True, "邊界:只有一個 '*'"),
        ("(", False, "邊界:只有一個 '('"),
        (")", False, "邊界:只有一個 ')'"),
        ("((()))", True, "不含 '*' 的合法字串"),
        (")(", False, "不含 '*',數量相同但順序錯誤"),
        ("(*", True, "'*' 在 '(' 之後"),
        ("*)", True, "'*' 在 ')' 之前"),
        ("*(", False, "'*' 在 '(' 之前"),
        (")*", False, "'*' 在 ')' 之後"),
        ("((*)", True, "兩個 '(',一個 '*',一個 ')'"),
        ("(((*)", False, "三個 '(',但後面只有兩個字元"),
        ("(*()", True, "'*' 夾在兩組括號之間"),
        ("**))", True, "兩個 '*' 後接兩個 ')'"),
        ("**)))", False, "兩個 '*' 後接三個 ')'"),
        ("())(*", False, "前段就出現多餘的 ')'"),
        ("(*)(", False, "最後一個 '(' 之後沒有任何字元"),
        ("*()(*", True, "首尾都有 '*'"),
        ("(((******))", True, "大量 '*' 夾在中間"),
        ("(" * 50 + "*" * 50, True, "邊界:50 個 '(' 後接 50 個 '*'"),
        ("(" * 51 + "*" * 49, False, "邊界:51 個 '(' 後接 49 個 '*'"),
        (")" + "*" * 99, False, "邊界:開頭為 ')',後接 99 個 '*'"),
        ("*" * 100, True, "邊界:100 個 '*'"),
    ]

    for s, expected, note in test_set:
        result = c.checkValidString(s)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       s={s!r}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
