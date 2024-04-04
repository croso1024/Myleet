
from math import floor 
class Solution:

    def intToRoman(self, num: int) -> str:

        refVal= {1:"I" , 5:"V" , 10:"X" , 50:"L" , 100:"C" , 500:"D" , 1000:"M"}
        ref = [1,5,10,50,100,500,1000]
        solution = ""
        probe = 6 

        while (num > 0) :
            print(num , solution , probe)
            if num >= ref[probe] :
                x = floor(num // ref[probe])
                if (x == 4 and probe+1 <= 6) :
                    solution += refVal[ref[probe]] + refVal[ref[probe+1]] 
                elif (x == 9 and probe+2 <= 6 ): 
                    solution += refVal[ref[probe]] + refVal[ref[probe+2]] 
                else : 
                    solution += refVal[ref[probe]] * x  
                num -= (x * ref[probe])
            else : 
                probe -= 1 
                
        return solution
    
class Solution:

    def intToRoman(self, num: int) -> str:
        refVal= {1:"I" ,4:"IV" , 5:"V" ,9:"IX", 10:"X" ,40:"XL" ,
                 50:"L" , 90:"XC"  
                 , 100:"C" ,400:"CD", 500:"D" , 900:"CM" , 1000:"M"}
        ref = [1 , 4 , 5 , 9 , 10 , 40 , 50 , 90 , 100 , 400 ,500 , 900 ,1000]
        
        probe = len(ref) - 1 
        solution = ""
        while num > 0 : 
            
            if num >= ref[probe] : 
                solution += refVal[ref[probe]] 
                num -= ref[probe]
            else : 
                probe -= 1 
        return solution


S = Solution() 
# print(S.intToRoman(23))
# print(S.intToRoman(3))
# print(S.intToRoman(153))
# print(S.intToRoman(58))
print(S.intToRoman(1994))
            
            