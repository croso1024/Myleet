from typing import List 

""" 
    暴力解
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        size = len(strs) 
        use = [ False for i in range(size)] 
        encode_table = []
        sol = [] 
        # 進行編碼 , 放入encode_table 
        for  string in strs:   
            encode = {}
            for s in string : 
                if s in encode : encode[s] += 1 
                else : encode[s] = 1 
            encode_table.append(encode)
            
        
        # 給定兩個encode , 確認是否相同        
        def check(s1:dict , s2:dict) : 
            if len(s1.keys()) == len(s2.keys()) : 
                
                for k in s1.keys() : 
                    if not k in s2 : return False 
                    elif not s2[k] == s1[k] : return False 
                return True 
            
            else : return False 
                
        for i in range(size): 
            
            if use[i] : continue

            temp = [ strs[i] ]

            for j in range( i+1 , size ) : 
                
                if use[j] : continue 
                
                if check( encode_table[i] , encode_table[j] ) :  
                    temp.append( strs[j] )
                    use[j] = True 
            
            use[i] = True 
            sol.append(temp)
        
        return sol 
        

""" 
    對每個內容 sort 
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ref =  list(   map(  lambda x :  "".join(sorted(list(x))) , strs  )  ) 
        # hashmap裡面都是存"不同的anagrams"
        hashmap = dict() 
        
        for i in range(len(strs)) : 
            
            if ref[i] in hashmap : 
                hashmap[ref[i]].append(strs[i])
            else : 
                hashmap[ref[i]] = [ strs[i] ] 
        
        return hashmap.values()
            
        
        
        
strs = ["eat","tea","tan","ate","nat","bat"] 
S = Solution() 
S.groupAnagrams(strs=strs) 
