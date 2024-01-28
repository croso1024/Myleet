""" 
    題意 : 
        給定一組array裡面的所有數值都不一樣
        , 我們要重新排序這個array使得當中除了頭尾以外的每個元素不等於其neighbor的平均值
        ex. nums = [1,2,3,4,5] -> [1,2,4,5,3] , 答案不只一組 , 只要找出一組解就可
    
    思路 : 
    
        <解法一 , 但有錯誤 , 有可能後面的swap會回頭導致前面的出錯>
        由於給定的array全都是不同的數值 , 因此我的想法是先進行sort , 讓元素照順序排完後
        開始走O(N) , 一旦檢測到neighbor平均等於該元素 , 就讓這個觸發的元素與下一個元素進行swap
        照理來說原先為 : 小->中->大 ,會變為 小->大->中->更大 , 這個策略能卻確保直到最後一個的前一個值都不會異常
        ex. 小->大->中->更大->更大2 , 也可以再次調換 ,小->大->中->更大2->更大 
        這個策略的時間為O(NlogN) , 空間為O(1) 

        < 解法二 , 兩個pointer從左右開始往內縮 , 一旦遇到異常就鎖定 , 當兩邊都異常後做對調 
            實際上這個解法沒有太直接肯定的邏輯 , 有點純粹像是想到就直接做下去這樣 , 但是有錯
        > 
        
        
"""

""" 
    解法二 . 內縮pointer
"""
from typing import List 

class Solution:
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        # nums.sort()
        left , right = 1 , len(nums)-2 
        
        check = lambda i : nums[i-1] + nums[i+1] == nums[i]*2
        
        while left <= right : 
            
            # 先定位到左端有異常的值 
            while  left <= right  and not check(left) :
                
                left += 1 
            
            # 再定位到右邊有異常的值
            while  left <= right and not check(right)  : 
                right -= 1 
            
            # 如果left == right 代表這個值應該就是最後一個異常值,
            # 我們要確保這個異常值的交換不會造成新的異常 ,換句話說就是找一個點來插入這個值
            if left == right :
                nums[left] , nums[0] = nums[0] , nums[left]
                
            
            # left > right , 代表沒有異常,可以return
            elif left > right : 
                return nums
            
            # 在此代表左右各自抓到一個異常 , 要來做swap
            else : 
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1 
                right -= 1 
            
            
        return nums 

""" 
    解法三. 
        sorting之後 , 左右pointer輪流添加值 , 只要畫圖出來,這一題的想法算是比較直觀
        一句話概括就是 : "錯峰出行"
"""
class Solution:
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort() 
        probe = 0 
        result = [] 
        size = len(nums)
        
        while probe < size//2 : 
            
            result.append(nums[probe])
            result.append(nums[size-probe-1])  

            probe += 1 
        if not size % 2 == 0 : 
            result.append(nums[size//2])
            
        return result 

C = Solution() 
# print(C.rearrangeArray([1,2,3,4,5,0,7,8,12,14,22,11,15]))
print(C.rearrangeArray([22,34,27,42,23,4,32,41,21,0]))
# print(C.rearrangeArray([1,2,3,4,5,6]))