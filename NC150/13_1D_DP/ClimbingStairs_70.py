"""
    題意 :
    爬 n 階樓梯,每次可以爬 1 階或 2 階。
    回傳有多少種不同的爬法可以到達樓頂。
    順序不同就算不同的爬法。

    LeetCode 70 · Easy
    URL : https://leetcode.com/problems/climbing-stairs/

    Example :
    n = 2 -> 2
    n = 3 -> 3

    Constraint :
    1 <= n <= 45

    思路 :
    回傳可以有幾種方法爬到 N 階. 經典的DP問題. 
    已知每一次可以爬 1 or 2 階. 
    因此, 爬到第N階的方法數等同爬到第N-1階的方法 + N-2階的方法數. 

    給定 N=2 -> 2 , 代表從0階開始爬. 
    爬到 N=2 的方法數等於爬到一階的方法數1 , 加上爬到0階的方法數. 題目給定2 , 則假設爬到0階有一種方法.
    N=3 => 爬到2階的方法數2 + 爬到1階的方法數1 

    故只需要常數空間即可維護 N-1 / N-2 的方法數去推得N 
    時間複雜度則為N. 可以 DP Bottom Up , 或著遞迴Top-Down 遞迴需要吃下 Call stack 的空間,但比較漂亮


    Trade-off :

"""

# # DP Solution 
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 : return 1 
        elif n == 2 : return 2 

        # N=2
        n_prev = 2
        # N=1 
        n_prev_prev = 1 
        for _ in range(3,n+1):
            methods = n_prev + n_prev_prev 
            n_prev_prev = n_prev 
            n_prev = methods 
        return methods

# Recursive Solution 
class Solution:
    def climbStairs(self, n: int) -> int:

        ref_map = {} 

        def _recursive(n): 
            if n == 1 : return 1 
            elif n == 2 : return 2 
            elif n in ref_map : return ref_map[n]
            answer = _recursive(n-1) + _recursive(n-2) 
            ref_map[n] = answer 
            return answer 
    
        return _recursive(n)




if __name__ == "__main__":
    c = Solution()

    # (n, 預期, 說明)
    test_set = [
        (1, 1, "邊界:只有 1 階,只能爬一步"),
        (2, 2, "官方範例:1+1 或 2"),
        (3, 3, "官方範例:1+1+1、1+2、2+1"),
        (4, 5, "在 3 階的爬法後面各接一步,或在 2 階後面接兩步"),
        (5, 8, "接在前兩階的爬法數量相加"),
        (6, 13, "同上,確認遞推還在累加"),
        (45, 1836311903, "邊界:n 的上限"),
    ]

    for n, expected, note in test_set:
        result = c.climbStairs(n)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={n} | expected={expected} | got={result}")
