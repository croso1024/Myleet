

class Solution:
    table = {
        1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I" 
    }
    def intToRoman(self, num: int) -> str:
        self.num = num 
        self.result =""
        for idx, roman in enumerate(list(self.table.keys())): 
            #print(idx,self.result)
            self.parser(idx,roman)
        
        return self.result
    # def parser(self,index,Number): 
    #     count  = 0
        
    #     while self.num - Number >=0  or  ( index<=5 and   self.num - 4*list(self.table.keys())[index+1] >=0 ) or( index<=4 and   self.num - 9*list(self.table.keys())[index+2] >=0 ): 
    #         if self.num - Number >=0:
    #             self.num -= Number  
    #             self.result += self.table[Number] 
              
    #         elif self.num - 4*list(self.table.keys())[index+1] >=0: 
    #             self.num -= 4*list(self.table.keys())[index+1] 
    #             self.result +=  self.table[list(self.table.keys())[index+1]] +self.table[Number] 
                
    #         elif  self.num - 9*list(self.table.keys())[index+2] >=0: 
    #             self.num -=  9*list(self.table.keys())[index+2]
    #             self.result += self.table[list(self.table.keys())[index+2]] + self.table[Number]
    def parser(self,index,Number): 
        count  = 0
        if index<=5:
            cal1 =4*list(self.table.keys())[index+1]
        if index<=4:
            cal2 =9*list(self.table.keys())[index+2]
        while self.num - Number >=0  or  ( index<=5 and   self.num - cal1 >=0 ) or( index<=4 and   self.num - cal2 >=0 ): 
            if self.num - Number >=0:
                self.num -= Number  
                self.result += self.table[Number] 
              
            elif self.num - cal1 >=0: 
                self.num -= cal1
                self.result +=  self.table[int(cal1/4)] +self.table[Number] 
                
            elif  self.num -cal2 >=0: 
                self.num -=  cal2
                self.result += self.table[int(cal2/9)] + self.table[Number]
                
            

        
c =Solution() 
print(c.intToRoman(1994))