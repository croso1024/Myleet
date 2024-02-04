""" 
    題意:
        給定兩個字串 , 在字串中 '#' 表示backspace 刪除鍵
        題目要求兩個字串打在empty text editor上的結果是否相同
    
    思路 :
        最簡單淺顯的作法 , 可以直接兩個stack , 遇到#做pop結束後比較是否一樣就好
        但題目希望我們做到 O(N)時間 O(1)空間
        
        要到O(1)空間,最直覺的想法就是在traverse過程中做比較 , 藉此省去儲存的issue
"""


""" 
    解法一. stack then compare , O(N)時間  , O(N)空間 
    但實際上這個解法的時間空間都很不錯了
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def typing(text): 
            
            stack = list() 
            
            for char in text :  
                
                # stack是有的遇到刪除
                if stack and char == "#" :  
                    stack.pop() 

                # stack是空的 , 但遇到刪除 ->啥都不做
                elif not stack and char == "#" : 
                    continue 
                
                else : 
                    stack.append(char) 
            
            return stack 
        
        return typing(s) == typing(t) 
    
""" 
    解法二. 嘗試去碰題目要的O(1)空間
    
        我的靈感來源在於backspace是從後面開始刪除 ,
        換句話說如果從後面數過來 , 則每個backspace就意味'jump' 
        
        從這個思路下手 , 從後面進行逐一的比對並maintain各自字串的指標即可 
        
        這個解法在速度上一樣很優 , 而空間上 ... 雖然理論上來說是O(1)的解 , 但實際跑得效果並沒有比較好
"""

class Solution:
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        probe1 , probe2 = len(s) -1  , len(t) - 1 

        # counter , 用來計算各自還有幾個 'jump' 
        counter1 = counter2 = 0 
        
        #每一輪 , 先去檢查指標指向什麼而不是急著刪除 , 因為 '##' 代表累積兩個counter
        while probe1 >=0 or probe2 >=0 :
            
            # 先定位到probe1指向有效比較字元
            while probe1 >= 0 : 
                
                if s[probe1] == "#" : 
                    counter1 +=1 
                    probe1 -= 1  
                
                elif s[probe1] != "#" and counter1 > 0 : 
                    counter1 -=1 
                    probe1 -=1 
                
                # s[probe1] != "#" , 並且沒有counter , 代表準備好做比較了
                else : 
                    break  
                
            while probe2 >= 0  : 
                
                if t[probe2] == "#": 
                    counter2 += 1 
                    probe2 -= 1 
                    
                elif t[probe2] != "#" and counter2 > 0 : 
                    counter2 -=1 
                    probe2 -=1  
                
                else : 
                    break 
            
            # 當來到這邊 , 只有可能是probe1 , probe2 都小於0,或著都指向有效比對字
            if probe1 < 0 and probe2 < 0 : return True 
            elif probe1 <0 or probe2 <0 : return False 
            
            elif s[probe1] == t[probe2] : 
                probe1 -= 1 
                probe2 -= 1 
            
            else : return False 
        
        return True 
            
        