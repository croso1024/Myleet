class Solution: 
    table = { 
    
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    def romanToInt(self, s: str) -> int:
        string = list(s)  
        sol = 0 
        for i,char in enumerate(string):
            if char == "I" or char == "X" or char =="C" : 
                #next char: 
                if not i == len(string)-1:
                    next_char = string[int(list(self.table.keys()).index(char)+1 )]
                    next_char2 = string[int(list(self.table.keys()).index(char)+2 )]
                    if string[i+1] == next_char or string[i+1] == next_char2: 
                        
                        sol -= self.table[char]
                    else : 
                        sol += self.table[char] 
                else: 
                    sol += self.table[char] 
            else: 
                sol += self.table[char] 
        return sol 
    
    
S = Solution() 
sol = S.romanToInt("IV")
print(sol)