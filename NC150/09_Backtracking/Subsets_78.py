"""
    題意 :
    給定一個由互異整數組成的陣列 nums,回傳它的所有子集(power set)。

    解集合不能含有重複的子集。子集之間的順序不限,子集內部元素的順序也不限。

    LeetCode 78 · Medium
    URL : https://leetcode.com/problems/subsets/

    Example :
    nums = [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [0]     -> [[],[0]]

    Constraint :
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    nums 中的元素互異

    思路 :
    走Backtracking , DFS展開. 
    不過這一題要的是子集,因此不用到葉節點走完選擇空間也能當答案. 
    去重部分用一個 hashset 去紀錄看過的集合是一種做法. 
    但更好的做法應該是DFS過程當中去拆選擇枝,這樣天然確保不會有重複.

    複雜度 : 
    Time ,走訪的時間複雜度應該是 O(N!) , 空間也是 O(N!)

    Trade-off :

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        results = [] 
        
        def _backtracking( choices : List[int] , path : List[int]):
            nonlocal results
            # 先把走到目前為止的Path複製紀錄到答案
            results.append(path[:]) 
            for i , choice in enumerate(choices) : 
                path.append(choice) 
                # 這一題切選擇空間 , 不是只拿掉這一Round選的,而是直接拆掉前方.
                # 因為這一題不需要重複的解.不是要找出全部排列. 
                _backtracking( choices=choices[i+1:] , path=path ) 
                path.pop() 
            return 
        _backtracking(choices=nums, path=[])
        return results


def canon(subsets: List[List[int]]):
    """子集順序、子集內元素順序都不影響對錯。"""
    if subsets is None:
        return None
    return sorted(tuple(sorted(group)) for group in subsets)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出) —— 比對時忽略順序
    test_set = [
        (
            [1, 2, 3],
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        ),                                                    # 官方範例,2^3 = 8
        ([0], [[], [0]]),                                     # 官方範例,單一 0
        ([-10], [[], [-10]]),                                 # 邊界:數值下限
        ([10], [[], [10]]),                                   # 邊界:數值上限
        (
            [-1, 0, 1],
            [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]],
        ),                                                    # 負數、零、正數同時出現
        (
            [1, 2, 3, 4],
            [
                [],
                [1], [2], [3], [4],
                [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4],
                [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4],
                [1, 2, 3, 4],
            ],
        ),                                                    # 2^4 = 16,空集與全集都要在
    ]

    for nums, expected in test_set:
        result = c.subsets(nums)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={nums}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
