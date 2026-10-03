"""
    題意 :
    中位數是有序整數列表正中間的值。
    個數是奇數時,取正中間那個;個數是偶數時,取中間兩個數的平均。

    例如 [2,3,4] 的中位數是 3。
    例如 [2,3] 的中位數是 (2 + 3) / 2 = 2.5。

    實作 MedianFinder class,數字會一個一個進來 :
      - MedianFinder()           初始化
      - addNum(num: int)         把 num 加進目前的資料
      - findMedian() -> float    回傳目前所有數字的中位數

    與正確答案的誤差在 10^-5 以內即算對。
    findMedian 被呼叫時,資料裡至少已經有一個數字。

    LeetCode 295 · Hard
    URL : https://leetcode.com/problems/find-median-from-data-stream/

    Example :
    操作   ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
    參數   [[],            [1],     [2],     [],          [3],     []]
    輸出   [null,          null,    null,    1.5,         null,    2.0]

    Constraint :
    -10^5 <= num <= 10^5
    addNum / findMedian 總呼叫次數最多 5 * 10^4

    思路 :
    直覺會認為需要Maintain兩組Heap , 
    這兩組Heap就是將將數字分成兩堆, 而中位數就藏在兩堆之間. 
    我們將其分為 first_half ( max heap ) , second_half (min heap )
    在添加數字的過程當中嚴格控制這條不變式 :   abs(len(first_half) - len(second_half)) <= 1 
    1. 若 first_half = second_half + 1 , 則 first half 的 top (max) 就是中位數
    2. 若 first_half + 1 = second_half , 則 second half 的 top (min) 就是中位數
    3. 若 first_half = second_half : 則兩邊的 Top 平均值就是中位數 

    另一個要點 ,就是在加入數字時. 要依據兩堆heap頂的數值去決定要丟入哪個Heap , 每次丟完也需要做一個平衡的動作. 

    複雜度 :
    - 時間複雜度 , 假設每一個Heap大小為 N ,   每次插入 O(NlogN), 由於我們使用兩個Heap且嚴格控制不變量.
    由於有平衡動作的存在,每一次一個數值加入Heap後(一次插入) , 最多只需要一次推出+一次插入就可以再平衡
    因此時間複雜度為 O( N/2 * Log(N/2) ) , 空間複雜度為 O(N)

    Trade-off :

"""


from heapq import heappop , heappush 
class MedianFinder:
    def __init__(self):
        
        # max heap 
        self.first_half = [] 
        # min heap 
        self.second_half = [] 

    def addNum(self, num: int) -> None:
        # 關鍵是要控制兩邊Heap的大小。
        # 一個數字加入,有可能大於兩端 heap 的任意數值 ,先決定新數值要放入哪個Heap, 
        # 最後再平衡Heap的大小. 

        max_from_first_half = -1 * self.first_half[0] if self.first_half else None 
        min_from_second_half = self.second_half[0] if self.second_half else None

        if max_from_first_half is not None and min_from_second_half is not None : 

            if max_from_first_half <= num <= min_from_second_half : 
                heappush(self.first_half , -1 * num ) 
            elif num < max_from_first_half : 
                heappush(self.first_half , -1 * num ) 
            elif num > min_from_second_half : 
                heappush(self.second_half , num) 

        elif max_from_first_half is not None : 

            if num > max_from_first_half : 
                heappush(self.second_half , num) 
            else : 
                heappush(self.first_half , -1 * num ) 
        
        elif min_from_second_half is not None : 

            if num < min_from_second_half : 
                heappush(self.first_half , -1 * num ) 
            else : 
                heappush(self.second_half , num) 
        
        else : 
            heappush(self.first_half , -1 * num ) 
            

        while abs(len(self.first_half) - len(self.second_half)) > 1 : 
            if len(self.first_half) > len(self.second_half): 
                val = -1 * heappop(self.first_half)
                heappush(self.second_half , val) 
            else : 
                val = heappop(self.second_half) 
                heappush(self.first_half , -1 * val ) 
        

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half): 
            # 兩邊的Top拿出來平均
            max_from_first_half = -1 * self.first_half[0]
            min_from_second_half = self.second_half[0]

            return (max_from_first_half + min_from_second_half)/2 
        
        elif len(self.first_half) == len(self.second_half) + 1 : 
            return -1 * self.first_half[0]
        else : 
            return self.second_half[0]

def run(ops, args):
    finder = None
    output = []
    for op, arg in zip(ops, args):
        if op == "MedianFinder":
            finder = MedianFinder()
            output.append(None)
        elif op == "addNum":
            finder.addNum(*arg)
            output.append(None)
        elif op == "findMedian":
            output.append(finder.findMedian())
    return output


def same(result, expected, tol=1e-5):
    if result is None or len(result) != len(expected):
        return False
    for got, exp in zip(result, expected):
        if exp is None:
            if got is not None:
                return False
            continue
        if isinstance(got, bool) or not isinstance(got, (int, float)):
            return False
        if abs(float(got) - float(exp)) > tol:
            return False
    return True


if __name__ == "__main__":
    # (操作, 參數, 預期輸出, 說明)
    test_set = [
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [2], [], [3], []],
            [None, None, None, 1.5, None, 2.0],
            "官方範例:偶數取平均,奇數取正中間",
        ),
        (
            ["MedianFinder", "addNum", "findMedian"],
            [[], [5], []],
            [None, None, 5.0],
            "邊界:只有一個數字",
        ),
        (
            ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [], [1], [], [1], []],
            [None, None, 1.0, None, 1.0, None, 1.0],
            "全部相同,奇數與偶數都是 1",
        ),
        (
            ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [-1], [], [-2], [], [-3], []],
            [None, None, -1.0, None, -1.5, None, -2.0],
            "全負數,由大到小進來",
        ),
        (
            ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [3], [], [1], [], [2], []],
            [None, None, 3.0, None, 2.0, None, 2.0],
            "未排序進來,第三個數插在中間",
        ),
        (
            ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [1], [], [3], [], [2], [], [4], []],
            [None, None, 1.0, None, 2.0, None, 2.0, None, 2.5],
            "奇偶交替:[1] -> [1,3] -> [1,2,3] -> [1,2,3,4]",
        ),
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [-100000], [100000], [], [0], []],
            [None, None, None, 0.0, None, 0.0],
            "數值上下限,中位數落在 0",
        ),
        (
            ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
            [[], [2], [2], [], [2], [], [2], []],
            [None, None, None, 2.0, None, 2.0, None, 2.0],
            "重複值剛好壓在中位數上",
        ),
    ]

    for ops, args, expected, note in test_set:
        result = run(ops, args)
        passed = same(result, expected)
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
