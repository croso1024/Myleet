""" 
    此題為書本中介紹二分搜索的第一題 , 同時查找也是我們使用binary search最常見的場景
    
    在還沒閱讀書本內容之前我先手寫一版 , 實際上光while迴圈的中止條件就可以想得到有
    
    - 檢查sub-list是否還有元素  ( 用sub list表示剩餘搜索空間 )

        我自己感覺是使用sub-list比較簡單 , 對於python可以比較輕易的操作 nums[:mid] , nums[mid+1:] 
        如此不用過多考慮左右指標除了碰頭或是互相反超 , 但問題變成 " 不容易返回目標的index , 只能說確實存在該目標 "
        可能用在如merge sort這樣的場景比較容易
    
    - 檢查左右指標是否交會  ( 單純用left , right指標規範出搜索空間 ) 

        這個方法的困難我認為可能是當我們的mid沒有找到target , 要進一步限縮搜索空間的時候 ,
        到底mid+1 , mid-1對於邊界的操作容易混亂 , 另外就是中止條件究竟是 left==right 還是 left >= right等等 ,
        但換句話說也是只要釐清這兩個問題 , 指標流可能更加易用 , 並且要返回index也更容易
    
"""

""" 
    解法一. 
        嘗試手刻的版本 , 注意的細節包含 while迴圈的中止條件 , 必須要left 超過 right ,
        並且我們透過在限縮空間時對mid的操作 , 使得不會產生無窮迴圈 
        例如nums=[0,1],target=1 , 我們會在mid=0沒有找到後將搜索空間限縮 , 如果left=mid就陷入無限迴圈
        
        總而言之 --> " 新的搜索空間中不包含我們這一輪嘗試但沒找到target的mid "
        

"""

from typing import List  

class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 : return 0 if nums[0] == target else -1 
        
        left , right = 0 , len(nums)-1
        
        while left <= right : 
            
            mid = (left+right) // 2  
            # 尋找到目標 
            if nums[mid] == target : return mid  
            
            # mid大於target , 把搜索空間縮小到左半邊
            elif nums[mid] > target : 

                right = mid -1  # 注意限縮時對mid的操作 
                
            elif nums[mid] < target : 
                
                left = mid + 1  # 注意限縮時對mid的操作 
            
        return -1 


test_case = [
    {"nums":[-1,0,3,5,9,12] , "target":9 } ,
    {"nums":[-1,0,3,5,9,12] , "target":2 },
    {"nums":[-1,0,3,5,9,12] , "target":12 },
    {"nums":[-1,0,3,5,9,12] , "target":0 },
    {"nums":[-1,0,3,5,9,12,15] , "target":9 },
    {"nums":[-1,0,3,5,9,12,15] , "target":2 },
    {"nums":[-1,0,3,5,9,12,15] , "target":12 },
    {"nums":[-1,0,3,5,9,12,15] , "target":0 },
    {"nums":[-1,0,3,5,9,12,15] , "target":15 },
]

C = Solution() 

for item in test_case : 
    print(C.search(**item) )
    
    