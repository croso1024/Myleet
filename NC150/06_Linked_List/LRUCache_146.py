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
    這一題直覺上是要維護一個長度最大為 Capacity 的 Linked List , 
    而且應該要是雙向 Linked List 來支援快速的替換節點. 

    我們使用 HashMap 去紀錄Key是否存在以及Key的值. 
    但問題在於我們要做 : 
    - 查找/更新後 , 將目標Key放到最近使用的第一個位置
    - 新增Key導致Size過大後，需要排除最舊的Key.

    因此我們需要能夠快速定位到 Linked list 當中的某個節點,還要能快速操作 Linked List 的結構. 
    這邊應該使用雙向 Linked List , 且同時紀錄頭尾兩端方便剔除/更新為最近使用. 
    
    複雜度 : 
    - 時間複雜度 :  put / get  操作為 HashMap 查表 , Linked List 更新 , 都為 O(1) 
    - 空間複雜度 :  我們需要儲存Size為 Capacity 的 Linked List / HashMap 

    Trade-off :

"""


from typing import List , Dict 

class Node: 
    def __init__(self, key : int , value : int) : 
        self.key = key 
        self.value = value 
        self.next : Node|None = None 
        self.prev : Node|None = None 

# Double-end Linked List 
class DLinkedList : 

    def __init__(self):
        
        self.dummy_head = Node(key=None,value=None)
        self.dummy_tail = Node(key=None,value=None)

        self.dummy_head.next = self.dummy_tail 
        self.dummy_tail.prev = self.dummy_head 

        self.current_capcity = 0 
    
    # 踢掉某個尾巴的節點 , 踢掉後吐出節點 , 讓外部 Hashmap 可以知道誰被踢
    def pop(self) -> Node  : 

        if self.current_capcity > 0 : 

            tail_node = self.dummy_tail.prev 
            tail_node.prev.next = self.dummy_tail 
            self.dummy_tail.prev = tail_node.prev 
            self.current_capcity -= 1 
            return tail_node
        else :
            raise ValueError("Invalid Operation")
    
    # 把某個節點更新到頭
    def update(self,node : Node) : 

        # 先取出節點. 
        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node 
        next_node.prev = prev_node 

        # 把節點塞到頭 , 將原先的頭 prev 指向新節點
        origin_head = self.dummy_head.next 
        self.dummy_head.next = node 
        node.prev = self.dummy_head 

        node.next = origin_head
        origin_head.prev = node 

    # 把某個節點塞入頭
    def add_to_head(self,node:Node)  : 
        
        origin_head = self.dummy_head.next 
        self.dummy_head.next = node 
        node.prev = self.dummy_head 

        node.next = origin_head 
        origin_head.prev = node 
        self.current_capcity += 1 

    def get_current_capacity(self) -> int : 
        return self.current_capcity 

class LRUCache:

    def __init__(self, capacity: int):
        
        # {Key : Node}
        self.hashmap : Dict[int , Node] = {} 
        self.double_ended_linked_list = DLinkedList() 
        self.maximum_capacity = capacity 

    def get(self, key: int) -> int:
        
        if key in self.hashmap: 
            node : Node = self.hashmap[key] 
            # 更新該節點為最新 
            self.double_ended_linked_list.update(node) 
            return node.value 
        else : 
            return -1 

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap : 
            node : Node = self.hashmap[key] 
            node.value = value 
            self.double_ended_linked_list.update(node) 
            return 
        else : 

            current_capacity = self.double_ended_linked_list.get_current_capacity() 

            if current_capacity == self.maximum_capacity : 
                evicted_node = self.double_ended_linked_list.pop() 
                del self.hashmap[evicted_node.key] 
                
            added_node = Node(key=key,value=value)
            self.hashmap[key] = added_node
            self.double_ended_linked_list.add_to_head(added_node)
        


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
