# 這一題告訴我們, 不要寫class attr在裡面, 因為leet可能只初始化一次就要拿來解一堆問題, 要直接寫在method裡面初始化attribute
class Solution:
    def isValid(self, s: str) -> bool:

        self.stackk = []
        self.correspond = {")":"(","}":"{","]":"["}
     
        for element in s : 
   
            if element  in ["(","[","{"] : 
                self.stackk.append(element)
                
            elif element in [")","]","}"] : 
                
                if self.stackk and (self.stackk[-1] == self.correspond[element]): 
                    self.stackk.pop()
                else:
                    
                    return False 
                
                
            else : 
                pass 
        if not self.stackk : 
            
            return True 
        else: 
            
            return False 
s = Solution() 
print(s.isValid("{[]}" ))
