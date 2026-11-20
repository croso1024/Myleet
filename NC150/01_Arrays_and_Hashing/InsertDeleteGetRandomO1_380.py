"""
    題意 :
    設計一個能插入、刪除,並且等機率取出任一元素的集合。
    insert、remove、getRandom 都必須是平均 O(1)。

    實作 RandomizedSet class :
      - RandomizedSet()           初始化
      - insert(val) -> bool       val 不在集合裡才插入。成功插入回傳 True,已存在回傳 False
      - remove(val) -> bool       val 在集合裡才刪除。成功刪除回傳 True,不存在回傳 False
      - getRandom() -> int        從目前集合等機率回傳一個元素

    getRandom 被呼叫時,集合裡至少有一個元素。

    LeetCode 380 · Medium
    URL : https://leetcode.com/problems/insert-delete-getrandom-o1/

    Example :
    操作   ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
    參數   [[],             [1],     [2],     [2],     [],         [1],     [2],     []]
    輸出   [null,           true,    false,   true,    2,          true,    false,   2]

    說明 :
    insert(1) 成功。remove(2) 時 2 不在集合裡。
    insert(2) 成功,此時集合是 {1, 2},getRandom 回傳 1 或 2 都合法,範例給的是 2。
    remove(1) 成功,再 insert(2) 因為 2 已在集合裡而失敗。
    集合只剩 2,getRandom 只能回傳 2。

    Constraint :
    -2^31 <= val <= 2^31 - 1
    insert、remove、getRandom 總呼叫次數最多 2 * 10^5
    呼叫 getRandom 時,集合裡至少有一個元素

    思路 :
    這一題第一眼比較矇的地方是看要怎樣隨機回傳, 以及如果不隨機又會怎樣!? 
    最直覺 Naive 的想法是, 存一個 Array 加上 HashSet ? => 無法處理刪除與插入 O(1) , 可以處理 getRandome

    我們需要一個資料結構,可以快速確認知道一個元素是否已經存在,以及存在在哪個位置.
    刪除時可以在 O(1) 當中清出空間. 

    直覺上好像會走到 LinkedList + HashMap , 可以快速查找元素是否存在 + 增刪. 但無法隨機讀
    ===

    這一題我回顧了過往解法,關鍵發現是處理 Array 的方式.
    我們被 Array 不好增刪這件事限制住了. 但 Array 其實仍然可以快速刪除元素. 
    => 將目標要刪除元素與Array尾巴對調 , 再走 pop => O(1) 
    用 HashMap 去維護所有元素存在 + 索引即可 , 這樣寫入與刪除都是 O(1) , 
    查詢則使用 randomint 從 Array 隨機取. 

    複雜度 :
    時間複雜度都為 O(1) , 空間為 O(N) , HashMap + Array

    Trade-off :

"""

from random import randint 


class RandomizedSet:

    def __init__(self):
        
        self.hashmap = dict() 
        self.array = [] 

    def insert(self, val: int) -> bool:

        if val in self.hashmap : return False 
        # 插入 Array , 直接 append 到尾巴即可
        self.array.append(val)
        # 每一次插入都是在尾巴,索引固定為 len(array) - 1 
        self.hashmap[val] = len(self.array) - 1 
        return True 

    def remove(self, val: int) -> bool:

        if val not in self.hashmap : return False 

        # 要移除一個元素, 先檢查目標元素所在的索引, 與最後一個元素的索引.
        # 將元素在 Array 內做對調. 並更新受到影響的 Hashmap 表. 
        # 最後用 pop 移除Array中的元素並刪除 Hashmap 對應元素

        target_index = self.hashmap[val] 
        # 如果要移除的就是尾巴了 , 就直接移除 
        if target_index == len(self.array) - 1 : 
            self.array.pop() 
            del self.hashmap[val] 
            return True 

        # 如果要移除的元素在 Array 內部,需要做 Swap 
        last_item = self.array[-1]
        self.array[target_index] , self.array[-1] = self.array[-1] , self.array[target_index]
        # 清除要被刪的元素,順便更新被對調 item 的hashmap索引
        self.array.pop() 
        del self.hashmap[val] 
        # 在此 target_index 原先必然不在Array尾巴, 所以索引是安全的
        self.hashmap[last_item]  = target_index 
        
        return True 

    def getRandom(self) -> int:
        i = randint(0 , len(self.array) - 1) 
        return self.array[i]
        

