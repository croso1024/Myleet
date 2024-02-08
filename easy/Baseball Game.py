""" 
    題意:   
        給定一連串operations , 每個operation都會執行以下其中一個操作
        - integer x  : 加上一個新成績x
        - symbol '+' : 將前兩個成績加總作為新成績加在紀錄
        - symbol 'D' : 將前一個成績乘上2作為新成績加在紀錄
        - symbol 'C' : 將前一個成績移除
        
        要求計算經過一連串操作後,成績表上的總和
        題目告知所有操作都是有效的
    
    思路: 
        其實就是給定一連串數字操作總和 , 最直觀的想法就是一個list和並指向目前最新值index
        最後再做加總或著在過程中加總不影響整體複雜度
"""
from typing import List 
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = list() 
        probe = -1 
        solution = 0 
        
        for operation in operations : 
            
            if operation == "+" :  
                record.append(  record[probe] + record[probe-1]    )
                solution += record[probe] + record[probe-1]
                probe += 1
            elif operation == "D" : 
                record.append( record[probe]*2 )
                solution += record[probe]*2
                probe += 1
            
            elif operation == "C":
                
                solution -= int(record.pop())
                probe -= 1 
                
            else : 
                solution += int(operation)
                record.append(int(operation))
                probe += 1 
        
        return solution 