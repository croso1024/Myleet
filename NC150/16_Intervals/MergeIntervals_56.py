"""
    題意 :
    給定若干區間 intervals,其中 intervals[i] = [starti, endi]。
    把所有重疊的區間合併,回傳合併後的區間。
    合併後的區間彼此不重疊,而且要蓋住原本的每一段。

    兩段只要有交集就算重疊,端點相接也算。
    例如 [1,4] 與 [4,5] 要合成 [1,5]。
    區間之間的順序不限,區間內部維持 [start, end]。

    LeetCode 56 · Medium
    URL : https://leetcode.com/problems/merge-intervals/

    Example :
    intervals = [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]                 -> [[1,5]]

    Constraint :
    1 <= intervals.length <= 10^4
    intervals[i].length == 2
    0 <= starti <= endi <= 10^4

    思路 :

    應該必然是一個 O(N) , N 為 interval 組數的演算法.
    但因為給定的題目沒有排序這些 interval , 完全有可能需要先做 Sorting 
    如果做 Sorting 才合併. 那基本上算法時間複雜度就是 O(NlogN) , 空間複雜度則除了暫存解答的輔助空間外,
    就只需要hook掛著當前正在合併的解. 
    Sorting 解 : 
    給定兩個Interval  [a,b] , [c,d] 且  a <= c 的情況下,要重疊則 b >= c 

    另外一個想法是 , 既然 start_i / end_i 的值域只有 0 ~ 10^4 , 
    是否直接初始化一個  10^4 大小的 boolean Array , 接著 O(N) 把所有的都填入就可!? 



    複雜度 : 
    Sorting 解 : 
    時間複雜度 O(NlogN) , 空間 O(C)

    Trade-off :

"""

from typing import List

# Solution.1 先做 Sorting 的解 : 
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort() 
        sorted_intervals = intervals # Rename 
        # 開始做 Merge, 題目沒說不能改原始解,那就直接 in-place 處理,不用額外輔助空間. 

        cur_interval : List[int] = None 
        results = [] 

        for interval in sorted_intervals : 

            if cur_interval is None : 
                cur_interval = interval 
                continue 
                
            # 現在開始 , 處理合併
            # 若下一個 Interval 與當前的重疊,則更新 Current interval 的範圍 (可能變大) 
            if cur_interval[1] >= interval[0] : 
                cur_interval[1] = max(cur_interval[1] , interval[1]) 
            
            # 若不重疊,就可以把先前合併完的結果丟進去, 並移動到下一個Interval
            else : 
                results.append(cur_interval) 
                cur_interval = interval 
        
        # 若手上還有 cur_interval , 記得加入回去
        if cur_interval : 
            results.append(cur_interval) 
        
        return results 
    

# Solution.2 嘗試做 基於 Boolean Array 的解 : 
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 0 ~ 10^4
        bit_array = [False] * ( pow(10,4) + 1 ) 

        for interval in intervals : 
            from_i , to_i = interval 
            bit_array[from_i:to_i+1] = [True] * (to_i - from_i + 1)
        # 完成之後開始走.

        i = 0 
        cur_start = None 
        results = [] 

        while i < len(bit_array) : 

            if cur_start is None  and bit_array[i] :
                cur_start = i 
            
            elif cur_start is not None : 
                # 斷掉,則添加到答案集,重置cur_start
                if not bit_array[i] : 
                    results.append([cur_start ,i-1]) 
                    cur_start = None 
            
            i += 1 
        
        if cur_start is not None : 
            results.append([cur_start , pow(10,4)]) 
        
        return results 


        

def canon(intervals: List[List[int]]):
    """區間彼此的順序不影響對錯;每段內部的 [start, end] 要保留。"""
    if intervals is None:
        return None
    return sorted(tuple(pair) for pair in intervals)


if __name__ == "__main__":
    c = Solution()

    # (輸入, 預期輸出, 說明) —— 只忽略區間彼此的順序
    test_set = [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
            "官方範例:前兩段重疊,後面兩段各自獨立",
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
            "官方範例:端點相接也要合併",
        ),
        ([[5, 8]], [[5, 8]], "邊界:只有一段"),
        ([[0, 0]], [[0, 0]], "邊界:起點終點都是 0"),
        (
            [[1, 2], [4, 5]],
            [[1, 2], [4, 5]],
            "完全沒有重疊",
        ),
        (
            [[4, 7], [1, 4]],
            [[1, 7]],
            "輸入未排序,端點相接",
        ),
        (
            [[1, 10], [2, 6], [3, 4]],
            [[1, 10]],
            "後段完全被前段包住",
        ),
        (
            [[1, 2], [2, 3], [3, 4]],
            [[1, 4]],
            "多段只在端點相接,串成一段",
        ),
        ([[1, 3], [1, 3]], [[1, 3]], "完全相同的兩段"),
        (
            [[1, 4], [0, 2], [3, 5]],
            [[0, 5]],
            "三段交錯,合成一段",
        ),
        (
            [[8, 10], [1, 3], [15, 18], [2, 6]],
            [[1, 6], [8, 10], [15, 18]],
            "官方範例打亂順序",
        ),
        (
            [[1, 4], [0, 0]],
            [[0, 0], [1, 4]],
            "點區間與後面的段不相交",
        ),
        (
            [[0, 10000], [1, 2]],
            [[0, 10000]],
            "邊界:數值上下限,短段被長段包住",
        ),
    ]

    for intervals, expected, note in test_set:
        result = c.merge(intervals)
        passed = canon(result) == canon(expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
