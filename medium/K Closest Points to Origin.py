from typing import List 
""" 
    題意: 
        題目給了一個 points array代表在二維平面的上一群點 , 以及一個常數 k ,
        返回距離原點前k個近的節點list 

    思路 : 
        這一題實在是真的超標準heap , 以距離作為priority ,去main tain一個大小為k個heap 

"""

""" 
    解法一. 基本上就是標準的heap解 , 自己建立了一個class代表節點 ,用來讓heapq運作
        空間上表現很好 , 但時間有點差 , 我猜是因為後面還額外走一個O(N)的map function
"""
class P : 
    
    def __init__(self,coor ,distance): 
        self.distance = distance 
        self.coor = coor 
        
    def __gt__(self,other): 
        return self.distance > other.distance 
    def __eq__(self,other):
        return self.distance == other.distance 
    def __lt__(self,other):
        return self.distance < other.distance

    
from heapq import heappush , heappop    ,heappushpop

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [] 
        
        for (x,y) in points :  
            
            if len(heap) < k :  
                heappush(
                    heap ,  P(coor = [x,y] ,distance = -(pow(x,2) + pow(y,2)))
                ) 
            else : 
                # heappop(heap)
                heappushpop(
                    heap , P(coor = [x,y] ,distance = -(pow(x,2)  + pow(y,2)))
                )
        
        # 取得前k接近原點的座標 , 放進解中
        
        return [item.coor for item in heap]
    

""" 
    解法二. 嘗試去加快解法一
"""
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [] 
        for (x,y) in points[:k] : 
            heappush( heap , P(coor=(x,y) , distance = -1*(x*x + y*y)))
        
        print(len(heap)) 
        
        for (x,y) in points[k:] :  
            
            # heappop(heap)
            heappushpop(
                heap , P(coor = (x,y) ,distance = -1*(x*x + y*y))
                )
        
        # 取得前k接近原點的座標 , 放進解中
        return [item.coor for item in heap ]