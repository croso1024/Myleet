""" 
    題意:
        給定一個整數array , 要我們找是否有132-pattern出現
        132-pattern的定義: 
        
        array中的3個index , i , j , k滿足 i<j<k , 且 array[i] < array[k] < array[j]

    思路: 

        我認為這一題應該可以一次travers完成 ,
        需要一直去keep左半邊最小值是多少 , 而剩下的問題在於快速判斷右半邊有沒有值介於左半的最小到目前中間值
        2,3,5,4,1

        只能說這一題的O(N)解法相當難以想出來 , 建立leftMin list後反著traverse array,
        有些類似monostack的感覺 , 我們把stack中已經低於leftMin的值給pop掉 , 因為在反著traverse的過程中 leftMin只會越來越大
        而若stack頂端的值大於leftMin也大於中間值 , 則把中間值放入stack, 
        起先我的疑惑在於這樣會不會剛好中間值能跟在stack非頂端的值組成132 , 但實際畫出來可以想到 , 若stack非頂端的值能夠和中間值組132 , 
        那該值必定早就在先前以stack[-1]作為中間值時組合出132了
        
        
"""

""" 
    解法一. naive solution take O(N^2) , Time limit exceed 
"""
from typing import List 
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3 : return False 
        
        # left_min[i] 代表 min(nums[0:i+1])
        left_min = [None for i in range(len(nums))]
        left_min[0] = nums[0] 
        
        for i in range(1 , len(nums)-2): left_min[i] = min(left_min[i-1] , nums[i])  
        
        for center in range(1 , len(nums)-1): 
            
            if nums[center] > left_min[center-1] :  
                
                for  j in range(center+1 , len(nums)): 
                    
                    if  nums[center] > nums[j]  > left_min[center-1]: 
                        return True 
        
        return False 

""" 
    解法二.  同樣先存從左邊數來的最小值 , 

        但這次我們從右邊reverse traverse回來, 並且在過程中使用一個stack去看過的值
        只把那些比left-min大的加入stack , 當traverse到中間的值小於stack頂端的時候 , 就是把當前值加入stack(如果還是比minleft大)
        遇到 left-min大於當前stack頂端的時候則做pop
"""
from typing import List 

class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3 : return False 
        
        leftmin = [ None for i in range(len(nums))] 
        leftmin[0] = nums[0]
        
        # definition leftmin[i] = min(nums[0:i+1])
        for i in range(1 , len(nums)-2): leftmin[i] = min(leftmin[i-1] , nums[i]) 
        
        stack = list() 
        stack.append(nums[-1]) 
        
        # 在往後退的過程中 , left_min會越來越大 , 
        for j in range(len(nums)-2 , 0 , -1 ):
            # 有幾種case: 
            # 1. 中間的值j 沒有大於left_min , 就直接pass 
            # 2. 中間的值j 大於當前left_min , stack頂端則大於left-min , 小於j -> Solution 
            # 3. 中間的值j 大於當前left_min , 但stack頂端沒有大於left-min , pop掉這個stack頂端再次比較 
            # 4. 中間的值j 大於當前left_min , 但stack頂端大於中間的值j , 把當前的值push進入stack下一論
            
            # case.1
            if nums[j] < leftmin[j-1] : continue  
            
            # case.2
            if nums[j] > stack[-1] > leftmin[j-1] : return True 
            
            
            elif stack and stack[-1] <= leftmin[j-1] : 
                
                while stack and stack[-1] <= leftmin[j-1]: 

                    stack.pop() 
                
                
                if stack and nums[j] > stack[-1] : return True 
                # 要馬是stack空了,或著stack頂端大於nums[j]
                else : 
                    stack.append(nums[j]) 
            
            elif stack and stack[-1] > nums[j] : 
                stack.append(nums[j]) 
        
        return False 



C = Solution()
print(C.find132pattern([3,5,0,3,4]))