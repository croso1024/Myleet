"""
    題意 :
    判斷整數 n 是不是「快樂數 (happy number)」。

    快樂數的定義:
    - 從任一正整數開始,把它替換成「各位數字的平方和」。
    - 重複這個過程,直到數字變成 1(之後會一直停在 1),
      或是陷入一個「不包含 1」的無限循環。
    - 過程最後變成 1 的數就是快樂數。

    若 n 是快樂數回傳 True,否則回傳 False。

    LeetCode 202 · Easy
    URL : https://leetcode.com/problems/happy-number/

    Example :
    n = 19 -> True
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
    n = 2  -> False

    Constraint :
    1 <= n <= 2^31 - 1

    思路 :
    按照題目意思,如果把數字拆開後 , 各自平方加總的數值不斷經過此過程會到達一,那就是Happy Number ,
    如果不會並且陷入循環就不是. 

    直覺得做法 , 就是按照題目的流程 , 把給定的數字做拆解與平方和 , 並記錄到一個曾經算過的 table , 如果某個數字在過程中循環了,就能判斷不是 Happy Number , 
    否則就做到循環或著停在1為止

    複雜度 : 
    已知 n <= 2^31 : 那大概也只有 1024^3 * 2 最多 10 位數 , 極限在 9^2 * 10 => 下一輪就會剩下 3 位數. 
    空間複雜度就是這個呼叫鍊的長度 , 時間複雜度也等於呼叫鍊長度. 

    第一輪最多 810 , 而在 999 內的數字上限就是 3 x 9^2 = 243 
    因此,依據鴿籠原理 , 最多243步序列就要馬碰到1或重複.
    這條呼叫鍊就是有界的. 





    Trade-off :

"""


class Solution:
    def isHappy(self, n: int) -> bool:

        memo = set() 
        
        def _divied_and_square_sum( n : int ) : 
            num_string = str(n) 
            total_sum = 0 
            for i in range(len(num_string)): 
                total_sum +=  pow(int(num_string[i]),2) 
            return total_sum 
        
        while  n != 1  : 
            memo.add(n) 
            r = _divied_and_square_sum(n) 

            if r in memo : return False 
            else : memo.add(r) 
            n = r 
        return True 


# 快慢指標版本 , 主要就是省下memo的空間
class Solution:
    def isHappy(self, n: int) -> bool:

        slow = n 
        fast = n 
        
        def _divied_and_square_sum( n : int ) : 
            num_string = str(n) 
            total_sum = 0 
            for i in range(len(num_string)): 
                total_sum +=  pow(int(num_string[i]),2) 
            return total_sum 
        
        while n != 1 : 

            slow = _divied_and_square_sum(slow) 
            fast =  _divied_and_square_sum(_divied_and_square_sum(
                fast
            ))
            # if slow == fast : 有迴圈,無解 : 
            if fast == 1 : return True 
            if slow == fast : return False  

        return True         


if __name__ == "__main__":
    c = Solution()

    # (n, 預期, 說明)
    test_set = [
        (19, True, "官方範例:經過 82 -> 68 -> 100 -> 1"),
        (2, False, "官方範例:非快樂數"),
        (1, True, "邊界:n 本身就是 1"),
        (7, True, "個位數的快樂數"),
        (4, False, "個位數的非快樂數"),
        (3, False, "個位數的非快樂數"),
        (10, True, "含有 0 的數字"),
        (100, True, "各位平方和直接是 1"),
        (82, True, "官方範例鏈上的中間值"),
        (1111111, True, "七個 1,各位平方和為 7"),
        (999999999, False, "9 位數,每位都是 9"),
        (1000000000, True, "10^9,只有一個非零位數"),
        (2147483647, False, "邊界:2^31 - 1"),
    ]

    for n, expected, note in test_set:
        result = c.isHappy(n)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       n={n}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
