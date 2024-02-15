""" 
    題意:
        設計一個用來管理作為預約的class , 我們有n個座位編號1->n 
        所有seat在初始化的時候都是available的 
        
        int reverse(): 從available的空位中選定編號最小的 , 並返回其編號同時將其設置為預約
        void unreverse(int seatNumber) : 依照給定的seatNumber取消預約 
    
    思路: 
    
        題目要的應該就是call reverse的速度 , 需要做一個資料結構提供快速找出目前編號最小的可用座位 ,
        同時unreverse()也要求我們要能夠快速的將一個作為插入回排序清單
        
        最暴力解的方式就是一個stack去儲存目前可用的座位 , 
        當reverse()的時候從stack上去返回 , 而unreverse則是走O(N)搜索將對應位子插回正確位子 
        
        另一種作法則是使用heap , 而我認為使用heap更加簡單 , 建立一個heap名為available , 將位子存入
        這樣可以確保reverse() , unreverse都只要O(logN) 
"""


""" 
    解法一. heap solution
        速度與空間都很優
"""
from heapq import heappop , heappush ,heapify
class SeatManager:

    def __init__(self, n: int):
        
        self.available_heap = [i for i in range(1,n+1)]
        heapify(self.available_heap)
    # 題目給定不會在沒有seat或著沒有任何預約的情況下call reserve/unreserve
    def reserve(self) -> int:
    
        return heappop(self.available_heap) 
            
        
    def unreserve(self, seatNumber: int) -> None:

        heappush(self.available_heap , seatNumber)         


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)