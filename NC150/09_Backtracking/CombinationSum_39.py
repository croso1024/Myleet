"""
    題意 :
    給定一個由互異正整數組成的陣列 candidates,以及一個目標 target。
    回傳所有總和剛好等於 target 的組合。

    同一個數字可以重複選取,次數不限。
    兩組組合只要任一數字的出現次數不同,就算不同組合。
    組合之間的順序不限,組合內部元素的順序也不限。

    LeetCode 39 · Medium
    URL : https://leetcode.com/problems/combination-sum/

    Example :
    candidates = [2,3,6,7], target = 7 -> [[2,2,3],[7]]
    candidates = [2,3,5],   target = 8 -> [[2,2,2,2],[2,3,3],[3,5]]
    candidates = [2],       target = 1 -> []

    Constraint :
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    candidates 中的元素互異
    1 <= target <= 40

    思路 :
    給定的數值是互異的 , 而且可以重複選取. 但要列出的是 unique combination , 
    直覺上會覺得先做一次 Sort , 再走 Backtracking 疊加比較直覺. 可以提早排除一些不可能的選擇枝.
    但實際上也不需要. 就直接展開.

    時間複雜度上,由於這一輪是可以重複選擇. 而 target 最大為40 , candidate 最小2
    因此深度上最多重複挖20層. 每個元素最多出現20次這樣估. Candidate有30種

    而空間複雜度上,除了results之外我們就只存一個Path ,Path大小如上估計為20 
    

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = [] 
        size = len(candidates)

        # index 紀錄目前使用到 candidates 的哪個位置. 
        # accumulate : 展開到此當前的累積值. 
        # path : 展開到此的路徑 , 要作為解的一部分
        def _backtracking( index : int , accumulate : int , path : List[int]  ) : 
            for i in range(index , size) : 
                add = candidates[i]
                path.append(add)

                if accumulate + add == target : 
                    results.append(path[:]) 
                elif accumulate + add > target : 
                    pass 
                # 還可以繼續搜索,就往下展開
                else : 
                    _backtracking( i ,  accumulate=accumulate+add , path=path)
                path.pop() 
        
        _backtracking(0 , 0 , []) 
        return results

            


def canon(combos: List[List[int]]):
    """組合順序、組合內元素順序都不影響對錯。"""
    if combos is None:
        return None
    return sorted(tuple(sorted(group)) for group in combos)


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— 比對時忽略順序
    test_set = [
        (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),          # 官方範例,同一數字可重複
        (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),  # 官方範例
        (([2], 1), []),                                 # 官方範例,湊不出來
        (([2], 2), [[2]]),                              # 邊界:剛好一個數字等於 target
        (([3], 9), [[3, 3, 3]]),                        # 邊界:只能靠同一個數字重複
        (([4, 5], 3), []),                              # 每個候選都大於 target
        (([8, 2, 3], 6), [[2, 2, 2], [3, 3]]),          # 大於 target 的候選必須被跳過
        (([7, 3, 2], 7), [[7], [2, 2, 3]]),             # 輸入未排序,答案應與排序後相同
        (([2, 3, 5], 3), [[3]]),                        # 只有一組,而且不是重複取 2
        (([2, 4], 6), [[2, 2, 2], [2, 4]]),             # 兩種湊法,一種全重複、一種混用
    ]

    for args, expected in test_set:
        result = c.combinationSum(*args)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
