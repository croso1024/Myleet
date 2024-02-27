""" 
    題意:
        定義ugly number是指除了2,3,5以外,該數字不能被其他質數整除
        題目給定一整數n , 要求判斷該數是否是ugly nubmer 

    思路:
        我認為一個較漂亮的解法是利用 ugly-number = (2^a)(3^b)(5^c) 這個概念
        將給定n數字作為root去展開來看 .
        
        但另外一個比較直覺的作法 , 既然題目說uugly nuumber不能被2,3,5以外的質數整除,
        那我們就嘗試去找是否有其他質數可以整除n 
        
"""

""" 
    解法一. naive approach , 
        先找出1 -> sqrt(n) 範圍的所有質數,接著一一嘗試用該數字進行整除
        大概可以處理到 2^20多位 , 但再更大就會炸
"""
from math import sqrt 
class Solution:

    def isUgly(self, n: int) -> bool:
        
        
        if n <= 0 : return False 
        prime_list = [True for i in range( n  + 1)] 
        prime_list[1] = False # 1 不是質數 
        
        for i in range(2 ,n+1) : 
            
            # 如果該數字是質數,那他的倍數都不是質數
            if prime_list[i] :  
                j = 2 
                while i * j < n+1 : 
                    prime_list[i*j] = False 
                    j += 1 
        
        # 到此,我們就拿到 1->sqrt(n)這些數字中是否是質數 
        # 我們接下來要做的就是檢查是否有其他質數可以整除n
        # 但實際上這件事有點bug , 因為我們只有列表到sqrt(n) , 
        # 舉例來說n=14 , 當我們檢查 2 可以整除14時 , 我們並沒有7是否是質數的資訊
        # 所以這個解法如果把sqrt(n)改成n , 雖然可以解決這個問題但這樣TC,MC都不好
        
        for i  in range(2, int(sqrt(n)) ):     
            
            # 如果該數字是prime , 就拿來除除看
            if prime_list[i] :      
                
                if (n % i) == 0 and prime_list[n//i] == True : 
                    
                    if i in [2,3,5] and n//i in [2,3,5 ]: pass 
                    else : return False 
                    
        return True                 
        

""" 
    解法二, 用展開的
"""
class Solution:

    def isUgly(self, n: int) -> bool:
        
        if n == 1 : return True  
        elif n <= 0 : return False  
        
        result = False         
        if n % 2 == 0 : 
            result = result or self.isUgly( n // 2 )  
        if n % 3 == 0 : 
            result = result or self.isUgly(n // 3 ) 
        if n % 5 == 0 : 
            result = result or self.isUgly(n // 5 ) 
        
        return result
        
        
        
        

S = Solution()
print(S.isUgly(n=pow(2,20)))
            
            
            
            
        