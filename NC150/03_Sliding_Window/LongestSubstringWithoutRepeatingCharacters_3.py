"""
    題意 :
    給定字串 s，找出其中不含重複字元的最長「子字串」（substring，需連續）的長度。

    Constraint :
    0 <= s.length <= 10^5
    s 由英文字母、數字、符號和空白組成

    思路 :

    這題要找長度,我預期是Sliding Windows去維護一個目前兩指標之間的窗口.
    每次移動前,確認新目標是否在窗口內,是的話就要縮小窗口. 
    確保每次動完窗口內都是不重複字元,再接 evaluate
    此解法時間複雜度O(N) , 空間O(N)



    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        right = 0 
        window = set()
        longest_substring_size = 0 

        while left < len(s) : 

            while right < len(s) and  s[right] not in window : 
                 
                window.add(s[right])
                right += 1 

            longest_substring_size = max(longest_substring_size , len(window)) 
            
            if right == len(s) : 
                break 
            
            while left < len(s)  and s[right] in window : 
                window.remove(s[left]) 
                left += 1 

        return longest_substring_size 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left , right = 0 , 0 
        window = set() 
        answer = 0 

        while right < len(s) :

            if s[right] not in window : 
                window.add(s[right]) 
                right += 1 
            else :
                while s[right] in window : 
                    window.remove(s[left]) 
                    left += 1 
            
            answer = max(answer , len(window)) 
        
        return answer




if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
        (("",), 0),  # 邊界案例:空字串, constraint 允許 s.length == 0
    ]

    for args, expected in test_set:
        result = c.lengthOfLongestSubstring(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
