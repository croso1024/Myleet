"""
    題意 :
    給定字串 s，找出其中不含重複字元的最長「子字串」（substring，需連續）的長度。

    Constraint :
    0 <= s.length <= 10^5
    s 由英文字母、數字、符號和空白組成

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


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
