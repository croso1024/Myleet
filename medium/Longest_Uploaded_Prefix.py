class LUPrefix:

    def __init__(self, n: int):
        
        self.createTable = [False for i in range(n)] 
        self.Longest = 0  
        self.size = n
    def upload(self, video: int) -> None:
        
        self.createTable[video-1] = True 
        
        for i in range(self.Longest , self.size): 
            
            if self.createTable[i] :  
                pass 
            else : 
                self.Longest = i 
                return 
        self.Longest = self.size 
        
        
    def longest(self) -> int:
        return self.Longest
        
