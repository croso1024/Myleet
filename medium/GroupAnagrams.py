from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_with_sorted_element = map( lambda element : "".join(sorted(element))  , strs )
        table = dict() 
        for index , anagram  in enumerate(str_with_sorted_element) : 
            if table.get(anagram , None): 
                table[anagram].append(strs[index])  
            else : 
                table.update({anagram:[strs[index]]}) 
        
        result = [] 
        for key , value in table.items() : 
                result.append(value)
        return result 