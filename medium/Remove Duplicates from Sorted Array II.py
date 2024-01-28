""" 
    思路 :  
        本題給定一個Array , 裡面是已經經過排序的數值 , 我們要in-place的拿掉array中"重複超過兩次"的數字 , 
        亦即如果一個數字出現到第三次就將其去除  . 注意此題需要直接在原始題目給定的array上進行操作. 
        返回最終的array中有效數字的個數k , 並且此時array的前k個值就要是移除重複兩次以上數字的array

        
        我的想法可能是初始化兩個指標 , 一個指標只向當前訪問的 , 而另外一個指標則指向要替代掉的元素 
        
        訪問指標遇到新的值就將其加入替代指標的位置 , 並且紀錄當前訪問的值出現的頻率 , 如果超過兩次,就不去將值加入替代指標 ,
        注意我們不在意說原始array從超過k的位置的值.        

"""

""" 
    解法一. 基本就是follow我上述的概念 , 
        我這邊在 temp_digits 出了一個小bug , 我一開始直接 if temp_digits ,
        結果遇到temp_digits為數字0會異常 , 改為 not temp_digits is None才可
"""
from typing import List 
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        size = len(nums) 
        
        insert_probe = 0 
        check_probe = 0 
        # temp用來保存目前探索指標指到的值 , 以及他的出現頻率是否大於兩次
        temp_digits , duplicate  = None  , False
        
        # check probe 總是>= insert_probe 
        while check_probe < size :   
            # 如果前一個值和目前探測指標的值一樣 
            if not temp_digits is None and temp_digits == nums[check_probe] : 
                # 如果他目前只有出現一次 , 那ok 還可以插入 ,否則就要跳過 
                if duplicate :
                    check_probe += 1 
                else : 
                    nums[insert_probe] = nums[check_probe]
                    check_probe += 1 
                    insert_probe += 1 
                    # 更新這個值已經插入兩次了 
                    duplicate = True 
            
            # 這個值是第一次出現 , 更新temp_digits , duplicate
            else :
                nums[insert_probe] = nums[check_probe] 

                temp_digits = nums[check_probe]
                duplicate = False 
                
                check_probe += 1 
                insert_probe += 1 
        
        # 最終 insert_probe的數字大小就是我插入了幾個新值 , 即k
        return insert_probe



""" 
    解法二. 就是優化 , 希望可以加速 ,把duplicate改為數值 , 但似乎沒有啥差別
"""
from typing import List 
class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        size = len(nums) 
        
        insert_probe = 0 
        check_probe = 0 
        # temp用來保存目前探索指標指到的值 , 以及他的出現頻率是否大於兩次
        temp_digits , duplicate  = None  , 0
        
        # check probe 總是>= insert_probe 
        while check_probe < size :   
            # 如果前一個值和目前探測指標的值一樣 
            if not temp_digits is None and temp_digits == nums[check_probe] : 
                
                if duplicate < 2 :   
                    nums[insert_probe] = nums[check_probe] 
                    check_probe += 1 
                    insert_probe += 1 
                    duplicate += 1 
                
                else : 
                    
                    check_probe += 1 
                    
  
            
            # 這個值是第一次出現 , 更新temp_digits , duplicate
            else :
                nums[insert_probe] = nums[check_probe] 

                temp_digits = nums[check_probe]
                duplicate = 1
                
                check_probe += 1 
                insert_probe += 1 
        
        # 最終 insert_probe的數字大小就是我插入了幾個新值 , 即k
        return insert_probe