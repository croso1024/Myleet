""" 
    思路 :  
        這一題要我們使用兩個stack來模擬Queue , 並且我們只能做stack的基本操作 , pop / push / peek , size is empty
        stack的部份就直接用python list來當就可以 ,
        要實現FIFO , 直觀上最naive的方式 , 就是兩個stack , 在push時往空的stack去放
        然後把另一堆有東西的stack全部pop過去 , 其他的peek , pop操作則正常
        
        這樣來說 ,push要O(N) , pop / peek則是O(1)
"""


""" 
    解法一. 
        這個解法 , push的時間複雜度是O(N) , pop , peek O(1) 
"""
class MyQueue:

    def __init__(self):
        
        # stack1用來暫時接 , stack2則是實際用來存資料
        self.stack1 = [] 
        self.stack2 = [] 
        self.size = 0 


    # 在push的時候 , 先把所有stack2的元素append到stack1 , 再加上新元素 , 最後pop回stack2 
    def push(self, x: int) -> None:
        
        while self.stack2 : self.stack1.append(self.stack2.pop()) 
        self.stack1.append(x) 
        while self.stack1 : self.stack2.append(self.stack1.pop())
        self.size += 1 
    

    def pop(self) -> int:
        
        if self.size > 0 : 
            self.size -= 1 
            return self.stack2.pop()
        else : 
            raise ValueError("Queue is empty")
        
      
    def peek(self) -> int:
        if self.size > 0 : 
            return self.stack2[self.size-1]
        else : 
            raise ValueError("Queue is empty")

    def empty(self) -> bool:
        return False if self.size > 0 else True 
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


""" 
    解法二. 
        我們就是keep兩個stack , 在push的時候一直往其中一個append , 真的要pop或peek時 
        就把第一個stack的東西全部移動到stack2 , 此時stack2由上到下就是FIFO , 可以使用多次pop/peek 
        此時如果有新的元素push , 就還是加入到stack1 
"""


class MyQueue:

    def __init__(self):
        # stack1就是正常的接新值 , 像是一般的stack
        self.stack1 = [] 
        # stack2則是上到下保持最早進入到最晚進入 , 提供pop , peek使用
        self.stack2 = [] 
        self.size = 0 

    def push(self, x: int) -> None:

        self.stack1.append(x)
        self.size += 1 

    def pop(self) -> int:
        
        if not self.size > 0 : raise ValueError("Queue is empty")
        
        # 如果stack2是有東西 , 則stack2最上面就是最早進入的
        if self.stack2 : 
            self.size -=1 
            return self.stack2.pop()

        # 如果stack2空了 , 把目前為止累積在stack1的都丟過去
        else : 
            while self.stack1 : self.stack2.append(self.stack1.pop())
            self.size -=1 
            return self.stack2.pop()                
        
    
    def peek(self) -> int:
        # peek的操作基本上就和pop一樣 , 只是沒有真的砍值
        if not self.size > 0 : raise ValueError("Queue is empty")
        
        # 如果stack2是有東西 , 則stack2最上面就是最早進入的
        if self.stack2 : 
            return self.stack2[len(self.stack2)-1]

        # 如果stack2空了 , 把目前為止累積在stack1的都丟過去
        else : 
            while self.stack1 : self.stack2.append(self.stack1.pop())
            return self.stack2[len(self.stack2)-1]        
        
    def empty(self) -> bool:
        return False if self.size > 0 else True 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()