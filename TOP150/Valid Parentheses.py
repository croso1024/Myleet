class Solution:
    
    # use stack to solve this problem 
    def isValid(self, s: str) -> bool:
        
        stack = [] 

        ref = {")":"(" , "}":"{" , "]":"["}


        for char in s : 

            if char in ref.values() :   
                stack.append(char) 
            else : 
                
                if stack and stack[-1] == ref[char] : 
                    stack.pop() 
                else : 
                    return False 

        return True if len(stack) == 0 else False                   




