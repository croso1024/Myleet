"""
    題意 :
    給定兩個字串 s1 與 s2,若 s2 包含 s1 的任一個排列(permutation)作為子字串,
    回傳 True,否則回傳 False。
    換句話說:s1 的某個排列是否為 s2 的 substring(需連續)。

    LeetCode 567 · Medium

    Example :
    s1 = "ab", s2 = "eidbaooo" -> True   (s2 含有 "ba")
    s1 = "ab", s2 = "eidboaoo" -> False

    Constraint :
    1 <= s1.length, s2.length <= 10^4
    s1 與 s2 僅由小寫英文字母組成

    思路 :

    思路是用一個 Map 儲存 s1 的字元與出現次數.
    走雙指標, 目的是要看是否有某個窗口與s1完全Match ( 出現的字母 & 次數 ) 

    我認為核心解題點是明確知道 , 要同時平移整個固定Size的Window
    同時控制Windows內的元素.
    第一次解的卡點是在 "evaluate" 的方式 , 我嘗試用一個變數Int去存 , 每次加入s1內的+1 , 離開-1 , 
    但這會使得進入/離開同時都是s1內的字的時候不好處理 , 第一版是寫一個 evaluate 函數 , 走O(26)的時間來評估一次是否為正解.
    因此第一版時間複雜度大概是 O(N) * 26 (每一步evaluate) , 空間 O(26) 

    面重新嘗試用單變數去儲存距離答案的距離 , 需要更精細的控制


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def evaluate(dict:dict):
            return all([v == 0 for v in dict.values()])
        
        s1_dict = {} 
        for char in s1 : 
            if char in s1_dict : 
                s1_dict[char] += 1 
            else :
                s1_dict[char] = 1 

        left , right = 0 , 0 
        while right < len(s2) : 

            letter = s2[right] 

            if letter in s1_dict  : 
                s1_dict[letter] -= 1 

            # 維持窗口大小 , 窗口 Size 必然不大于S1 
            while (right - left)+1 > len(s1) : 
                letter = s2[left] 
                if letter in s1_dict : 
                    s1_dict[letter] += 1 
                left += 1 
            if evaluate(s1_dict) : return True 
            right += 1 
        return False 


            
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        left , right = 0 , 0 
        s1_size = len(s1) 
        s2_size = len(s2)
        missing = s1_size
        map = dict() 
        for char in s1 : 
            if char in map : 
                map[char] += 1 
            else : 
                map[char] = 1 


        while right < s2_size : 

            letter = s2[right] 

            if letter in map : 
                # 只有在這次進來 , 是真的需要而不是多餘時才 missing - 1 
                if map[letter] > 0 : 
                    missing -= 1 
                map[letter] -= 1 
            
            if ( right - left ) + 1 > len(s1) : 

                letter = s2[left] 

                if letter in map : 
                    # 若這次離開不是多餘的離開 , 而是需要的離開才 missing + 1 
                    if map[letter] >= 0 : 
                        missing += 1 
                    map[letter] += 1 
                
                left += 1 
                
            
            if missing == 0 : return True 
            right += 1 
        
        return False 


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (("ab", "eidbaooo"), True),
        (("ab", "eidboaoo"), False),
        (("a", "a"), True),                 # 邊界:最短輸入且相等
        (("ab", "a"), False),               # 邊界:s1 比 s2 長,不可能成立
        (("adc", "dcda"), True),            # 排列出現在開頭
        (("hello", "ooolleoooleh"), False), # 字元都在但湊不出連續排列
        (("abc", "ccccbbbbaaaa"), False),   # 字元數足夠但順序無法構成窗口
        (("aab", "eidbaaoo"), True),        # 含重複字元的 s1
    ]

    for args, expected in test_set:
        result = c.checkInclusion(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