def matches(actual, expected) -> bool:
    """預期若是 set,代表 getRandom 回傳其中任一值都算對。"""
    if isinstance(expected, set):
        return actual in expected
    return actual == expected


if __name__ == "__main__":

    # Design 類題目:以「操作序列」驅動,格式同 LeetCode 判題輸入
    # (操作名稱 list, 參數 list, 預期輸出 list, 說明)
    # None 代表該操作無回傳值
    # 預期若是 set,代表當下 getRandom 只要落在這個集合裡即算通過
    test_set = [
        (
            ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
            [[], [1], [2], [2], [], [1], [2], []],
            [None, True, False, True, {1, 2}, True, False, 2],
            "官方範例:插入 1,移除不存在的 2,再插入 2;移除 1 之後只剩 2",
        ),
        (
            ["RandomizedSet", "insert", "insert", "getRandom", "insert"],
            [[], [1], [1], [], [1]],
            [None, True, False, 1, False],
            "重複插入回傳 False,集合仍只有 1",
        ),
        (
            ["RandomizedSet", "insert", "remove", "getRandom", "remove"],
            [[], [3], [4], [], [4]],
            [None, True, False, 3, False],
            "移除不存在的值回傳 False,原有的值還在",
        ),
        (
            ["RandomizedSet", "remove", "insert", "remove", "remove", "insert", "getRandom"],
            [[], [1], [1], [1], [1], [9], []],
            [None, False, True, True, False, True, 9],
            "空集合移除回傳 False;刪光後再移除仍是 False,新插入的值才能被抽到",
        ),
        (
            ["RandomizedSet", "insert", "remove", "insert", "getRandom", "insert"],
            [[], [5], [5], [5], [], [5]],
            [None, True, True, True, 5, False],
            "移除後可以重新插入同一個值;插入第二次回傳 False",
        ),
        (
            ["RandomizedSet", "insert", "insert", "remove", "getRandom"],
            [[], [1], [2], [1], []],
            [None, True, True, True, 2],
            "移除先插入的 1 之後,只剩 2",
        ),
        (
            ["RandomizedSet", "insert", "insert", "remove", "getRandom"],
            [[], [1], [2], [2], []],
            [None, True, True, True, 1],
            "移除後插入的 2 之後,只剩 1",
        ),
        (
            ["RandomizedSet", "insert", "insert", "insert", "remove", "getRandom", "remove", "getRandom"],
            [[], [1], [2], [3], [2], [], [1], []],
            [None, True, True, True, True, {1, 3}, True, 3],
            "移除 2 之後隨機只能是 1 或 3;再移除 1 就只剩 3",
        ),
        (
            ["RandomizedSet", "insert", "insert", "insert", "remove", "getRandom"],
            [[], [0], [-1], [2147483647], [0], []],
            [None, True, True, True, True, {-1, 2147483647}],
            "0、負數與上界整數都合法;移除 0 後只能抽到剩下的兩個",
        ),
        (
            ["RandomizedSet", "insert", "insert", "getRandom", "getRandom", "getRandom", "getRandom"],
            [[], [7], [8], [], [], [], []],
            [None, True, True, {7, 8}, {7, 8}, {7, 8}, {7, 8}],
            "兩個元素時,連續 getRandom 都必須落在 {7, 8}",
        ),
    ]

    for ops, args_list, expected_list, note in test_set:
        obj = None
        actual_list = []
        for op, args in zip(ops, args_list):
            if op == "RandomizedSet":
                obj = RandomizedSet()
                actual_list.append(None)
            else:
                actual_list.append(getattr(obj, op)(*args))

        passed = len(actual_list) == len(expected_list) and all(
            matches(actual, expected) for actual, expected in zip(actual_list, expected_list)
        )
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected_list}")
        print(f"       got     ={actual_list}")
