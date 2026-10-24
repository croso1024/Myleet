"""
    題意 :
    一圈房子圍成環,nums[i] 是第 i 間房子裡的金額。
    第一間與最後一間相鄰。
    不能偷相鄰的兩間,否則會觸發警報。
    回傳今晚能偷到的最高金額。

    LeetCode 213 · Medium
    URL : https://leetcode.com/problems/house-robber-ii/

    Example :
    nums = [2,3,2]   -> 3
    nums = [1,2,3,1] -> 4
    nums = [1,2,3]   -> 3

    Constraint :
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000

    思路 :
    這一題相較一版,把房子串接起來. 
    看起來可以當作版本一, 只是是求 

    max(
        houseRobberI(nums[:-1]),
        houseRobberI(nums[1:]),
    )
    但更合理的做法不應該是這樣. 要先思考 DP 狀態要記什麼.
    第一版先做 houseRobberI 的解答, 需要 O(N) 時間+ O(1)空間




    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber_1(nums:List[int]): 
            if len(nums) <= 2 : return max(nums)
            prev_1 = max(nums[0], nums[1]) 
            prev_2 = nums[0]
            maximum = max(prev_1 , prev_2)
            for i  in range(2,len(nums)) : 
                maximum = max(maximum , prev_2 + nums[i] , prev_1)
                prev_2 , prev_1 = prev_1 , maximum
            return maximum
            
        if len(nums) <= 2 : return max(nums) 
        return max(
            house_robber_1(nums[:-1]) , 
            house_robber_1(nums[1:]) , 
        )

if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([2, 3, 2], 3, "官方範例:頭尾相鄰,只能偷中間"),
        ([1, 2, 3, 1], 4, "官方範例:偷第 1 間與第 3 間"),
        ([1, 2, 3], 3, "官方範例:三間成環,偷金額最高的那間"),
        ([0], 0, "邊界:只有一間,金額是 0"),
        ([5], 5, "邊界:只有一間,沒有相鄰的房子"),
        ([1, 2], 2, "兩間相鄰,偷金額較高的那間"),
        ([2, 1], 2, "兩間相鄰,偷第一間"),
        ([0, 0, 0], 0, "每一間都是 0"),
        ([100, 1, 1, 100], 101, "頭尾兩個 100 相鄰,只能留一個"),
        ([2, 1, 1, 2], 3, "頭尾相鄰,偷第二間與第三間"),
        ([1, 3, 1, 3, 100], 103, "最後一間很大,搭配不相鄰的 3"),
        ([2, 7, 9, 3, 1], 11, "成環之後不能同時偷頭尾"),
    ]

    for nums, expected, note in test_set:
        result = c.rob(list(nums))
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
