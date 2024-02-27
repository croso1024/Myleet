""" 

    題意:   
        給定一個 n x n integer matrix grid.         
        要返回有多少個 row/column pair是完全一樣的( equal array )
        
    思路:
        這一題的naive solution , 我想應該是先在任意維度走O(N) , 把所有row/column都建到hashmap ,
        接著從另外一個維度走O(N) , 一次看有多少個配對到
        (由於可能我一開始用列來建表, 這些列就有一些是完全一樣的 , 所以得用hashmap 而不是hashset , 即額外要紀錄出現次數)

        雖然我覺得這一題有北七 , 但這個解法的速度很優,空間也很不錯
"""
from typing import List 

""" 
    解法一. 雖然我覺得這一題有北七 , 但這個解法的速度很優,空間也很不錯
"""
class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        
        hashmap = dict()
        sol = 0 
        # use row as key of hashmap  
        for i in range(len(grid)): 
            
            tuple_row = tuple(grid[i]) 
            
            if tuple_row in hashmap: 
                hashmap[tuple_row] += 1 
            else : 
                hashmap[tuple_row] = 1
                
        # then traverse the column of the matrix 
        
        for i in range(len(grid)): 
            
            temp = tuple([ grid[j][i] for j in range(len(grid))]) 
            
            if temp in hashmap  : sol += hashmap[temp] 
                
        return sol