# 實做書中，使用memo 且Top down recursion的fibonacci 
def fibo(n): 
    
    table = dict() 
    table[0] = 1 
    table[1] = 1 
    
    def recursion(n): 
        
        if n in table: return table[n]
        
        table[n-1] = recursion(n-1) 
        table[n-2] = recursion(n-2)
        
        return table[n-1] + table[n-2]
    
    return recursion(n) 

print(fibo(5))

    
# 實做由下而上 , 遞推 + Space complexity optimize的fibo
def fibo_spaceOPT(n) : 
    if n == 0 or n == 1 : return 1 
    
    temp = [1,1]
    
    for i in range(2 , n+1): 
        solution = temp[0] + temp[1] 
        temp[0] , temp[1] = temp[1] , solution  
    return solution 

print(fibo_spaceOPT(5))
        
        