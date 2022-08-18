
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
       # return str(eval(num1)*eval(num2)) 
        return str(eval(num1+"*"+num2))

C = Solution()
print(C.multiply("123","456")) 