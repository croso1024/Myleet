import time
from typing import List 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## slow method 
        number =  ""
        for i in digits:
            number += str(i)
        return list(str(eval(number) + 1 )) 
    def plusOne_2(self, digits: List[int]) -> List[int]:
        number = ""
        def plus(x): 
            nonlocal number 
            number += str(x) 
        [plus(i) for i in digits] 
        return list(str(eval(number) + 1 )) 

testman = Solution()
listt = [1,2,1,2]

t1 = time.time()
testman.plusOne(listt)
t2 = time.time()-t1

t3 = time.time()
testman.plusOne_2(listt)
t4 = time.time() -t3 
print(t2)
print(t4)
print(t4-t2)