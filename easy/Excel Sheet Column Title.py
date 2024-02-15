""" 
    題意:   
        給定一個數字columnNumber , 我們要返回他會在Excel上出現的英文號碼 
        A -> 1 
        B -> 2 
        ...
        Z -> 26 
        AA -> 27
        AB -> 28  
        
    思路:   
        依照這個邏輯推想 , AZ = 52 BA = 53      
        所以example的ZY = 26*26 + 25 = 701   
        ZAA = 26*27 + 1 = 703   
        
        但現在要的是將數字轉回英文 , 先看這數字可以除以多少次26以及其除以26的餘數 
        餘數會決定最後一個字母是什麼 , 而前方除以26的次數則決定他有幾個位數  
        
        701 // 26 = 26 -> Z   , 701 % 26 = 25 -> Y 
        每一階層除以26 , 由後往前堆數字
        
        
        27  = 26 * 1  + 1 -> AA
        130 = 26 * 5  + 0 -> DZ 
        132 = 26 * 5  + 2 -> EB
        676 = 26 * 26 + 0 -> YZ
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # unicode A->Z : 65 -> 90
        letter = lambda x :  chr(x+64+1)
        
        sol = ""
        # columnNumber -= (columnNumber % 26)
        

        # 26 * 26 -> Z + ? 
        # 26 * 27 + 1 -> Z + ? + ?
        
        while columnNumber > 0  : 
            
            sol = letter(  (columnNumber-1)%26   ) + sol 
            columnNumber = (columnNumber-1)//26
        
        return sol 
            
    

C = Solution() 
print(C.convertToTitle(701))