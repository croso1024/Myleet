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
    
    
    
class Solution2: 
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0 
        if len(s) == 1  : return 1 

        left_probe = 0 
        right_probe = 1
        size = len(s)
        #temp = s[left_probe]
        table = {s[left_probe]:0} 
       
        while right_probe < size :
            
            #print(temp ,right_probe , left_probe)
            #if not s[right_probe]  in table.keys() : 
            if  table.get(s[right_probe],-1) == -1 : 
                #temp += s[right_probe] 
                #table.update({s[right_probe]:right_probe})
                table[s[right_probe]] = right_probe
            else : 
                if table[s[right_probe]] < left_probe : 
                    #temp+= s[right_probe] 
                    table[s[right_probe]] = right_probe 
                
                else: 
                    #temp = temp[table[s[right_probe]]+1:] + s[right_probe] 
                    #temp = temp[table[s[left_probe]]+1:] + s[right_probe]
                    left_probe = table[s[right_probe]]+1 

                    table[s[right_probe]] = right_probe

            right_probe +=1  
            # sol = max(sol,len(temp))
            sol = max(sol , right_probe-left_probe)
        return sol 
    
    
    
    
    
S = Solution2() 
import time 
t1 = time.time()
print(S.lengthOfLongestSubstring("bbbbb"))
print(S.lengthOfLongestSubstring("dvdf"))
print(S.lengthOfLongestSubstring("abcabcbb"))
print(S.lengthOfLongestSubstring("pwwkew"))
print(time.time() - t1)