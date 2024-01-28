
class Solution:

    # 先拆解 "/" , 取出出了斜線以外的元素先放進list 
    
    def simplifyPath(self, path: str) -> str:
        
        ref = path.split("/")     
        # init一個stack
        # 定義遇到不同內容的反應 
        # 1. ".." 代表返回上一層 , 要pop掉 stack最上(如果有東西)
        # 2. "." 實際沒有要幹麻 pass 
        # 3. "directory or file" 加入stack   
        # 4. "" , 實際上這也沒有要幹麻
        
        stack = [] 
        
        
        for item in ref:  
            
            if item == "" : pass 
            elif item == "." : pass 
            elif item ==".." : 
                
                if stack : stack.pop() 
                else : pass 
                
            else : 
                stack.append(item) 
        
        # 最後 ,stack只會保存有效的文件夾名稱或檔案 , 我們在其中穿插 "/" 作為答案  
        if stack : 
            sol = ""
            for directory in stack :  
                sol = sol + "/" + directory
            return sol 
        else :
            return "/"
        