""" 
    思路 : 
        這一題就是直接實現一個stack , 要有push/pop/top/getMin四個method
        其中getMin看題目應該就是只要返回值 , 而不需要實際將其pop出來 
        
        題目要求四個操作全都是O(1) , 我覺得直觀來看就是只要Maintain stack中的minimum就好
        問題是在於當minimum被移除後 , 要怎麼找到新的min是這題的難點
        
        思考一下我認為應該是要運用到LIFO的特性 , 去不斷keep先前的最小值 , 
        如果新加入的值刷新了最小或等於最小 , 把他存在另外一個array裡面 , 如果pop出去的值等於他才pop 
        這樣應該就可以不斷maintain最小值 (另外一個array的最後一個element)
        
        --> 因為Stack的移除一定會先移除到當下的最小值
        
        理清以上的思路其實就很直接了 , 實際的code沒難度
"""


class MinStack:

    def __init__(self):
        
        self.stack = [] 
        self.minimum = None 
        # keep track the minimum in our array
        self.minimum_array = []

    def push(self, val: int) -> None:
        
        self.stack.append(val) 
        
        if self.minimum is None : 
            self.minimum = val 
            self.minimum_array.append(val) 
        else :             
            if val == self.minimum : 
                self.minimum_array.append(val) 
            elif val < self.minimum : 
                self.minimum = val 
                self.minimum_array.append(val) 
        
    def pop(self) -> None:
    
        remove_element = self.stack.pop() 
        
        if remove_element == self.minimum : 
            self.minimum_array.pop() 
            
            if len(self.minimum_array) >= 1 : 
                self.minimum = self.minimum_array[-1]
                
            # 一開始提交的時候忽略了這個case , pop到array為空的時候要把minimum重置回None
            else : 
                self.minimum = None 
            
        
    def top(self) -> int:
        
        return self.stack[-1]
        
    def getMin(self) -> int:
        
        return self.minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()