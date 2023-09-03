class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        even = lambda x : True if  9 < x < 100 or 999 < x < 10000 else False 
        result = 0
        for i in range(low , high+1 ): 
            
            if not even(i) : continue 
                
            string_number = str(i)
            mid = len(string_number) // 2  
            
            left_sum ,right_sum = 0 , 0 

            for j in string_number[:mid] : 
                left_sum += int(j) 

            for j in string_number[mid:] : 
                right_sum += int(j) 

            if left_sum == right_sum : result += 1 

        return result 