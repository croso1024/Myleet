"""
    題意 :
    給定一個非負整數,以「整數陣列 digits」表示,digits[i] 是該數的第 i 位數字,
    最高位在最前面(index 0)。整數不含前導 0(除了 0 本身)。

    將這個整數加 1,回傳結果同樣以陣列表示。

    LeetCode 66 · Easy
    URL : https://leetcode.com/problems/plus-one/

    Example :
    digits = [1,2,3]   -> [1,2,4]   (123 + 1 = 124)
    digits = [4,3,2,1] -> [4,3,2,2] (4321 + 1 = 4322)
    digits = [9]       -> [1,0]     (9 + 1 = 10)

    Constraint :
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits 不含前導 0

    思路 :

    我的想法是直接控制這個傳入陣列,用 Pop 檢視陣列尾部. 
    這樣也可以控制進位數. 

    [1,2,3] , pop 後得到 3,  加 1 變為4 append 回去
    [1,2,9] , pop 後得到 9 , 遇到9就先存進位 count = 1 , 再 pop 一次遇到2 , 變為3 , 之後再把進位 count 補 0 回去
    [1,9,9] , pop 後得到 9 , 先存進位 count = 1 , 再 pop 就再存, count = 2 , 再 pop 遇到 1 , =2 之後把 count = 2 補2個0回去
    [9] , pop 後得到 9 , 先存進位 count = 1 , 此時 pop 不了就先補 1 , 再把 count = 1 補一個0 

    複雜度 :

    上述解法 , 時間複雜度等於 O(N) , 空間複雜度 O(1) 

    Trade-off :

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        count = 0 
        while len(digits) > 0 : 

            last_digit = digits.pop() 

            if last_digit == 9 : 
                count += 1 
            else : 
                digits.append(last_digit + 1)
                break 
        
        if len(digits) == 0: digits.append(1)

        while count > 0 : 
            digits.append(0)
            count -= 1 
        
        return digits


if __name__ == "__main__":
    c = Solution()

    # (digits, 預期, 說明)
    # 每次呼叫都複製 digits,實作若原地修改,不會影響到下一題
    test_set = [
        ([1, 2, 3], [1, 2, 4], "官方範例:末位直接 +1"),
        ([4, 3, 2, 1], [4, 3, 2, 2], "官方範例:末位直接 +1"),
        ([9], [1, 0], "官方範例:單一位數進位,長度 +1"),
        ([0], [1], "邊界:數字 0"),
        ([1, 0, 0], [1, 0, 1], "中間皆為 0,不需進位"),
        ([1, 2, 9], [1, 3, 0], "末位進位,影響到前一位"),
        ([1, 9, 9], [2, 0, 0], "連續進位,但最高位不是 9"),
        ([9, 8, 9], [9, 9, 0], "進位只傳到第二位"),
        ([8, 9, 9, 9], [9, 0, 0, 0], "連續進位直到最高位,但最高位不溢位"),
        ([9, 9, 9], [1, 0, 0, 0], "全部是 9,結果多一位"),
        ([9] * 100, [1] + [0] * 100, "邊界:100 位全 9"),
        ([1] + [0] * 98 + [9], [1] + [0] * 97 + [1, 0], "邊界:100 位,只有末位進位"),
    ]

    for digits, expected, note in test_set:
        result = c.plusOne(digits[:])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       digits={digits}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
