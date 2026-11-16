"""
    題意 :
    給定一個只含正整數的陣列 nums。
    判斷能不能把它切成兩個子集,讓兩邊的元素和相等。
    每個元素只能放進其中一邊。

    LeetCode 416 · Medium
    URL : https://leetcode.com/problems/partition-equal-subset-sum/

    Example :
    nums = [1,5,11,5] -> True
    nums = [1,2,3,5]  -> False

    Constraint :
    1 <= nums.length <= 200
    1 <= nums[i] <= 100

    思路 :

    這一題是回頭看了東哥的書來複習的 , 0-1 背包問題的變種.
    問題的建模就是 , 能不能從給定陣列中取出一個子集 , 子集的大小剛好等於某個數值. 

    套回這題, 要找的是存不存在一個子集的總和等於  sum(nums) / 2 , 
    也就是,如果陣列中存在某個子集剛好等於 sum(nums) / 2 , 那其實沒被選入子集的湊起來也必然是 sum(nums) / 2 . 
    但這一題就是得想到這一點才可以. 

    接著定義 DP 的狀態和轉移. 
    這一題要看的狀態就是 , 能取多少陣列內的元素 , 以及要湊到多少.
    固應該從 2D-DP 開始 , dp[i][j] 去表示 , 採用前i個 nums ,是否能湊到 j  , 題目就是全部 nums 下能否湊出 sum(nums) / 2 

    接著看怎樣做狀態轉移!? , 在背包問題裡 ,選擇表示的是 "要不要拿進這個 num" 
    
    如果拿進 nums[i] , 則還能湊出 j 的條件就是 dp[i-1][ j - nums[i] ] , 
    如果不拿進 nums[i] , 則能湊出 j 的條件就是 dp[i-1][ j ] , 
    這兩種情況都能推算出 dp[i][j] , 也就是這兩個其中一個為 True , dp[i][j] 為 True 
    先以此版本 , 就能寫一個 2D DP 的模型 , 後面再來討論狀態壓縮. 
    
    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # Take O(N) time complexity 
        total_sum = sum(nums) 
        
        # if total_sum is odd , return False directly 
        if total_sum % 2 != 0 : return False 

        # Prepare DP Array  dp[i][j]   Solution = dp[len(nums)][ total_sum // 2 ]

        # Space Complexity =  O(N x total_sum)
        dp = [ 
            [ False for _ in range((total_sum // 2) + 1 ) ] for i in range(len(nums) + 1) 
        ]
        # Init State : 
        # if target == 0 , 則給定 nums 從 0 ~ 全部都可以湊出 0 元的子集
        # if 給定 nums 只有 0 個 , 則 j>=1 開始都湊不出 
        
        for i in range(len(nums) + 1) : dp[i][0] = True
        for j in range( (total_sum // 2 ) + 1 ) : dp[0][j] = False
        dp[0][0] = True


        # Start iterate 
        for i in range(1,len(nums)+1) : 
            for j in range( 1,(total_sum // 2 ) + 1 ) : 

                # use nums[i-1] , not nums[i] 
                if j - nums[i-1] >= 0 : 
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i - 1]] 
                else :
                    dp[i][j] = dp[i-1][j]


        return dp[len(nums)][ total_sum // 2 ] 
    

# 解法二 , 從狀態轉移看得出來 , 我們其實只要存 dp[i-1] 那一列 , 不需要從頭到尾每個子陣列的答案,這樣可以進一步優化空間
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums) 
        if total_sum % 2 != 0 : return False 

        # 將 "使用到前一個子陣列元素時是否能湊出錢的陣列存著" 
        # prev[i] 在目前所遍歷的第 k 個元素 , 能不能湊到 i 元
        prev = [ False for i in range( (total_sum // 2 ) + 1 )]  

        prev[0] = True 

        # 在使用到第 k 個元素的情況下 , 是否湊得到 i 元
        for k in range(1, len(nums) + 1 ) :

            # 注意這裡使用反向迭代 , 因為我們都是用同一個 prev 陣列去存 , 由左到右的迭代會讓每一個 prev[i] 沒有正確參考到前一輪
            for i in range( (total_sum//2)  , 0 , -1 ) : 

                # 不用第 k 元素 (prev[i-1]) , 或著用 prev([i - nums[k-1]])
                if i - nums[k-1] >= 0: 
                    prev[i] = prev[i] or prev[i - nums[k-1]]
                else : 
                    prev[i] = prev[i]
        
        return prev[(total_sum//2)]
                

        



if __name__ == "__main__":
    c = Solution()

    # (nums, 預期, 說明)
    test_set = [
        ([1, 5, 11, 5], True, "官方範例"),
        ([1, 2, 3, 5], False, "官方範例"),
        ([1, 2, 5], False, "三個正整數"),
        ([1, 2, 3, 4], True, "四個連續正整數"),
        ([2, 2], True, "兩個相同的數"),
        ([1, 1], True, "兩個 1"),
        ([100], False, "只有一個數"),
        ([1], False, "邊界:長度 1"),
        ([1, 1, 1, 1], True, "四個 1"),
        ([3, 3, 3, 4, 5], True, "五個數"),
        ([1, 2, 3, 6], True, "四個數"),
        ([2, 2, 2], False, "三個 2"),
        ([1, 5, 5, 11], True, "四個數,含重複"),
        ([10, 10], True, "兩個 10"),
        ([1, 1, 2], True, "三個數"),
    ]

    for nums, expected, note in test_set:
        result = c.canPartition(nums)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       input={nums} | expected={expected} | got={result}")
