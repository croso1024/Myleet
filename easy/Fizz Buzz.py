""" 
    Method.1 Linear traverse
"""
from typing import List 
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def check(i): 
            if i % 5 == 0 and i % 3 == 0 : 
                return 'FizzBuzz'
            elif i % 3 == 0 : 
                return "Fizz"
            elif i % 5 == 0 : 
                return "Buzz"
            else : 
                return str(i) 
        
        return [ check(i) for i in range(1,n+1)]