""" 
    Find out the first n ugly number , 
    ugly number is define that a number which prime factors in [2,3,5] or not any prime factor 

    the KEY is : a ugly number can be form as  (2^a)(3^b)(5^c) ,
    so the rest is how to order the value of this form ,  
    ---------------------------------------
    In this problem , the state transition function is unobviously .
    we use a pointer to record that the number of 2,3,5 last time multiply 
    So genius

"""
import math 
class Solution:
    def nthUglyNumber(self, n: int) -> int: 

        a , b , c = 0,0,0  
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(1 , n): 

            dp[i] = min(dp[a]*2 , dp[b]*3 , dp[c] * 5) 
            if (dp[i] == dp[a] * 2) : a +=1 
            if (dp[i] == dp[b] * 3) : b +=1 
            if (dp[i] == dp[c] * 5) : c +=1 

        return dp[n-1]
        
