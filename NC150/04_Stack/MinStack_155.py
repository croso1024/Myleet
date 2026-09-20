"""
    題意 :
    設計一個 stack,支援 push / pop / top,並且能以「常數時間」取得堆疊中的最小值。

    實作 MinStack class :
      - MinStack()          初始化物件
      - push(value: int)    將 value 推入堆疊
      - pop()               移除堆疊頂端元素
      - top() -> int        取得堆疊頂端元素
      - getMin() -> int     取得堆疊中的最小值

    所有方法都必須是 O(1) 時間複雜度。

    LeetCode 155 · Medium
    URL : https://leetcode.com/problems/min-stack/

    Example :
    操作   ["MinStack","push","push","push","getMin","pop","top","getMin"]
    參數   [[],        [-2],  [0],   [-3],  [],      [],   [],   []]
    輸出   [null,      null,  null,  null,  -3,      null, 0,    -2]

    Constraint :
    -2^31 <= value <= 2^31 - 1
    pop / top / getMin 保證只會在非空堆疊上被呼叫
    push / pop / top / getMin 總呼叫次數最多 3 * 10^4

    思路 :
    想法上需要有個東西去紀錄當前還在Stack內的最小值,才能做到O(1) getMin , 
    而這樣做的問題就在於如果最小值被 pop , 該如何回答下一個最小值是誰. 

    我的想法是既然要達到O(1)速度,我們可能得有一個額外的儲存去記憶當前在Stack內的最小值.
    假設這個額外儲存叫做 minimum_stack : List[(int,int)] , 分別儲存值與出現次數. , 這個Array的尾巴就是當前最小值與出現次數
    一但新元素被放入 :
    - 新元素大於目前最小值 , 則不用更新 minimum_stack , 因為新元素直到被pop出去前,最小值必在Stack內 
    - 新元素小於目前最小值 , 新增到 minimum_stack ,計數為1
    - 新元素等於目前最小值 , minimum_stack 最小值出現次數 +1 
    一但Stack頂端被移除 : 
    - 若該值等同於minimum_stack 最小值,則次數-1 , 若減1後為0,則移出 minimum_stack 


    複雜度 : Time O(?) / Space O(?)

    時間複雜度滿足所有操作O(1),
    空間複雜度在worse case底下(全部單調遞減) , O(N) n為操作數(push)


    Trade-off :

"""


from typing import List , Tuple 

class Record:
    
    def __init__(self,value:int):
        self.value = value 
        self.count = 1 
class MinStack:

    def __init__(self):
        self.minimum_stack : List[Record] = [] 
        self.stack : List[int] = [] 

    def push(self, value: int) -> None:
        self.stack.append(value) 
        if self.minimum_stack : 
            
            if value < self.minimum_stack[-1].value : 
                self.minimum_stack.append(Record(value))
            elif value == self.minimum_stack[-1].value : 
                self.minimum_stack[-1].count += 1

        else : 
            self.minimum_stack.append( Record(value) ) 

    def pop(self) -> None:
        value = self.stack.pop() 
        if value == self.minimum_stack[-1].value : 
            if self.minimum_stack[-1].count == 1 : 
                self.minimum_stack.pop() 
            else:
                self.minimum_stack[-1].count -=1 
        
    def top(self) -> int:
        return self.stack[-1] 

    def getMin(self) -> int:
        return self.minimum_stack[-1].value


if __name__ == "__main__":

    # Design 類題目:以「操作序列」驅動,格式同 LeetCode 判題輸入
    # (操作名稱 list, 參數 list, 預期輸出 list) —— None 代表該操作無回傳值
    test_set = [
        (
            ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
            [[], [-2], [0], [-3], [], [], [], []],
            [None, None, None, None, -3, None, 0, -2],
        ),
        (
            # 邊界:單一元素,push 後立刻 getMin
            ["MinStack", "push", "getMin", "top"],
            [[], [5], [], []],
            [None, None, 5, 5],
        ),
        (
            # 重複的最小值:pop 掉一個 0 之後,最小值仍須是 0 (不可一次清光)
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [0], [1], [0], [], [], []],
            [None, None, None, None, 0, None, 0],
        ),
        (
            # 遞減 push:每次 getMin 都要換成新的最小值
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
            [[], [3], [2], [1], [], [], [], [], []],
            [None, None, None, None, 1, None, 2, None, 3],
        ),
        (
            # 遞增 push:最小值自始至終不變
            ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"],
            [[], [1], [2], [3], [], [], []],
            [None, None, None, None, 1, None, 1],
        ),
        (
            # 負數與 pop 到只剩一個元素
            ["MinStack", "push", "push", "pop", "getMin", "top"],
            [[], [-1], [-5], [], [], []],
            [None, None, None, None, -1, -1],
        ),
    ]

    for ops, args_list, expected_list in test_set:
        obj = None
        actual_list = []
        for op, args in zip(ops, args_list):
            if op == "MinStack":
                obj = MinStack()
                actual_list.append(None)
            else:
                actual_list.append(getattr(obj, op)(*args))

        passed = actual_list == expected_list
        status = "Pass" if passed else "Failed"
        print(f"{status} | ops={ops}")
        print(f"       expected={expected_list}")
        print(f"       got     ={actual_list}")
