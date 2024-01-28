""" 
    思路 :
        此題給定一個array, array內的值在 [1,n]的區間 , 並且總共有n+1個數字 ,
        題目給定有一個數字會重複出現(2次或以上) , 在不修改array並使用constant space的情況下找出哪個數字是重複的 
        這題看上去能想得鴿籠原理 , 必然有重複的數字 , 但要用constant space找重複是主要挑戰

        這一題不準修改array + constant space的限定直接拘束了 sorted 或透過hashtable的作法    
        
        -> 去看了解 ,發現這題也可以雙指標 ,把array想像成再找linked-list cycle來操作 ,
        -> 當兩個指標相遇就是duplicate的元素
"""


""" 
    這題思想上的難點在於將其和Linked-list相連 , 
    實際上這個array內的每個元素值 , 可以想像成就是一個節點的next
    [1,3,4,2,2] ,轉化為  0 -> 3 -> ( 2 -> 4 -> 2 ) , 並且有cycle在內
    所以nums[i]的值本身就是節點的val,也代表著next是array中的哪個element 
    
"""
from typing import List 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]
        # 題目給定了 1到n的區間 , 共有n+1個數字 , 換句話說所有array內的值當作索引都不會index out of range 
        # 透過floyd's cycle detect algorithms來做 , 把array的值當作連通得下一個節點
        while True :
            slow = nums[slow] # 一次走一步
            fast = nums[ nums[fast] ] # 一次走兩步
            if slow == fast : break 
            
        # 我們找得到相同點就代表有cycle,  只是要找重複的點 -> cycle的起始點
        # 隨便初始化一個指標回到原點 , 用一樣的步調來走
        slow = nums[0]

        while slow!=fast : 
            slow = nums[slow]
            fast = nums[fast] 
        return slow 
        
        
        

# test = [18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]
test = [1,2,1,3]
S = Solution() 
S.findDuplicate(test) 