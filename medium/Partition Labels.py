""" 
    題意 :
        給定一個字串s , 我們要盡可能把其分為多個part , 但注意不可以改變順序 , 亦即分完之後再次連接起來會得到原始字串
        另外在字串中同一個char必須被分到相同的part , 回傳一個list去表示滿足此條件下每個part的長度
    
    思路 :
        既然同一個char必須分在同一塊 , 代表開始定位一個part的範圍的時候 , 
        要做的就是確保被框在這個part內的所有字串 ,都沒有在被匡選外的範出現過 .
        
        我的想法就是兩個probe , 一個鎖定當前part的起始字母 , 另一個往右掃過去確認該字母最後一次出現的index
        這個part的範圍"至少"在這兩個index中間 , 但實際上我們要對被包在這範圍內的每一個字母做這件事情 ,
        逐漸去定位完成一個part , 往復做這件事直到完成所有字母 TC:O(N^2) , MC:O(1)

        -----------
        這一題我去看了solution , 要做到TC:O(N)的核心思路在於使用hashmap去紀錄所有字元的第一次與最後一次出現 ,
        以此為基我來寫了解法二

"""

""" 
    解法一. 就是按照上述的思路 , 雖然code寫的有些凌亂 , 但實際上算是一次直接AC 

        速度很差 , 空間倒是還不錯 .如同上述說的時間複雜度大概是O(N^2)  , 但空間複雜度基本上就是O(C) , 除了保存解的陣列以外就只有用指標存值
"""
from typing import List 
class Solution:
    
    def partitionLabels(self, s: str) -> List[int]:
        
        partition = list()
        
        # 用來切分一個part的範圍
        start = 0    
        
        while start < len(s) :  
            
            interval = [start , None]
            # 從後方尋找跟char一樣的字元 , 這要作為這個part的初始邊界
            probe = start + 1 
            while  probe < len(s): 
                
                if s[start] == s[probe] : 
                    interval[1] = probe  
                probe += 1 
                
            # 如果有成功定位到interval bound , 就要開始對內部範圍繼續搜尋  , 若否,代表這個字可以單獨一part 
            
            if interval[1] is None :  
                partition.append(1)  
                start += 1 
                continue 
            
            # 要開始使用被初始定位包裹住的字元進行interval的擴張
            probe = start + 1 

            # 從這邊開始就是不斷更新interval[1] , 因為interval[1]會隨著擴張過程改變,這邊用while
            while probe < interval[1]: 
                
                char = s[probe] 

                # 特別注意 , 這裡的擴張只需要檢查超出interval[1]的範圍的數值
                s2 = interval[1] + 1 
                
                while s2 < len(s):  
                    
                    # 擴張這個part
                    if char == s[s2] : interval[1] = s2 
                    
                    s2 += 1 
                
                probe += 1 
            
            # 到達這邊 , 就是完整的一塊了 
            partition.append(  interval[1] - interval[0] + 1   )
            start = interval[1] + 1 
        
        return partition
                    

                    
""" 
    解法二.
        Hashmap to track every letter  first & last appearence . 
        and perform the interval merge 
        
        TC:O(N) , MC:O(N) (實際上為O(26))
"""
from typing import List 

class Solution:
    
    def partitionLabels(self, s: str) -> List[int]:
        
        hashMap = dict() 
        
        for idx , char in enumerate(s) : 
            if char in hashMap : 
                hashMap[char][1] = idx 
            else : 
                hashMap[char] = [idx,idx] 
        
        # perform interval merge
        intervals = sorted(  hashMap.values()  , key = lambda i : i[0] ) 
        solution = [] 
        temp = intervals[0]
        for (start , end) in intervals :
            
            if temp[1] < start : 
                solution.append( temp[1] - temp[0] + 1   )
                temp = [start , end]
            
            elif temp[1] < end :  
                temp[1] = end   
            
        solution.append(temp[1]-temp[0] + 1)
        
        return solution
                
                
S = Solution() 
print(S.partitionLabels("ababcbacadefegdehijhklij"))
print(S.partitionLabels("eccbbbbdec"))
                    
    
            
            
            
            
            
        
        
