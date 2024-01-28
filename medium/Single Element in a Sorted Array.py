from typing import List 
""" 
    題意 : 
        給定一個sorted array , 當中只有一個數值是只出現一次 , 其他都剛好出現兩次
        要找到那一個只出現一次的元素 
        題目要求使用O(logN)時間和O(1)空間
    
    思路: 
        這一題最直覺的作法可以是線性搜索去找每個元素的下一個元素是否等同自己 ,
        但這樣需要O(N)時間+O(1)空間 , 而題目說明要求logN時間就有點直接表明了需要binary search 
        
        因此我就打算用binary search , 找到目標的function其實蠻簡單的
        就是當 ( 左邊的值 = 超出邊界 or != 自己  ) and ( 右邊的值 = 超出邊界 or != 自己  )就是目標
        
        這一題的關鍵點在於要怎麼決定沒找到目標時要切分左邊或右邊 ,這個關鍵是看Solution得到的靈感
        -> 如果一個sorted array裡面的元素都是兩個 ,則所有偶數index的下一個值應該要是一樣的 
        : nums[i] == nums[i+1] if i%2 == 0 但如果某個點發生了只出現一次 , 則後面的部份就不滿足這個規則
        因此我們判斷切左右的規則就是 :
        1. 先檢查mid是否為答案 , 若否
        2. 檢查mid的index 奇數偶數 , 再決定跟前還是後比較
        3. 如果mid這邊就已經沒有上述規則 , 說明答案在前半 , 否則在後半
        

"""

""" 
    解法一. recursion的binary search , 
        一開始想不太到怎樣去判斷要往左還往右探索 , 所以這邊寫了一個都展開的方式 , 每次recursion都要O(1)時間
        我自己算大概是 O(logN^2)
        最終可以過測資 , 但時間與空間都不好
"""

class Solution:
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        
        def recursion(i,j) : 
            
            if (i>j) : return None 
            
            mid = (i+j) // 2 
            
            if (mid==0 or nums[mid-1] != nums[mid]) and (mid == len(nums)-1 or nums[mid+1] != nums[mid]) : 
                return nums[mid] 
            
            else : 
                
                left = recursion(i , mid-1) 
                right = recursion(mid+1 , j) 

                if left is None : return right 
                elif right is None : return left 
                else : return None
        
        return recursion(0 , len(nums)-1)
    

""" 
    解法二. 
        binary search , 這一題判斷答案在左或右的方式真的蠻絕的 , 
        速度有明顯提昇 , 但實際數值上沒有跟上述的logN^2算法差太多
        
        速度還不錯 , 空間略差
"""
class Solution:
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        left , right = 0 , len(nums) - 1 
        
        while left <= right :
            
            mid = (left+right)//2
            
            if (mid==0 or nums[mid-1] != nums[mid]) and (mid==len(nums)-1 or nums[mid+1] != nums[mid]): 
                return nums[mid] 

            # 判斷答案在左半還是右半
            # 如果mid index為偶數 , 那檢查他下一個值是否跟他一樣 , 如果一樣代表答案在右半
            if mid % 2 == 0 :
                # 我這邊實際上沒有考慮到會不會index out of range , 但基本上照著合理邏輯的binary search不會造成這個狀況
                if nums[mid] == nums[mid+1] : 
                    left = mid + 1 
                else : 
                    right = mid - 1 
                
            else :  
                
                if nums[mid] == nums[mid+1] : 
                    right = mid - 1 
                else : 
                    left = mid + 1 
                
        return None
        
        
        
        
    
# test_case = [3,3,7,7,10,11,11]
test_case = [0,1,1]
S = Solution()
print(S.singleNonDuplicate(test_case))