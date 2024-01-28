""" 
    題意: 
        這一題的現實意義我沒有說很get的到 , 但就是會依序得到當天的stock price ,
        並且得到該日 stock price後我們需要返回目前的 stock price已經連續漲價或持平第幾天 (即使跌了 , 答案至少也是1天) 
        ex. [7,2,1,2] 接下來得到 price = 2 , 那我們要返回4 
        
    思路:
        這一題在分類上就已經知道是個monostack , 但題目意思蠻明顯就是"前一個大於自己"的值 , 因此也可以想得到monostack
        而且還是順向的做

        stack裡面保存(price ,days) , 當有一個新的價格進來 , 就從stack pop掉所有低於該價格的
        如果pop完 , stack還有值 , 則span等於 當天日期- stack頂端的日期 ,
        如果stack空了 , 則span-day等於當天日期 ,
        最後還是要把這一組值放進stack
        

"""

""" 
    解法一. 我們給 stack放入一個預設值 , 這樣可以簡化一些額外處理

        基本上維護一個stack需要的空間為O(N) , 而時間也是O(N) 
        具體的性能表現來說 , 時間略差 , 空間不錯
"""

class StockSpanner:

    def __init__(self):

        self.stack = [(0,0)] 
        self.currend_day = 0 
        
    def next(self, price: int) -> int:
        
        self.currend_day += 1 
        
        # 如果新進入的price大於等於當前stack的頂端 , 那後面的價格要馬被他擋住 , 或著只能再次超越
        while self.stack and self.stack[-1][0] <= price : 
            self.stack.pop() 
            
        # 如果stack還有值
        if self.stack : 
            span_day = self.currend_day -  self.stack[-1][1] 
        else : 
            span_day = self.currend_day 
        
        self.stack.append( (price , self.currend_day)   )

        return span_day
        
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)