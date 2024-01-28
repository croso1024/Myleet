""" 
    思路:  
        設計一個停車系統 , 我們的停車場只有三種停車位 , 大中小 ,
        並且每一種的車位都只有固定數量(在初始化時給定)  .
        
        接著要implement addCar method ,使用 1,2,3分別代表: 大 中 小 
        addCar要返回一個boolean代表這台車能否停入 , 車子只能停在符合他size的停車位 
        
        
    這一題看完題目敘述實在有點2 , 沒有把車開出去這件事情也沒有說小車可以停大位這件事 
    直接在instance裡面加入剩餘位子數的紀錄即可
    
"""
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.rest = [None , big ,medium , small]
        
        
    def addCar(self, carType: int) -> bool:
        
        if self.rest[carType] > 0 : 
            self.rest[carType] -= 1 
            return True 

        else : 
            return False 
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)