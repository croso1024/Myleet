class Solution:
    def myAtoi(self, s: str) -> int:
        self.solution = "" 
        self.temp = []
        self.sign = None
        self.terminate = False 
        for i,char in enumerate(s):  
            if char == " ": 
                continue 
                
            if self.isDigit(char): 
                self.temp.append((i,char))  
            else : 
                if char in "+-" and i+1<len(s) and self.isDigit(s[i+1]) : 
                    pass
                else : 
                    break 
                    
                    
                    
                    
        if self.temp: 
            start = self.temp[0][0]
            if start-1>=0:  
                self.sign = s[start-1]
            for item in self.temp: 
                if item[0] == start: 
                    self.solution+=item[1] 
                    start+=1 
                else : 
                    break 
        
       
            while self.solution[0] == "0":
                if len(self.solution) >1 : 
                    self.solution = self.solution[1:]
                else: 
                    break
         
        else: 
            self.solution = "0" 
        
        self.isOutRange() 
        return self.solution 
        
     
     
     

    def isDigit(self,char): 
        return char in "0123456789"
    
    def isOutRange(self): 
        if self.sign : 
            self.solution = eval(self.solution) if  not self.sign== "-" else -eval(self.solution) 
        else: 
            self.solution = eval(self.solution)
        
        if self.solution>(pow(2,31)-1) :
            self.solution = pow(2,31) - 1 
        elif self.solution<-pow(2,31) :
            self.solution =  - pow(2,31) 

    
C = Solution()
print(C.myAtoi("   -2323"))


