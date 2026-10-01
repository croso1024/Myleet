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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


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
