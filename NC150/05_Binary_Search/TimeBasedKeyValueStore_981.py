"""
    題意 :
    設計一個「帶時間戳記」的 key-value store,同一個 key 可以在不同的 timestamp 存入不同的 value,
    並且能查詢某個 key 在「某個 timestamp 之前(含)」最新的 value。

    實作 TimeMap class :
      - TimeMap()
            初始化物件。
      - set(key: str, value: str, timestamp: int) -> None
            將 (key, value) 存入,並標記為在 timestamp 存入。
      - get(key: str, timestamp: int) -> str
            回傳先前呼叫 set(key, value, timestamp_prev) 中,
            滿足 timestamp_prev <= timestamp 的所有紀錄裡,timestamp_prev 最大的那個 value。
            若有多筆同樣 timestamp_prev,取最後一次呼叫的 value。
            若不存在這樣的紀錄,回傳空字串 "" 。

    LeetCode 981 · Medium
    URL : https://leetcode.com/problems/time-based-key-value-store/

    Example :
    操作   ["TimeMap","set",              "get",       "get",       "set",               "get",       "get"]
    參數   [[],       ["foo","bar",1],    ["foo",1],   ["foo",3],   ["foo","bar2",4],    ["foo",4],   ["foo",5]]
    輸出   [null,     null,               "bar",       "bar",       null,                "bar2",      "bar2"]

    Constraint :
    1 <= key.length, value.length <= 100
    key 與 value 只包含小寫英文字母與數字
    1 <= timestamp <= 10^7
    對同一個 key,傳入 set 的 timestamp 保證嚴格遞增
    set 與 get 呼叫總次數最多 2 * 10^5

    思路 :

    每一個 Key 要維護一段由timestamp排序的value , 
    Key查找 O(1) , 而由於給定 set 操作輸入的 timestamp 為嚴格遞增. 
    因此每個 Key 對應的 List 總是升序排列. 

    因此我們在查詢時,就走Binary Search , 採用推進到邊界的版本. 查詢仍為 O(LogN) N=該Key下 Set 的數量. 級別


    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""



from sqlite3.dbapi2 import Timestamp
from typing import List , Dict 

class Item : 
    def __init__(self,key:str , value:str,timestamp:int): 
        self.key = key 
        self.value = value 
        self.timestamp = timestamp 

class TimeMap:

    def __init__(self):

        # Dict[str,List[Item]]
        self.time_map : Dict[str,List[Item]] = {} 
    

    def set(self, key: str, value: str, timestamp: int) -> None:

        item = Item(key,value,timestamp)
        
        if key in self.time_map : 
            self.time_map[key].append(item)
        else :
            self.time_map[key] = [item]
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.time_map : return "" 

        # Perform binary search on key list 
        map_series = self.time_map[key] 
        left , right = 0 , len(map_series) - 1 

        # 已知 set 的順序會使得 timestamp 為非遞減序列. 
        # 因此整個 List 由小到大

        while right >= left : 

            mid = (right+left)//2 
            mid_item : Item = map_series[mid] 

            # mid_item >/< 的分支 , 就去刪減搜索空間
            if  mid_item.timestamp > timestamp : 
                right = mid - 1 

            elif mid_item.timestamp < timestamp : 
                left = mid + 1 
            # 若是相等,則要往右逼近最大
            else : 
                left = mid + 1 
        
        # 離開迴圈時的條件是 left = right + 1 , 
        if right >= len(map_series) or map_series[right].timestamp > timestamp : 
            return ""
        
        else : 
            return map_series[right].value

        

        

if __name__ == "__main__":

    # Design 類題目:以「操作序列」驅動,格式同 LeetCode 判題輸入
    # (操作名稱 list, 參數 list, 預期輸出 list) —— None 代表該操作無回傳值
    test_set = [
        (
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
            [None, None, "bar", "bar", None, "bar2", "bar2"],
        ),
        (
            # 邊界:查詢的 timestamp 早於任何一次 set
            ["TimeMap", "set", "get"],
            [[], ["a", "1", 5], ["a", 1]],
            [None, None, ""],
        ),
        (
            # 邊界:查詢的 timestamp 恰好等於某次 set 的 timestamp
            ["TimeMap", "set", "set", "get", "get"],
            [[], ["a", "1", 1], ["a", "2", 3], ["a", 3], ["a", 2]],
            [None, None, None, "2", "1"],
        ),
        (
            # 多個不同 key 互不干擾
            ["TimeMap", "set", "set", "get", "get"],
            [[], ["a", "va", 1], ["b", "vb", 1], ["a", 10], ["b", 10]],
            [None, None, None, "va", "vb"],
        ),
        (
            # 查詢從未 set 過的 key
            ["TimeMap", "set", "get"],
            [[], ["a", "1", 1], ["b", 1]],
            [None, None, ""],
        ),
        (
            # 同一個 key 多次覆寫,timestamp 嚴格遞增
            ["TimeMap", "set", "set", "set", "get", "get", "get", "get"],
            [[], ["k", "v1", 1], ["k", "v2", 2], ["k", "v3", 3], ["k", 1], ["k", 2], ["k", 3], ["k", 100]],
            [None, None, None, None, "v1", "v2", "v3", "v3"],
        ),
    ]

    for ops, args_list, expected_list in test_set:
        obj = None
        actual_list = []
        for op, args in zip(ops, args_list):
            if op == "TimeMap":
                obj = TimeMap()
                actual_list.append(None)
            else:
                actual_list.append(getattr(obj, op)(*args))

        passed = actual_list == expected_list
        status = "Pass" if passed else "Failed"
        print(f"{status} | ops={ops}")
        print(f"       expected={expected_list}")
        print(f"       got     ={actual_list}")
