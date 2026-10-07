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
    看起來直接維護一個Heap就可以處理. 而且只需要回傳第K高. 不必回傳完整排序序列.
    因此 Heap 可以只設置為大小K , 保持所有插入操作的時間複雜度為 O(logK) , 空間為 O(K) 

    複雜度 :
    - 時間複雜度 O(logK) 
    - 空間複雜度 O(K)

    Trade-off :

"""

from multiprocessing import Value
from typing import List
from heapq import heappop , heappush
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [] 
        self.maximum_size = k
        self.current_size = 0   

        # pre-fill heap
        for num in nums : 
            self.add(num)
    
    def _heap_top(self) -> int :
        if self.current_size == 0 : 
            raise ValueError("Heap is empty") 
        return self.heap[0]

    def add(self, val: int) -> int:
        
        if self.current_size < self.maximum_size: 
            heappush(self.heap , val) 
            self.current_size += 1 
        
        # 當 Heap 大小滿了 , 檢查新值有沒有大於 Kth , 有的話就塞入
        elif val > self._heap_top()  :  
            heappop(self.heap) 
            heappush(self.heap,val) 
        
        # 回傳 heap 頂端 , 也就是 Kth 
        return self._heap_top()



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
