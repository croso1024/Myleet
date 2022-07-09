#好題目, 兩次錯誤發生在沒有考慮到" " , 還有"dvdf" ,遇到重複時不是直接歸零重算
#利用index去找發生重複的位置,保留重複的char下一個開始
#更新最大值得時候要注意真的有變大再刷新
# faster than 42% space less than 93%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.best = 0 
        self.temp = []
        for i,char in enumerate(s): 

            if char not in self.temp: 
                self.temp.append(char) 
            else : 
                self.best = len(self.temp) if len(self.temp) > self.best else self.best
                #self.temp.remove(char)
                self.temp = self.temp[self.temp.index(char)+1:]
                self.temp.append(char) 
            
        return max(self.best , len(self.temp))
S = Solution() 
import time 
t1 = time.time()
print(S.lengthOfLongestSubstring("pwwkew"))
print(time.time() - t1)