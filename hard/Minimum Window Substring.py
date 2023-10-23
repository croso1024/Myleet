""" 
    思路: 
        此題的完整思路在javascript版本中,這邊改用python實做
        
        第一個版本是普通板 
        第二個則是優化valid判斷

"""

""" 
    解法一. 判斷valid使用for-loop iterative的去檢查key , amount pair , 另外對於solution是存sub-string而非區間
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 初始化指標, 注意window的區間為左閉右開 [left,right)
        left , right = 0 , 0 
        solution = None 
        # 使用兩個dict來保存windows和target內各字元的次數 
        windows = {}
        target = {} 
        for char in s : windows[char] = 0 
        for char in t : 
            if char in target : target[char] += 1 
            else : target[char] = 1
        
        # 再次注意區間為 [left,right) , 代表left=right=0的時候windows是空的
        while right < len(s)  : 
            
            # 將元素加入視窗  
            windows[s[right]] += 1 
            
            # 判斷當前window內的解是否有效
            valid = True 
            for char , amount in target.items() : 
                if char in windows and windows[char] >= amount : continue
                valid = False 

            # 統一擴增與縮減 , 調整指標範圍都在第三個部份
            right += 1 

            
            # 當目前視窗內的解是可行的 , 開始收縮window
            while valid and ( left <= right ) : 
                
                # 收縮前 , 要先做更新答案 
                if solution :  
                    solution = s[left:right]  if right-left < len(solution) else solution 
                else : solution = s[left:right] # 注意區間 [left , right)
                
                # 其餘步驟與擴大視窗基本是一樣 , 從window去除元素 -> 更新valid -> 調整指標
                windows[s[left]] -= 1  
                
                # 再次判斷windows內的解是否還有效 , 直接看拿出去的值是否有在target內 , 並且拿掉後數量是否足夠
                if (s[left] in target) and (windows[s[left]] < target[s[left]]) : 
                    valid = False 
                
                left += 1 
                
        
        return solution if solution else ""
                
                
            
""" 
    解法二.   優化valid 以及 solution的暫時儲存
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 初始化指標, 注意window的區間為左閉右開 [left,right)
        left , right = 0 , 0 
        solution = None 
        # 使用兩個dict來保存windows和target內各字元的次數 
        windows = {}
        target = {} 
        for char in s : windows[char] = 0 
        for char in t : 
            if char in target : target[char] += 1 
            else : target[char] = 1
        
        # 額外保存一個window_valid , 用來表示window內有效的字元數
        windows_valid = 0 
        
        # 再次注意區間為 [left,right) , 代表left=right=0的時候windows是空的
        while right < len(s)  : 
            
            # 將元素加入視窗  
            windows[s[right]] += 1 
            
            # 判斷當前window內的解是否有效 , 我們使用了一個window_valid來保存window內有效字元的數量
            if ( s[right] in target ) and ( windows[s[right]] <= target[s[right]] ) : 
                windows_valid += 1 
            
            valid = windows_valid == len(t)  

            # 統一擴增與縮減 , 調整指標範圍都在第三個部份
            right += 1 

            
            # 當目前視窗內的解是可行的 , 開始收縮window
            while valid and ( left <= right ) : 
                
                # 收縮前 , 要先做更新答案 
                # 解法二 . 改為保存範圍的指標
                if solution :  
                    solution = (left, right) if  right-left < solution[1]-solution[0] else solution
                else : solution = (left , right) 
                
                # 其餘步驟與擴大視窗基本是一樣 , 從window去除元素 -> 更新valid -> 調整指標
                windows[s[left]] -= 1  
                
                # 再次判斷windows內的解是否還有效 , 需要檢查該值是否是在target內並且window內該字的數量來調整
                # window_valid 
                
                if (s[left] in target) and ( windows[s[left]] < target[s[left]]   ) : 
                    windows_valid -= 1 
                valid = windows_valid == len(t) 
                
                left += 1 
                
        
        return s[solution[0]:solution[1]] if solution else ""
                