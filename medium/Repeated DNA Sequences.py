""" 
    題意:   
        已知一個DNA序列是由字母 A,C,G,T所組成 , 我們的任務是要找出在一串給定的DNA序列中 ,
        所有長度為10並重複出現的片段

    思路: 
        我的直覺想法是sliding window , 利用一個長度為10的window去掃略
        把所有的片段作為key在dict中儲存出現的次數即可 , 但這麼做有可能會使得空間複雜度炸裂

        實際上這個解反而是時間複雜度不夠快,空間還不錯 

"""
from typing import List 

class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10 : return []

        hashMap = dict()  
        
        
        for i in range(len(s) - 10 +1) : 
            
            if s[i:i+10] in hashMap : 
                hashMap[s[i:i+10]] += 1 
            else  :
                hashMap[s[i:i+10]] = 1 
                
        sol = [] 
        for key , value in hashMap.items() : 
            
            if value > 1 : 
                sol.append(key)
        
        return sol
        

""" 
    解法二.就改為放set , 速度更快一點
"""

class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10 : return []

        record = set()  
        sol = set()
        
        
        for i in range(len(s) - 10 +1) : 
            
            if s[i:i+10] in record : 
                sol.add(s[i:i+10])
            else  :
                record.add(s[i:i+10])
                
        
        return list(sol)