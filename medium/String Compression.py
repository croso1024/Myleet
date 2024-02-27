""" 
    Given a chars array , we need to compression it to another representation.
    I feel a little bit cofuse in the part that the problem ask me 
    'should not be return compressed string s separately , stored in the input character array'
    And we need modify the input array to return new length of array
    " Must use constant extra space "  

    Because we need in-place modify the input array , so we use two pointer in
    the array directory
"""
from typing import List 
class Solution:
    def compress(self, chars: List[str]) -> int:
        # counter for the length of modifed array 
        solution = 0 
        insertPointer = 0 

        prevChar , prevFreq = None , 0 

        for i in range(len(chars)): 

            if prevChar and prevChar == chars[i] : 
                prevFreq += 1 

            # have different prevChar
            elif prevChar : 
                
                chars[insertPointer] = prevChar 
                insertPointer += 1 

                if prevFreq > 1 : 
                    for freq in str(prevFreq)  :
                        chars[insertPointer] = freq 
                        insertPointer += 1 

                prevChar = chars[i]
                prevFreq = 1 

            else : 
                prevChar = chars[i] 
                prevFreq = 1 
        
        # put the prefChar and prevFreq to the char 
        chars[insertPointer] = prevChar 
        insertPointer += 1 
        if prevFreq > 1 :
            for freq in str(prevFreq):
                chars[insertPointer] = freq 
                insertPointer += 1 
        
        return insertPointer












        return solution 