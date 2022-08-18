class Solution:
    def generateParenthesis(self, n: int) -> list:

        #solution1 , record left and right , recursion 
        """solution = [] 
        
        def recursion(string,length,left,right): 
            if length == n*2  : 
                solution.append(string)
            
            else: 
                if right>left: return 
                else: 
                
                    if left < n :
                    
                        recursion(string+"(",length+1,left+1,right) 
                       
                    if right < n : 
                        
                         recursion(string+")",length+1,left,right+1)
                     


        recursion("",0,0,0)"""
        #return solution
        

        #solution2 Dynamic programming 
        table = [list() for i in range(n+1)]
        table[0].append("")
        for i in range(1,n+1):
            for j in range(i) : 
                
                table[i] +=["("+x+")" +y for x in table[j] for y in table[i-j-1]]
        
        return table[n]
    
        
        
        
        

s =Solution() 
sol = s.generateParenthesis(3)

print(sol)
print(len(sol))




