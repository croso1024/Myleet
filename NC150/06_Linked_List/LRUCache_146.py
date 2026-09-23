"""
    題意 :
    設計一個符合 Least Recently Used (LRU) 淘汰策略的 cache。

    實作 LRUCache class :
      - LRUCache(capacity)   以正整數 capacity 初始化
      - get(key) -> int       key 存在則回傳對應 value,否則回傳 -1
      - put(key, value)       key 已存在則更新 value;否則插入這組 key-value。
                              若插入後 key 數量超過 capacity,淘汰最久沒被使用的 key

    get 與 put 都必須是平均 O(1) 時間複雜度。
    get 命中、以及 put 更新既有 key,都算一次「使用」,會把該 key 變成最近使用。

    LeetCode 146 · Medium
    URL : https://leetcode.com/problems/lru-cache/

    Example :
    操作   ["LRUCache","put","put","get","put","get","put","get","get","get"]
    參數   [[2],       [1,1],[2,2],[1],  [3,3],[2],  [4,4],[1],  [3],  [4]]
    輸出   [null,      null, null, 1,    null, -1,  null, -1,   3,    4]

    Constraint :
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    get 與 put 的總呼叫次數最多 2 * 10^5

    思路 :

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""


class LRUCache:

    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":

    # Design 類題目:以「操作序列」驅動,格式同 LeetCode 判題輸入
    # (操作名稱 list, 參數 list, 預期輸出 list) —— None 代表該操作無回傳值
    test_set = [
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            # 邊界:capacity = 1,新 key 立刻淘汰舊 key
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[1], [1, 1], [1], [2, 2], [1], [2]],
            [None, None, 1, None, -1, 2],
        ),
        (
            # 更新既有 key 的 value,不增加大小,且該 key 變成最近使用
            ["LRUCache", "put", "put", "put", "get", "put", "get", "get"],
            [[2], [1, 1], [2, 2], [1, 10], [1], [3, 3], [2], [1]],
            [None, None, None, None, 10, None, -1, 10],
        ),
        (
            # get 命中會刷新使用順序:get(1) 之後,下一次淘汰的是 2 而不是 1
            ["LRUCache", "put", "put", "get", "put", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [1]],
            [None, None, None, 1, None, -1, 1],
        ),
        (
            # 查詢不存在的 key,回傳 -1,且不該插入該 key
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[2], [1, 1], [2], [3, 3], [2], [1]],
            [None, None, -1, None, -1, 1],
        ),
        (
            # 同一個 key 連續 put,cache 大小維持 1
            ["LRUCache", "put", "put", "get", "put", "get", "get"],
            [[1], [1, 1], [1, 2], [1], [2, 3], [1], [2]],
            [None, None, None, 2, None, -1, 3],
        ),
    ]

    for ops, args_list, expected_list in test_set:
        obj = None
        actual_list = []
        for op, args in zip(ops, args_list):
            if op == "LRUCache":
                obj = LRUCache(*args)
                actual_list.append(None)
            else:
                actual_list.append(getattr(obj, op)(*args))

        passed = actual_list == expected_list
        status = "Pass" if passed else "Failed"
        print(f"{status} | ops={ops}")
        print(f"       expected={expected_list}")
        print(f"       got     ={actual_list}")
