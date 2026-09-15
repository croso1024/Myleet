"""
    題意 :
    給定一個字串陣列 strs，請將所有互為變位詞（anagram，字母組成相同、順序不同）的字串
    分到同一組，回傳所有分組。分組之間的順序、以及同一組內字串的順序都不限定。

    Constraint :
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] 僅由小寫英文字母組成

    思路 :
    這題有難度，直覺思路沒有特別馬上浮出來的想法.
    Naive Solution , 一個 Map 存分組, 分組Key使用 sorted 字串. , 存同組結果.
    因此解法是每一個 strs[i] 都做一次 Sort O(SlogS) , 然後 Hash Map 比對O(1).
    總時間是 O( N x SlogS ) , 空間應該是存Map的部分 ~ O(NS)



    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""
from pstats import SortKey
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_by_sorted_string = dict() 

        for element in strs : 
            sorted_string = "".join(sorted(element))
            if sorted_string in group_by_sorted_string : 
                group_by_sorted_string[sorted_string].append(element) 
            else : 
                group_by_sorted_string[sorted_string] = [ element ] 
        
        return list(group_by_sorted_string.values())


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例
    test_set = [
        ((["eat", "tea", "tan", "ate", "nat", "bat"],), [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        (([""],), [[""]]),
        ((["a"],), [["a"]]),
    ]

    def normalize(groups):
        # 分組順序、組內字串順序都不重要,排序後再比較
        return sorted(tuple(sorted(g)) for g in groups)

    for args, expected in test_set:
        result = c.groupAnagrams(*args)
        passed = result is not None and normalize(result) == normalize(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
