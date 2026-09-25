"""
    題意 :
    給定一個整數陣列 nums,其中包含 n + 1 個整數,每個整數都落在 [1, n]。
    陣列裡只有一個數字會重複出現(至少兩次),其餘數字最多出現一次。
    回傳這個重複的數字。

    不得修改 nums,且只能使用常數額外空間。

    LeetCode 287 · Medium
    URL : https://leetcode.com/problems/find-the-duplicate-number/

    Example :
    nums = [1,3,4,2,2] -> 2
    nums = [3,1,3,4,2] -> 3
    nums = [3,3,3,3,3] -> 3

    Constraint :
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    nums 中除了恰好一個數字會出現兩次以上,其餘數字都只出現一次

    思路 :

    只能使用常數空間 , 且不能修改 nums 基本上就鎖死了 sorted 的路線. 因為不能直接改,複製出來Sort又會破壞空間複雜度限制. 
    最 Naive 的做法是雙迴圈,
    釘著一個接著掃其他的 , 才能做到 O(N^2) 時間 + O(1) 空間 ,但這是不可接受的


    這一題的解法，是將 nums 當作 Linkedlist 建模,
    由於 nums 長度為 N + 1 , 值域為 [1,N] , 因此所有值都不會 out of index , 
    由於一定有個值出現超過一次 , 因此, 將 nums[i] 作為節點 next 指向的位置時 , 一定有某個節點有超過一條的進入點
    ( 一定有某個 nums[i] 出現超過一次  ) , 而這個有多個入口的點,就是環的起始點. 因此我們要找的就是環的起始點Index.
    ( 在我們的定義 , nums[i]表示下一個節點的index , 超過一個 nums[i] 指向某個節點 == 該節點為環入口 )

    複雜度 : Time O(N), 需要走最多兩輪 Linked list , / Space O(1) , 僅存指標

    Trade-off :

"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow , fast = 0 , 0 
        # 已知 nums 長度為 N + 1 , 值為 1~N 
        

        # 將 nums 內的值作為一個個節點 , 
        # 在節點 index=i , 下一個節點的索引為 nums[i] ,
        # 因為 nums  array 內一定至少有2個以上的數字有一樣的 nums[i] , 因此一定會構成環

        # 這一題的核心觀察是,找到環的起始點Index. 
        # 環的起始點 , 就表示有一條以上的路徑會指向該節點 , 那就是有兩個以上 nums[i] 所持有的數值  )

        # Step.1 使用快慢標先進入環中 
        while True :
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast : break 

        # Step.2 找相交點 , 初始化一個新指標從頭開始走 , 找到相交點的index
        probe = 0 
        while probe != slow : 

            slow = nums[slow] 
            probe = nums[probe] 

        # 回傳相交點的索引
        return probe 
        

if __name__ == "__main__":
    c = Solution()

    # (nums, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    # 另檢查呼叫後 nums 沒有被改動
    test_set = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),                         # 同一個數字重複填滿
        ([1, 1], 1),                                  # 邊界:n = 1
        ([1, 3, 4, 2, 1], 1),                         # 重複值在頭尾
        ([2, 2, 2, 2, 2], 2),
        ([1, 4, 4, 2, 3], 4),                         # 重複值在中間
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5),          # 較長,重複一次
        ([3,3,3,1,2], 3),          
        ([1,2,3,3,3], 3),          
    ]

    for nums, expected in test_set:
        given = list(nums)
        result = c.findDuplicate(given)
        unchanged = given == nums
        passed = result == expected and unchanged
        status = "Pass" if passed else "Failed"
        print(
            f"{status} | input={nums} | expected={expected} | got={result} | unchanged={unchanged}"
        )
