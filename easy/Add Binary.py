""" 
    給定兩個binary的字串 , 以binary的形式將他們相加。 
    可以直接通過語言內部二進制轉十進制的一些操作直接完成,但沒意思
    
    這一題的想法上 ,雖然是在DP的catagory , 但我覺得應該是可以雙指標完成 ,
    從最後一位數開始相加 , follow一定的規則 , 在透過一個變數保存前一位是否有進位就可
    
    
""" 

""" 
    解法一. 內建function直接來
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2)))[2:]
    

""" 
    逐位數的相加 , 這邊Add函數邏輯有點麻煩 , 還要處理進位產生的額外數字
    -> 過不了 , 感覺這個方法有點自亂陣腳
"""
class Solution:

    def addBinary(self, a: str, b: str) -> str :
        
        if a=="0" : return b
        elif b =="0" : return a 
        
        result = ""
        
        # padding the "0"
        if not len(a) == len(b) : 
            if len(a) > len(b): 
                b = "0" * (len(a) -len(b)) + b 
            else : 
                a = "0" * (len(b)-len(a) ) + a 
        
        def Add( a,b ) : 
            nonlocal res 
            if a == "0" and b == "0" : 
                if res : 
                    res = False 
                    return "1"
                else : return "0"
            elif a == "1" and b == "1" : 
                if res : 
                    res = True
                    return "1" 
                else : 
                    res = True 
                    return "0"
            else : 
                if res : 
                    res = False 
                    return "0" 
                else : return "1"                    
            
            
        result = ""
        res = False 
        
        for index in range(len(a)-1 , -1 , -1) : 
            
            result = Add( a[index] , b[index]  )  + result  

        if res or result[0] == "0": 
            return "1" + result
        else : 
            return result


""" 
    解法三 .
        直接轉成十進位後相加 , 然後從後往前遇到2就進位 
        最後手上還拿著進位 , 就再補1在最前方
        
        這個解法就時間和空間都還不錯了
"""

class Solution:
    
    def addBinary(self, a: str, b: str) -> str :
        
        temp = str(int(a) + int(b))
        result = "" 
        res = False 
        
        for i in temp[::-1] : 
            
            if i == "0" : 
                
                if res : 
                    res = False 
                    result =  "1" +result
                else : 
                    result =  "0" +result 
                
            elif i == "1" : 
                
                if res : 
                    result =  "0" + result
                else : 
                    result = "1"+result
                    
            elif i == "2" : 
                
                if res : 
                    result =  "1"  + result 
                else : 
                    res = True 
                    result = "0" + result 
        
        # 全部走完以後 , 如果是有進位拿在手上 , 就再加一位 
        
        return "1"+result if res else result
                    
                
test_case = [("11","1") , ("1010","1011")]