"""
    Define the rule of calcultor is foremost , 
    basically , the formula need to follow multi/division first , then plus/minus , and in this problem , the formula don't have any patheness ,
    so we need to follow 
    1. M/D first , minus/plus second
    2. from left to right 

    so my strategy is calculate all multiply/division part first 
    then we get a expression that only have plus/minus , 
    so we can get solution simply 

    --- 
    after solve this problem , i think in minus/plus part , we also can use  store the temporal value as multiply/division part. 

    so-on that can save a lot of space ( dose not need simpleExpression list ) and evade another linear traverse
"""
class Solution:
    def calculate(self, s: str) -> int:
        
        # calculate the expression that only have minus/plus 
        simpleExpression = list()

        current = None
        sign = None 
        i = 0 
        while i < len(s):

            if s[i] == " ": 
                i += 1 
                continue 

            elif s[i] in ["+" , "-"] : 
                simpleExpression.append(current) 
                simpleExpression.append(s[i])
                current = None 
                
            elif s[i] in ["*","/"]  : 
                sign = s[i]
            else : 
                number = s[i] 
                while i+1 < len(s) and not s[i+1] in [" ","+","-","*","/"]  : 
                    number += s[i+1]
                    i += 1

                if not current is None  and sign in ["*" , "/"]: 

                    if sign == "*" : 
                        current = current * int(number) 
                    else : 
                        current = int(current / int(number)) 
                    sign = None 

                else : 
                    current = int(number) 

            i += 1 
        # use simple Expression find out last solution 
        if not current is  None  : simpleExpression.append(current) 
        sol = simpleExpression[0]
        for i in range(1 , len(simpleExpression)-1 , 2 ):  
            if simpleExpression[i] == "+" : 

                sol = sol + simpleExpression[i+1] 

            else : 

                sol = sol - simpleExpression[i+1] 
        
        return sol 
        

              
                



