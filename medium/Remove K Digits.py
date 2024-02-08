""" 
    題意 :
        給定一組數字字串 , 以及整數k 
        要求返回將數字字串移除掉k個digits後的最小值 , 
        注意如果移除完後有 leading-zero , 則zero不算 
        如過移除到空了也是等於0
        
    思路 : 
        我仔細用了幾個case去想移除策略 , 
        並不是盲目去移除最大的那個值就好 , 同時有個比較隱晦的觀察 : "移除一個數字後 , 會讓其左方的數字退後一位 , 但不影響其右方的數字位數" 
        換句話說移除靠前的數字比起直接移除最大的數字有用 . 
        
        因此我的策略上就是從最前方開始決定要移除的數字 , 以stack來保存當作解答的字串 , 並且以stack頂端作為比較使用 
        如果新的數值大於等於當前stack的頂端 , 就可以利用k-1去移除該數值繼續比較 , 
        若是小於stack的頂端 , 則可以將stack的頂端移除 , 並將新數值加入stack .
        比較需要特別注意的是遇到 0 , 我認為比較簡單的處理就是照樣把0以上方的規則加入stack , 在最後output answer時移除leading-zero
        ----------------------
        
        Follow我自己上面的邏輯來寫 , 還是會出現一些小bug , 例如"12345",k=2 , 我會優先移除掉2,3 導致答案是145而不是最佳的123 
        所以我去看Solution , 較為正確的理解將數字變小應該是 "盡可能保留升序 , 去掉降序的部份" , 這一點使用monostack來完成就可以
        
"""

""" 
    解法一. follow我原本的邏輯 , 會有一些bug
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = list()  
        if k == len(num) : return "0"

        stack.append(num[0])

        for digit in num[1:] :  
            
            if k > 0 : 
                
                if int(digit) > int(stack[-1]) : 
                    k -= 1 
                
                
                elif int(digit) == int(stack[-1]) : 
                    stack.append(digit)
                
                else : 
                    
                    stack.pop() 
                    stack.append(digit) 
                    k -= 1  
            
            else : 
                stack.append(digit)

        if k > 0 : 
            for i in range(k) : stack.pop()

         
        # covert the stack to digits string , then remove leading-zero   
        sol = ""
        for digit in stack :    sol += digit  
            
        
        return str(int(sol))
    
""" 
    解法二 . 使用Monostack去盡可能保留升序 , 移除降序的部份
        速度與空間都不錯 , TC:O(N) , MC:O(N)
"""

class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k : return "0"
        
        monoStack = list() 
        monoStack.append(num[0])  
        
        
        for digit in num[1:]:  
                
            # 保留升序 , 移除降序的部份
            while k>0 and monoStack and int(monoStack[-1]) > int(digit) : 
                monoStack.pop() 
                k -= 1 
            monoStack.append(digit)

        # 因為我們都是keep升序 , 或至少不降序 , 因此若k有剩,就pop掉尾巴        
        if k > 0 : 
            for i in range(k) : monoStack.pop() 

        sol = "" 
        for digit in monoStack:  
            sol += digit
        
        
        
        # 我原本是使用int來處理remove leading zero , 但會有些小bug
        # 這邊的操作是用來規避一些超級大的數字 , 因為超級長的數字字串無法轉成int() , 
        # 最後避免sol全部被移除 , 要留下if-else expression
        probe = 0 
        while probe < len(sol) and sol[probe] == "0"  : 
            probe += 1 
        
        return sol[probe:] if sol else "0"