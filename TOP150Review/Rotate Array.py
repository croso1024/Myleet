from typing import List 

# method.1 take O(N) space  , O(N) time  , copy a reference and insert 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        ref = nums[:] 
        probe = k  
        size = len(nums) 

        for i in range(size):
            nums[ ((probe+i)  % size ) ] = ref[i] 
        return nums             
    

# method.2 take O(1) space , O(N) time 
# 這個方法遇到 nums.length % k == 0就異常 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 : return nums
        # 總共要走size步  
        size = len(nums) 
        probe = 0 
        step = 0 
        # 步驟解析 : 
        # 先尋找 probe+k的位置 , 紀錄下該值(用作下一個插入)
        # 接著將原array中位置在probe的值插在probe+k的位置   
        cur_value = nums[0]
        while step < size : 
            
            next_value = nums[ (probe+k ) % size ] 

            nums[(probe+k)% size] = cur_value 

            probe = (probe+k) % size   
            cur_value = next_value
            step += 1 
        
        
        return nums 
    
# method.3 就是只存O(K)空間 , 一樣O(N) 時間 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        #保存最後k個值
        size = len(nums) 
        k = k % size 
        temp = nums[size-k:]  
        
        for i , j  in enumerate(range(  size-k-1 , -1 , -1  )): 
            nums[size-1  - i] = nums[j]  
        
        for i ,j in enumerate(temp): 
            nums[i] = j 
        
        return nums  
        