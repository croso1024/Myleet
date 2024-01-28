""" 
    思路: 
        這一題要我們implement一個所謂的 smallest infinite set , 
        在初始化的時候這個集合包含了"所有正整數" , 
        而popSmallest會從1開始 , 因為在初始化完成後的set中最小的值是1 , 
        addBack則可以將值加入回到set ( 如果他仍在set中就沒有任何動作 )  
        
        換句話說這一題就是初始化完就是滿陣列 , 然後要實現pop最小值與加入最小值的功能. 
        我直觀想到的就是一個heap和一個counter的實現 
        
        counter要去紀錄下一次pop要丟出的值 , 而heap則是保存經過addBack回來的值 ,
        如果addBack的值 > counter , 相當於不用做事, 但若小於就將其加入heap 
        在pop時先從heap找最小值 , 也許還需要一個hashmap去查說 addBack的值是否在heap中
        
"""

""" 
    解法一. 
        基本上就是照上述的思路 , 用一個heap , counter , set來完成功能 , pop與add的操作都是O(logN) , 
        最終的答案速度不錯 , 空間也還可
"""
from heapq import heappop , heappush 
class SmallestInfiniteSet:

    def __init__(self):
        # self.counter代表下一個要丟出的內容
        self.counter = 1 
        self.heap = [] 
        self.inHeap = set() 

    def popSmallest(self) -> int:
        
        # 如果heap有值 , 那就pop出min heap的最小值
        if self.heap : 
            val = heappop(self.heap) 
            self.inHeap.remove(val)  
            return val 
            
        # heap是空的 , 代表要從infinite set去丟值了
        else : 
            val = self.counter  
            self.counter += 1 
            return val 

    def addBack(self, num: int) -> None:
        
        # 代表這個值還在infinite set內 , 可能是還沒pop出去或是在heap中
        if num >= self.counter or num in self.inHeap: 
            pass 
        # 值真的是需要被加入的 , 放進heap中,並在self.inHeap集合中紀錄
        else : 
            heappush(self.heap , num) 
            self.inHeap.add(num) 


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)