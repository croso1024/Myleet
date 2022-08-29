# 因為不能使用除法　--> 
#       可以的話只要全部乘起來O(N) 
#       再用O(N)去一個個除 就能有解 
# 要考慮到有0的狀況,  若list有兩個0 則解就都是0 
# 此題大概花25分鐘解出  ,使用兩個Space O(N) 來儲存由前往後 與 由後往前的連乘
# 在index處的解就是 forward[index-1] * backward[index+1] 代表略過該index 
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        length = len(nums)
        if 0 in nums:   # take big-O(N)
            pos = nums.index(0) 
            total = 1 
            for element in (nums[:pos] + nums[pos+1:]) : 
                total *= element 
            
            solution = [0] * length
            solution[pos] = total 
            return solution 

        else:
            forward = [None] * length 
            backward = [None] * length

            base = 1 
            for i in range(length): 
                base *=  nums[i]
                forward[i] = base 

            base = 1 
            for j in range(length-1 ,-1 ,-1 ) :
                base*= nums[j]  
                backward[j] = base 
            #print(f"forward : {forward} , backward:{backward}")

            sol = [None] * length
            
            for index in range(length): 
                if  length-1 > index > 0 :
                #if not index == 0 and not index == length - 1 : 
                    sol[index] = forward[index-1] * backward[index+1]
                else: 
                    if index == 0 : 
                        sol[index] = backward[index+1]  
                    else: 
                        sol[index] = forward[index-1]

            return sol 


# C =Solution() 
# print(C.productExceptSelf([1,2,3,4]))

# 第二個解太過天才 O(1)的空間使用,
# 速度過慢, 但空間使用量贏過80%
class Solution_fromDiscuss : 
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        sol = [1 for  i in nums]

        left ,right = 1 ,1 

        for index in range(len(nums)):
            #print(f"Start: Solution :{sol} , left: {left},right : {right}")
            sol[index] *= left 
            sol[-1-index] *= right 
            left *= nums[index]
            right *= nums[-1-index]
            #print(f"End: Solution :{sol} , left: {left},right : {right}")
            #print("---------------------------------------")
        return sol
#D = Solution_fromDiscuss() 
#D.productExceptSelf([1,2,3,4])


#第三種解 比較能夠理解,但速度不比我的第一種快, 空間則是略優
class Solution_fromDiscuss2: 
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        solution = [1] * len(nums)
        accumulate = 1 

        # 第一階段做順向的連乘, 注意是先賦值給解 才做乘法
        for index in range(len(nums)): 
            solution[index]  *= accumulate 
            accumulate *= nums[index]

        accumulate = 1 
        for index in range(len(nums)-1 , -1 ,-1): 
            solution[index] *= accumulate
            accumulate *= nums[index] 
        
        return solution

#E = Solution_fromDiscuss() 
#print(E.productExceptSelf([1,2,3,4]))

from random import randint as r 
from time import time as t 
testSet = [  [r(0,99) for i in range(50*j)] for j in range(20) ] # Test data 
def Testing(testSet , *objectSet): 
    time_table = [0] * len(objectSet) 

    for i,algorithms in enumerate(objectSet):
        start = t() 
        for test in testSet: 
            algorithms.productExceptSelf(test)
        end = t() 
        time_table[i] = end-start 
    
    print(time_table)

A = Solution()
B = Solution_fromDiscuss()
C = Solution_fromDiscuss2()
Testing(testSet , A,B,C)

# 反而是我的解法最快 , 但也只有贏過40%