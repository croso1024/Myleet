class Solution:
    def hammingWeight(self, n: int) -> int:
        
        sol = 0 
        for i in bin(n) : 
            if i == "1" : sol += 1 
        return sol 