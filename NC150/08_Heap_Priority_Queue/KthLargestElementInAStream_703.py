"""
    題意 :
    即時維護一串分數,每次有新分數進來,都要回傳目前所有分數裡的第 k 高。

    「第 k 高」是排序後的第 k 名,不是第 k 個不重複的值。
    相同的分數會各自佔一個名次。

    實作 KthLargest class :
      - KthLargest(k: int, nums: List[int])  用 k 與一開始的分數串流 nums 初始化
      - add(val: int) -> int                  把 val 加進串流,回傳目前的第 k 高

    初始的 nums 長度可以比 k 少 1。
    add 回傳時,串流裡至少已經有 k 個分數。

    LeetCode 703 · Easy
    URL : https://leetcode.com/problems/kth-largest-element-in-a-stream/

    Example :
    操作   ["KthLargest","add","add","add","add","add"]
    參數   [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
    輸出   [null,4,5,5,8,8]

    操作   ["KthLargest","add","add","add","add"]
    參數   [[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
    輸出   [null,7,7,7,8]

    Constraint :
    0 <= nums.length <= 10^4
    1 <= k <= nums.length + 1
    -10^4 <= nums[i] <= 10^4
    -10^4 <= val <= 10^4
    add 最多被呼叫 10^4 次

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


def run(ops, args):
    obj = None
    output = []
    for op, arg in zip(ops, args):
        if op == "KthLargest":
            k, nums = arg
            obj = KthLargest(k, list(nums))
            output.append(None)
        elif op == "add":
            output.append(obj.add(*arg))
    return output


if __name__ == "__main__":
    # (操作, 參數, 預期輸出, 說明)
    # 建構時會複製 nums,避免實作改到測資本身
    test_set = [
        (
            ["KthLargest", "add", "add", "add", "add", "add"],
            [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            [None, 4, 5, 5, 8, 8],
            "官方範例:第 3 高隨新分數往上移",
        ),
        (
            ["KthLargest", "add", "add", "add", "add"],
            [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]],
            [None, 7, 7, 7, 8],
            "官方範例:重複的 7 各自佔名次",
        ),
        (
            ["KthLargest", "add", "add", "add"],
            [[1, []], [5], [-1], [10]],
            [None, 5, 5, 10],
            "邊界:一開始沒有分數,k = 1",
        ),
        (
            ["KthLargest", "add", "add"],
            [[1, [3]], [1], [4]],
            [None, 3, 4],
            "k = 1,永遠回傳目前最高分",
        ),
        (
            ["KthLargest", "add", "add", "add"],
            [[2, [1, 1, 1]], [0], [2], [2]],
            [None, 1, 1, 2],
            "第 2 高被兩個相同的新分數推上去",
        ),
        (
            ["KthLargest", "add", "add"],
            [[2, [-1, -2]], [-3], [0]],
            [None, -2, -1],
            "全是負數",
        ),
        (
            ["KthLargest", "add", "add", "add"],
            [[3, [4, 5]], [6], [1], [7]],
            [None, 4, 4, 5],
            "邊界:初始長度是 k - 1,第一次 add 才湊滿 k 個",
        ),
        (
            ["KthLargest", "add", "add"],
            [[3, [1, 2, 3]], [0], [4]],
            [None, 1, 2],
            "比第 k 高還小的分數不會改結果,更大的分數會",
        ),
    ]

    for ops, args, expected, note in test_set:
        result = run(ops, args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
