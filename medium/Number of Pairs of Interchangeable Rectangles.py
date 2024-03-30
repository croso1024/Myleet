from typing import List 

# hashmap + combination mathmatics solution 
from math import factorial
class Solution:

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        hashmap = dict() 
        # O(N) space complexity 
        for (width,height) in rectangles : 
            ratio = width/height 
            if ratio in hashmap : hashmap[ratio] += 1 
            else : hashmap[ratio] = 1 
        
        solution = 0 

        combination2 = lambda x : (x * (x-1))//2
        
        for ( ratio , amount ) in hashmap.items() :        
            if amount == 1 : continue        
            
            solution += combination2( amount ) 

        return solution 
            
            
""" 

C n 取 k :
 n! / (n-2)! * 2 
 => (n * n-1)/2


"""
