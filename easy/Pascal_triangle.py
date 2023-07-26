class Solution:
    def generate(self, numRows: int) :
        # self.result = [ [None] for i in range(numRows) ]
        self.result =  [  [ None for i in range(j) ] for j in range(1,numRows+1)  ]
        self.result[0] = [1] 
        for i in range(1 , numRows): 
            
            self.result[i][0] = 1 
            self.result[i][i] = 1 

            for j in range(1,i): 

                self.result[i][j] = self.result[i-1][j-1] + self.result[i-1][j]
        return self.result 

