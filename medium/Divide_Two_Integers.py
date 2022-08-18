class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True if ( dividend>=0 and divisor>0 ) or (dividend<0 and divisor < 0) else False 
        dividend , divisor = abs(dividend) , abs(divisor) 
        quotient = 0 
        step = 0  
        
        res = dividend
        
        while (dividend - (divisor<<step+1)) >= 0 :
            step+=1 
        # get maximum step 

       

        while step >= 0 and (res -(divisor<<step)) >= 0 :  
         
            quotient += 1<<step 
            res = res-(divisor<<step)
  
            if (res -(divisor<<step)) >= 0:pass 
            else: 
                while step>0:
                    step -=1 
                    if (res-(divisor<<step)) >= 0 : break 
                    else: pass 
            
        quotient = quotient if sign else - quotient 
        if quotient>2147483647 : return 2147483647
        elif quotient<-2147483648 : return -2147483648 
        else : return quotient
        

      


S= Solution() 
print(S.divide(0,1))
