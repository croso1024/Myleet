class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if digits =="" : return []

        self.table = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        self.solution = [] 
        self.temp = [""]
        self.digits_length = len(digits)

        self.recursionFind(digits , self.temp)
        print(self.solution)
        return self.solution


    def recursionFind(self,resDigits,resSolution): 

        print(f"resDigits: {resDigits}  resSolution : {resSolution}")
        # 全部用str作為往下傳遞的resSolution
        # 在每一次的遞迴中初始化self.temp 
        # 取出resSolution中的字串 , for去所有該digits對應的字元後加入temp (temp內的元素長度應該等同於該digits的位置)
        # 當self.temp的元素長度等於len(digits) 即為solution並return 
        # else的部分直接作為原始輸入為空的處理
        if resDigits: 

            self.temp = [] 

            for subSolution in resSolution: 
                for char in self.table[resDigits[0]]: 
                    self.temp.append(subSolution+char)
            self.recursionFind(resDigits[1:] ,self.temp )
        else:  
            #if len(resSolution[0]) == self.digits_length: 
            for solution in resSolution: self.solution.append(solution) 

            


S = Solution() 
S.letterCombinations("5232")

