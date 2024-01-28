from typing import List 


""" 
    給定一個array有 n個數字 , 其中range在[1,n] , 返回在這個range內的所有數字但沒有出現在array中的
    ex. 給5個數字 , [1,2,3,4,3]  
    
    直觀來說就是  {1,2,...,n} - set(array)    
    
    這一題要有意義就是follow-up , 要求O(N)時間與O(1)空間
"""

"""
    解法一. built-in function    
"""
class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return list( 
                    set(range(1,len(nums)+1)) - set(nums)     
                )

""" 
    解法二. 
        解follow-up的O(N)時間與O(1)空間 
        但可以把返回的list不算進extra space

        這個說法的意義我不太確定是指什麼 , 如果直接create一個array ,然後把遇到的數字踢出 ,那也很白痴
        但確實這樣做讓空間減少很多 , 因為我使用built-in來做的時候是create兩個array
"""

class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ref = set(range(1,len(nums)+1))
        
        for num in nums : 
            if num in ref : ref.remove(num)
        
        return list(ref) 