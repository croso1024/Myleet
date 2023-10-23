
""" 
    思路 :
        此題給定一個數字陣列 , 當中只會有一個數字是出現一次 , 其餘都是出現兩次 . 
        要找出那個出現兩次的值 .

        直觀的思路是hashmap , 
        我用兩個hashset , 當值第一次出現(不在hashset1) , 加入hashset1 , 如果第二次出現了就加入hashset2
        最後做difference得到解

"""

""" 
    解法一. 
        直觀的思路是hashmap , 
        我用兩個hashset , 當值第一次出現(不在hashset1) , 加入hashset1 , 如果第二次出現了就加入hashset2
        最後做difference得到解

        Time : O(N) , Space : O(N)
        
        這個解法的速度非常快 , 但空間不佳 , 我想是因為我用了兩個hashset 
"""

from typing import List 
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        set1 = set() 
        set2 = set() 
        
        
        for i in nums: 
            
            if i in set1 : set2.add(i)  
            else : set1.add(i) 
            
        return  list(set1.difference(set2))[0]

""" 
    解法二 . 實際上空間問題可以只透過一個hashmap去解決 , 就用hashmap紀錄出現次數就好 
"""
class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        hashmap = dict() 

        for i in nums: 
            if i in hashmap : hashmap[i] += 1 
            else : hashmap[i] = 1 
        
        for key , value in hashmap.items() :
            if value == 1 : return key 
        
        return 


""" 
    解法三 :
        如果要更加空間的解法 , 那可以嘗試Sort後用指標 
        注意nums array必定是奇數長度 , 因為只有1個是獨立 , 其他都是twice出現 
        
        因此sort完後從index 0開始 +2 , +2  , 獨立的term一定會出現在偶數index 
"""

class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort() 
        i = 0 
        while i < len(nums)-1 : 
            
            if nums[i] == nums[i+1] : 
                i += 2 
            else : 
                return nums[i]
        
        
        # 使用nums[i]作為回傳 , 如果nums只有一個元素 , 則回傳nums[0] , 
        # 如果答案在最後一個元素 , 則i+=2後超出while條件的話也會停在解的index
        
        return nums[i]