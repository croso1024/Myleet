

""" 
    Implement stack , stack中的元素需要去包含在這個元素"之下"的最小值為何
    stack裡面去maintain當前的最小值(整個stack內的最小值) , 並將其與元素一同存入stack ,
"""    
class MinStack:
    def __init__(self):
        self.stack = [] 
    def push(self, val: int) -> None:
        if self.stack : 
            self.stack.append( (val ,  min(val , self.stack[-1][1]) ) )
        else :
            self.stack.append((val,val))

    def pop(self) -> None:
        
        if self.stack : 
            
            self.stack.pop() 
        
        else :
            
            raise RuntimeError("Error")

    def top(self) -> int:
        
        if self.stack : 
            
            return self.stack[-1][0]

        else :
            
            raise RuntimeError("Error")
        
    def getMin(self) -> int:
        
        if self.stack : 
            
            return self.stack[-1][1]

        else :
            
            raise RuntimeError("Error")

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()