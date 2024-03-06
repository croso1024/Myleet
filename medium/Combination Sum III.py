""" 
    題意:
        尋找所有可以使用k個數字湊成n的組合,同時follow以下規則
        - 只能使用數字1-9
        - 每一個數字只能使用一次 
        要求返回所有可行的組合，同時不能有重複的 ,
        不過這一題沒有說明那一個組合中的順序是否沒差 

    思路:
        直覺看起來就是要使用Backtrack , maintain一個還可以使用的number set , 然後往下展開
        因為這一題每一個數字都只能使用一次,而且還不能使用重複的,這代表我可以在往下展開的時候只留下後半的數字陣列.
        因為前半的數字陣列會在先前的展開中使用到

"""
from typing import List 

class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        solution = list()
    
        def backtrack( start :int ,  combination : list , rest:int ): 
            if rest == 0 and len(combination) == k : solution.append(list(combination)) 
            elif rest <= 0 : return 
            else : 
                
                for i in range(start , 10):  
                    combination.append(i)
                    backtrack(i+1 , combination , rest - i )
                    combination.pop() 
        
        backtrack( 1 , [] , n )
        
        return solution 

S = Solution() 
print(S.combinationSum3(k=3 , n =7) )
