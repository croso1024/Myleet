

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.temp = ""
        self.result = ""
        self.s = s
        self.sLength = len(s)
        if self.sLength == 1: 
            return s 
        
        for i, char in enumerate(s): 
            self.temp = char
            self.diffusion(i)
        
        return self.result
    
    def diffusion(self,index):
    
        #case1. if answer is odd palindromic   --> get a self.result
        step = 1
        while index-step>=0 and index+step <= self.sLength -1: 
            if self.s[index-step] == self.s[index+step] :  
                self.temp = self.s[index-step] + self.temp + self.s[index+step]
                step+=1
            else: 
                break
           
        if len(self.temp) > len(self.result): 
            self.result = self.temp 
        self.temp=""
        
        #case2. if answer is even palindromic 
        step = 1
        if index+step<= self.sLength-1 and self.s[index] == self.s[index+step]: 
            self.temp = self.s[index] + self.s[index+step]
            
            while index-step>=0 and index+step+1 <= self.sLength - 1: 
                if self.s[index-step] == self.s[index+step+1] :
                    self.temp = self.s[index-step] +self.temp +self.s[index+step+1] 
                    step +=1 
                else: 
                    break
           
            if len(self.temp) > len(self.result): 
                self.result = self.temp 
            self.temp=""
            
A =  Solution() 
print(A.longestPalindrome("a"))
print(A.longestPalindrome("aba"))
print(A.longestPalindrome("babad"))
print(A.longestPalindrome("cbbd"))
print(A.longestPalindrome("ccc"))
print(A.longestPalindrome("ABCDEFFEDCBA"))
print("done")