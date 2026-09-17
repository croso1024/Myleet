"""
    題意 :
    給定一個整數陣列 nums，找出所有 i != j != k 且 nums[i] + nums[j] + nums[k] == 0 的
    三元組（triplet），結果不可包含重複的三元組。
    要回傳的是數值的陣列而不是 index 陣列

    Constraint :
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5

    思路 :
    因為是要回數值且不重複,我覺得可以先 Sorted , 之後用第一指標作為Anchor, 後面雙指標一左一右去掃.
    實作細節在於如何略過重複的數值. 這一件事簡單做就是用Set , 但為了General , 這邊走 while 跳過的做法. 
   
    
    複雜度 : Time O(N^2) / Space O(N)

    我的方案走一次Sorted O(NlogN) ,
    之後外層一個指標 , 內層雙指標全掃 ~ O(N^2)
    儲存上只有存指標 O(C) , 保存答案用 O(N) 

    Trade-off :

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []

        sorted_nums = sorted(nums) 

        # for i , anchor in enumerate(sorted_nums)  :  
        i = 0 
        while i < len(sorted_nums) : 

            anchor = sorted_nums[i]
            left = i + 1 
            right = len(sorted_nums) - 1 

            while left < right :

                if anchor + sorted_nums[left] + sorted_nums[right] == 0 : 

                    results.append([anchor , sorted_nums[left] , sorted_nums[right]]) 
                    # 完成添加後 , left , right 各自移動,跳過相同值來避免重複答案,只動一邊不可能是下一組解
                    cur_left = sorted_nums[left] 
                    cur_right = sorted_nums[right]

                    while left < right and sorted_nums[left] == cur_left : 
                        left += 1 
                    while left < right and sorted_nums[right] == cur_right : 
                        right -= 1 

                # 若數值太大 => 要減小
                elif anchor + sorted_nums[left] + sorted_nums[right] > 0 : 
                    right -= 1 
                # 數值太小 => 要增大 
                elif anchor + sorted_nums[left] + sorted_nums[right] < 0 : 
                    left += 1 
            
            i += 1
            # 跳過同一組 anchor : 
            while i < len(sorted_nums) and sorted_nums[i] == anchor : 
                i += 1 

        return results 
        


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例
    test_set = [
        (([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
        (([0, 1, 1],), []),
        (([0, 0, 0],), [[0, 0, 0]]),
        (([-1, 1, 0],), [[-1,0,1]]),
        (([-3, 1, 2],), [[-3,1,2]]),
    ]

    def normalize(triplets):
        # 三元組之間的順序、三元組內部的順序都不重要,排序後再比較
        return sorted(tuple(sorted(t)) for t in triplets)

    for args, expected in test_set:
        result = c.threeSum(*args)
        passed = result is not None and normalize(result) == normalize(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
