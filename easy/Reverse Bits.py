""" 
    此題給定一個二進制的數字 , 長度為32bit , 要我們反轉這個二進位數字表示的string , 再將其轉換為10進位數字返回
    
    這邊就是用build-in function去兜 , 有個小地方一開始沒有注意到是題目給定一定會有32bit的長度 , 
    因此需要在sol後方去補0 ,
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        ref = bin(n)[2:]
        sol = "" 
        for i in range(len(ref)-1, -1,-1): 
            sol += ref[i] 
        while len(sol) < 32 :  
            sol += "0"
        return  int(sol , base=2)
        
        
        
        
test_case = 0b00000010100101000001111010011100 

S = Solution() 
print(S.reverseBits(test_case) )