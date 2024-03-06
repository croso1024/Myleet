""" 
    Given n pairs and pairs[i] = [left_i , right_i] and left_i < right_i 
    two pair can connect if and only if p1=[a,b] , p2=[c,d] and b<c . 
    return the longest chain which can be formed.

    Sort the given pairs by (left,right) , and use Greedy approach or dynamic programming

    Approach.1 Dynamic programming

    I think use dynamic programming more better, but need use reverse traverse to fill out dp-table
    dp[i] is mean start from sorted-pairs[i] , the maximum length of pair chain 
    so dp[-1] = 1 
    
    dp[i] = max(dp[i], 1 + dp[j]) for j in range(i,len(pairs)) and sorted-pairs[j][0] > sorted-pairs[i][1]
    TC : O(N^2) , MC:O(N) 

    According to the result , this approach just have poor performance but still can pass test
    , so i think exist an O(n) or O(nlogn) approach
"""
from typing import List 
# class Solution:

#     def findLongestChain(self, pairs: List[List[int]]) -> int:

#         pairs.sort()    
#         size = len(pairs)
#         # initial maximum length of pairs is 1 
#         dp = [1 for i in range(size)]

#         # reverse traverse
#         for i in range(size-2 , -1,-1): 

#             # compare to later element 
#             for j in range(i , size): 
#                 # fulfill the condiction of connection
#                 if pairs[j][0] > pairs[i][1] : 
#                     dp[i] = max( dp[i] , 1 + dp[j] ) 
        
#         return max(dp)

""" 
    Another approach base on greedy algorithms , we sort the pairs by 'right_i' , 
    and every turn , we pick the element who have mimimum right_i and satisfy connect condiction
"""

class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        # sort by right_i 
        pairs.sort(key = lambda item : (item[1],item[0]) )
        # traverse and pick pairs element form a connection
        length = 1 
        cur_interval = pairs[0] 

        for i in range(1,len(pairs)): 
            
            if pairs[i][0] > cur_interval[1] : 
                length += 1 
                cur_interval = pairs[i] 


        return length 