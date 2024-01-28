""" 
    思路 : 
        這一題也是要實做一個界面 , 每次call ping會帶有一個參數t , 作為時間
        在ping()時 , 我們需要做兩件事 
        1. 先把該ping對應的時間加入既有的request內 ,
        2. 返回目前在request清單中 , range在 [t-3000,t] 這個範圍內的request共有幾個
        
        我的想法是在每次ping的時候maintain request這個數字 , 讓每次ping只保留t值在給定範圍內的

"""

""" 
    解法一. 
        在每次的ping function去maintain request array , 最後返回修改完的array長度
        這個解法空間蠻好的,但速度不佳
"""


class RecentCounter:

    def __init__(self):
        
        self.request = []    
        

    def ping(self, t: int) -> int:
        
        # 加入request 
        self.request.append(t)          
        # 更新request , 只保留在range [t-3000 ,t] 的數值 
        count = 0 
        
        while count < len(self.request) and self.request[count] < t-3000 : 
            count += 1 
        
        # count 停下來的元素開始 , 就是滿足題目條件的部份
        self.request = self.request[count:] 

        return len(self.request) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

""" 
    解法二. 
        雙指標maintain合乎條件的範圍 , 就不去砍掉那些已經不符合條件的request ,
        完全只做指標的操作 ,應該可以明顯加速 , 類似sliding window

        有快上不少 , 但空間不佳
"""

class RecentCounter:

    def __init__(self):
        
        self.request = []    
        self.left = 0 
        self.right = 0 

    def ping(self, t: int) -> int:
        
        # 加入request 
        self.request.append(t)        
        self.right += 1 
        
        while self.left < self.right and self.request[self.left] < t-3000  : 
            
            self.left += 1 
            
        
        return self.right - self.left 
          


          
