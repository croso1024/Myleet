""" 
    題意:
        給定一個字串 , 當中只包含 "(" , ")" , "*" 三種字符 , 題目要我們返回字串是否有效
        有效的定義如下:
            - 所有的"(" 要有對應")" , 反之亦然
            - "(" 要優先於 ")" 出現
        
        而"*" 可以被視為萬用符號 , 作為左or右括號 , 也可以視為空字串        
        
    思路:
        我的想法是使用stack , 有點類似於一般的檢查括號有效性, 但我們多了萬用字串可以作為免死金牌
        , 而多出的萬用字串也不一定需要被使用到     .
        
        唯一要注意的是在遇到")"要進行消除時 , 可以優先使用"(" ,
        避免亂用"*"去消最後剩下"("的情況 .
        
        但難處在於如何優先使用"("  , 我寫了一個暴力解,在時間與空間就算很不錯了 
        而Solution去看別人作法 , 則是我先前有想過的紀錄index , 只是將其具體化為code
           
"""

""" 
    解法一. 暴力解去處理優先使用"(" 
        實際上暴力解就速度就已經很不錯了 , 空間也很好
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = [] 
        # record the amount of left parenthesis in stack 
        lp = 0 
        
        for symbol in s : 
            
            if symbol == "*" : 
                stack.append(symbol)
            
            elif symbol == "(": 
                stack.append(symbol)
                lp += 1 
            
            else : 
                
                if not stack : return False 
                
                if lp > 0 : 
                    
                    star = 0 
                    while stack : 
                        
                        item = stack.pop() 
                        
                        if item == "*" : 
                            star += 1 
                        
                        else : 
                            lp -= 1 
                            break 
                    
                    for i in range(star): 
                        stack.append("*")
                
                else : 
                    
                    stack.pop() 
        
        # 走完後不代表就是有解 , 但stack只會剩下"("與"*"的組合
        lp = 0 
        for symbol in stack : 
            
            if symbol == "(" : 
                lp += 1 
            
            else : 
                
                if lp > 0 : 
                    lp -= 1  
        
        return True if lp == 0 else False                  
            
   
                    
                 
""" 
    解法二. 
        分別用兩個stack來儲存"*"與"(" , 但儲存的方式為index
        一樣在遇到")"時優先使用"("來消除 , 消除完之後我們只要確認一件事情 
        所有的 "(" 右邊都要有 "*" 這樣就可以了
        
        這個解的空間更好 , 只是時間反而退步 , 我猜測是因為測資太小 , TC的優勢沒出來
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star_stack = [] 
        left_stack = [] 
        
        for i in range(len(s)): 
            
            if s[i] == "*":
                star_stack .append(i) 
                
            elif s[i] == "(" : 
                left_stack.append(i) 
                
            else : 
                
                if not star_stack and not left_stack : return False 
                
                if left_stack : 
                    left_stack.pop() 
                    
                else : 
                    star_stack.pop() 
        
        # 走到這邊,所有的")"都被消除了 , 接下來只要確認所有的"("右邊都有"*" 
        
        while left_stack and star_stack :
            
            # 如果"("的index比"*"還大,就是False了
            if left_stack[-1] > star_stack[-1] : return False 

            left_stack.pop()
            star_stack.pop()  

        # 跳出代表至少有一個stack為空 , 如果left_stack空了就是True , 否則為False 
        
        return True if not left_stack else False 
 

            

                
                