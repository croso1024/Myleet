f"""
    題意 :
    給定字串 s 與整數 k。你可以把 s 中任意字元替換成任意其他大寫英文字母,
    最多執行 k 次替換。求替換後「所有字元皆相同」的最長子字串(substring,需連續)長度。

    LeetCode 424 · Medium
    URL : https://leetcode.com/problems/longest-repeating-character-replacement/

    Example :
    s = "ABAB",    k = 2 -> 4   (兩個 'A' 換成 'B',或反之)
    s = "AABABBA", k = 1 -> 4   (中間的 'A' 換成 'B' 得 "AABBBBA",取 "BBBB")

    Constraint :
    1 <= s.length <= 10^5
    s 僅由大寫英文字母組成
    0 <= k <= s.length

    思路 :
    想法是在一個Window內,維護最高頻的字. 
    每當窗口內 "非最高頻的字" 數量大於 K 時,就必須縮小窗口.

    我打算先維護窗口內"最高頻", 然後走Sliding Window.
    核心問題發生在最高頻的字被砍時,該如何確認其是否還是最高頻,以及若不是,下一個最高頻是誰. 

    e.g   a:2 , b:1 , c:1 ,a被砍. 下個最高頻選 a/b/c !?, 或著就維持a!? 因為至少 >= 下一個最高頻.(但下一輪再砍a就有問題).

    先走一個暴力解,窗口最高頻走O(26)檢查. 
    剩餘 Sliding Window.
    這一條路可以通過網站隱藏測資. 但還有優化空間.

    和AI討論,這一題在縮小窗口時其實不必去考慮次高頻,因為一定需要破最新高頻才有機會創造更好的解.
    因此我們只需要持續維護最高頻字,並處理窗口即可

    複雜度 : Time O(?) / Space O(?)

    Trade-off :
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def highest_freq(window:dict[int,int]):
            return max(window.values())
        
        window = dict() 
        left , right = 0 , 0 
        results = float("-inf")

        while right < len(s) : 

            letter = s[right]

            if letter in window : 
                window[letter] += 1 
            else: 
                window[letter] = 1 
            
            right += 1
            
            # 此時 window size = right-left 
            # 確認此時 窗口 - 最高頻字 <= k , 否則要踢元素
            while (right-left) - highest_freq(window) > k : 
                letter = s[left] 
                window[letter] -= 1 
                left += 1
            # 確保目前窗口Size合理的情況下(窗口內最高頻字+其他 <=K , 則evaluate一次解)
            results = max(results , right-left)

        return results

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left,right = 0,0 
        highest_freq = 0 
        window = {} 
        result = float("-inf")

        while right < len(s): 

            letter = s[right] 
            if letter in window : window[letter]+=1
            else : window[letter] = 1 

            # 直接維護到目前為止看過的最高頻
            if window[letter] > highest_freq : 
                highest_freq = window[letter] 
            
            right += 1 
            # 檢查窗口大小 , 窗口減去目前看過的最高頻 ,需要 <= K 
            # 核心想法就是 , 下一次真的能刷新答案的,就是更新 high freq的時候,而既然能更新,
            # 代表當前窗口內確實就是有那麼多個該字母
            while (right-left) - highest_freq > k : 
                letter = s[left]
                window[letter] -= 1 
                left += 1 

            result = max(result , right-left) 
        
        return result


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (("ABAB", 2), 4),
        (("AABABBA", 1), 4),
        (("A", 0), 1),              # 邊界:最短輸入
        (("AAAA", 2), 4),           # 邊界:全同字元,k 用不完
        (("ABCDE", 0), 1),          # 邊界:k=0,不得替換
        (("ABBB", 2), 4),           # 替換數剛好等於 k
        (("ABCDE", 4), 5),          # k 足夠替換掉整個字串其餘部分
        (("AABBBCCC", 2), 5),       # 最佳窗口不在字串開頭
    ]

    for args, expected in test_set:
        result = c.characterReplacement(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
