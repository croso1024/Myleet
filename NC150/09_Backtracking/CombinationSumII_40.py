"""
    題意 :
    給定一個可能含重複值的整數陣列 candidates,以及一個目標 target。
    回傳所有總和剛好等於 target 的組合。

    每個數字在同一組組合裡最多只能用一次。
    解集合不能含有重複的組合。
    組合之間的順序不限,組合內部元素的順序也不限。

    LeetCode 40 · Medium
    URL : https://leetcode.com/problems/combination-sum-ii/

    Example :
    candidates = [10,1,2,7,6,1,5], target = 8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]
    candidates = [2,5,2,1,2],     target = 5 -> [[1,2,2],[5]]

    Constraint :
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

    思路 :
    走Backtracking可以解 , 這一題不能重複選擇. 因此解空間會持續限縮. 
    由於每一種數字可以有選or不選兩條路 , 可以走的空間選擇枝最多為 2^n , 

    複雜度 :
    時間複雜度 : 展開所有選擇枝 , 解空間最多 2^n 
    空間複雜度 : 而每一個解答都可能要添加到hash set , 故最大極限為 n*(2^n)
    Trade-off :

"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = [] 
        size = len(candidates) 
        sorted_candidates = sorted(candidates)

        # index : 逐步限縮的搜索空間起始位置.
        # path 走到當前位置的軌跡
        # 走到當前位置的累積值
        def _backtracking( index : int , path : List[int], accumulate : int): 

            if accumulate == target : 
                copied_path = path[:]
                results.append(copied_path)
                return 
            
            elif accumulate > target :
                return 

            # 累加值還沒超過Sum , 則此時可以再從搜索空間找數值來加
            # 若搜索空間空了也無法找
            for i in range(index , size): 

                # 若同一層內,第二次開始展開的結果與前一個值一樣,這邊就可以剪枝. 因為這個解一定包含在前一個展開後的一部分
                if i > index and sorted_candidates[i] == sorted_candidates[i-1] : 
                    continue

                add = sorted_candidates[i]
                path.append(add)
                _backtracking(i+1 , path , accumulate=accumulate+add)
                path.pop()

        _backtracking(index=0,path=[],accumulate=0)

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
        (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),  # 官方範例,兩個 1 都要用到
        (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),          # 官方範例,重複的 2 只能產出一組
        (([1], 1), [[1]]),                                 # 邊界:單一元素剛好等於 target
        (([1], 2), []),                                    # 每個數字只能用一次,不能靠重複湊出 2
        (([1, 1], 2), [[1, 1]]),                           # 兩個不同位置的 1 可以同時使用
        (([1, 1, 1, 1], 2), [[1, 1]]),                     # 多種選法,但組合只算一種
        (([2, 2, 2], 4), [[2, 2]]),                        # 全相同,長度 2 的組合只有一組
        (([2, 2, 2], 6), [[2, 2, 2]]),                     # 全部用完才湊得到
        (([5, 5, 5], 5), [[5]]),                           # 相同值只回傳一組長度 1
        (([3, 1, 3], 6), [[3, 3]]),                        # 1 用不上;兩個 3 來自不同位置
        (([8, 7, 4, 3], 11), [[3, 8], [4, 7]]),            # 互異且未排序
        (([4, 5], 3), []),                                 # 每個候選都大於 target
        (([1, 2, 3], 6), [[1, 2, 3]]),                     # 只能全部取走
    ]

    for args, expected in test_set:
        result = c.combinationSum2(*args)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
