""" 
    思路 :  
        這一題也是比較少見的設計題 , 設計一個time-based的hashmap , 在存入值的時候會多保存一個time stamp 
        而在取值的時候 , 除了給定key以外也會提供timestamp , 
        如果該key在hashmap中且有著不只一個值 , 就要返回時間在給定key-time之前,並最接近該timestamp的

        note . 這一題的timestamp看起來就是給整數 , 並且在set()使用的time stamp保證是遞增

        內部用hashmap針對key做保存 , 但key保存的資料是一組組 tuple , ( timestamp , value )  
        因為set()的time stampe保證遞增 , 因此hashmap的key對應資料用list存 , 用append(添加) 確保list內的time stamp是符合排序過得

        在拿值的時候 , 要找到對應時間,或著最接近該時間的值 , 透過Binary search去做這件事
"""


class TimeMap:

    def __init__(self):
        
        self.hashmap = dict()         

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.hashmap : 
            self.hashmap[key].append(  (timestamp , value)    )
        else : 
            self.hashmap[key] = [(timestamp , value)]


    def get(self, key: str, timestamp: int) -> str:
        
        # 該key不存在
        if not key in self.hashmap : return "" 
        
        # 該key存在 , 接著針對time stamp做binary search 
        else : 
            return self.binarySearch( key , timestamp  )
    
    
    # 給定對應的key來找到要對哪個list做Binary search , 以timestamp為目標 
    # 我們要找的是 "小於等於該timestamp的最新值" , 相當於找右側邊界
    # 我們透過壓縮右側的方式來找到該邊界 
    # 最終右側邊界值會指向right 
    def binarySearch(self , key , timestamp): 
        
        array = self.hashmap[key]
        left , right = 0 , len(array)-1    

        while left <= right : 
            
            mid = (left + right) // 2

            if array[mid][0] <= timestamp : 
                left = mid + 1 
            elif array[mid][0] > timestamp : 
                right = mid - 1
        
        
        # 最後這邊要保護一下 , 我們在壓縮邊界的Binary search有可能出現直接index out of range ,
        # 在這一題中如果發生index out of range基本上就是沒有滿足題目要求的值了
        if right >= 0 : return array[right][1]
        else : return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)