""" 
    這題要將給定了資料夾路徑轉換為canonical form 
    題目定義canonical form指:
    1. 所有的路徑使用"/"開頭 
    2. 任意的兩個資料夾使用/作為分隔
    3. 路徑末端不能有/
    4. 路徑上只會有從root到目標資料夾或檔案的路徑 ,不會出現.和.. 
    題目有給定string的開頭會是/
"""

""" 
    思路 : 
        這一題我原先的想法是透過stack , 去一個個疊字元然後看見字元做相應處理 , 但實在是太瑣碎 .
        後來看東哥思路 , 主要是透過split("/")去進行分割 , 然後再透過stack來處理 , 這麼做確實比較合理
        我們先透過這這種方式過濾 , 讓stack保存有效的目錄最後做個解析   
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # 我們使用python的list搭配 append , pop來完成stack
        stack = list() 
        path = path.split("/") 


        # 先透過/去分割 , 把分割完的內容逐一加入        
        for item in path :
            if item == "" : pass 
            elif item =="." : pass 
            elif item == ".." : 
                if len(stack) == 0 : pass 
                else : stack.pop() 
            else : stack.append(item) 

        # 將stack的資料做後處理 
        
        result = ""
        
        while stack : 
            
            result = "/" + stack.pop() + result 

        if len(result) == 0 : return "/"
        
        return result 
        