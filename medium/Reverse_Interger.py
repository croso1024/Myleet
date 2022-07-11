class Solution:
    def reverse(self, x: int) -> int:
        if x>0:  
            output = ""
            for digit in str(x)[::-1]:
                
                output += digit  
            
            while output[0] == 0: 
                output.pop(0) 
            return int(output) if len(str(bin(int(output))))-2 <=31  else 0 
        elif x == 0: 
            return 0
        else:
            x = abs(x)
            output = ""
            for digit in str(x)[::-1]:
                output += digit  
            while output[0] == 0: 
                output.pop(0) 
            return -1*int(output) if len(str(bin(int(output)))) -2 <=31  else 0

S = Solution()
print(S.reverse(x=-1534236469))
