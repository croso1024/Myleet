""" 
    思路 : 
        這一題改為使用兩個Queue去實現Stack  , 實際上和Stack去實做Queue就是反過來而已
        我們的實做需要support所有的stack method , push , pop , top , empty  
        並且我們只能使用標準Queue操作 , push to back , peek pop from front , size , is empty ... 
        
        就是只能從後端加值 , 前端取值  
        
        我們使用collections的deque來模仿queue , 但就是只能用上面說的 append , popleft 

        這一題思考一下就是建立兩個Queue , 為了實現FILO的機制 , 
        每次插入element , 就把現有有元素的element先暫時全部移動到另一個Queue ,新element進到第一個Queue後再移動回來 
        基本上就是push需要O(N) , 其他操作O(1) 
        
"""


""" 
    解法一. 就是雙Queue在插入時輪流搬遷 , 插入要O(N) , 其他O(1) 
        時間不佳 , 空間普通
"""
from collections import deque
class MyStack:

    def __init__(self):
        # queue1用來持久保存Stack , queue2則是暫時移動用
        self.Queue1 = deque()
        self.Queue2 = deque() 
        self.size = 0 

    def push(self, x: int) -> None:
        
        # 先把所有元素移動到queue2 , 加入新元素到queue1再移動回來 
        while self.Queue1 : self.Queue2.append( self.Queue1.popleft()  ) 
        self.Queue1.append(x) 
        while self.Queue2 : self.Queue1.append(self.Queue2.popleft())
        self.size += 1 
        

    def pop(self) -> int:
        
        if self.empty() : raise ValueError("Stack is empty")        
        self.size -= 1 
        return self.Queue1.popleft()
        

    def top(self) -> int:
        if self.empty() : raise ValueError("Stack is empty")        
        return self.Queue1[0]
        
    def empty(self) -> bool:
        return False if self.size > 0 else True 


""" 
    解法二 . 依照題目要求 , 使用單一個Queue來模擬Stack

        插入的時候需要append popleft 自己原始長度的次數
    
"""
from collections import deque
class MyStack:

    def __init__(self):
        self.Queue = deque() 
        self.size = 0 

    def push(self, x: int) -> None:
        
        self.Queue.append(x)
        for _  in range(1 , len(self.Queue)): 
            self.Queue.append(self.Queue.popleft())
        self.size += 1 

    def pop(self) -> int:
        if not self.empty() : 
            self.size -= 1 
            return self.Queue.popleft() 

    def top(self) -> int:
        if not self.empty() : 
            return self.Queue[0]

    def empty(self) -> bool:
        return False if self.size > 0 else True 