""" 
    思路:   
        這一題要求我們持續追蹤一個sorted array內第k大的數值 , 
        並且透過add() , 再加入新值的時候, "返回加入了該新值到array後  , 第k大的數值"
        那沒啥好說在初始狀態sort一次原本的array , 後面插入值的時候都做Binary search insert 
        
        
        速度很慢且空間不佳 
"""


from typing import List 
class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        
        self.array = nums 
        self.k = k 
        self.array.sort() 
        

    # 先做binary search插入後返回
    def add(self, val: int) -> int:

        
        left , right = 0 , len(self.array) - 1 
        
        while left <= right : 
            
            mid = (left+right) // 2 
            
            if self.array[mid]  == val : 
                self.array.insert(mid , val) 
                break 
            elif self.array[mid] > val : 
                right = mid - 1
            else : 
                left = mid + 1 
            
        # 走完迴圈還沒有找到插入點的話 , 那代表left所指向的位置就是插入點
        if left > right  : self.array.insert(left , val) 

        
        return self.array[-self.k]
        
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)