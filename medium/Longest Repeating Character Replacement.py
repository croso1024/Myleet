""" 
    思路 :  

        一開始我一直覺得這一題是DP , 但不容易去思考DP要如何解這題 , 因為還需要maintain k這個數值的變化
        但實際上這一題的分類在Sliding window 
        
        從Sliding window的角度去切入 ,這一題的題目可以轉化為 , 求一個最長的區間 , 
        同時,區間內的元素除了最多的那個字母以外其他的字母出現次數不可超過k 
        
        所以要maintain一個 window , window是一個hash table紀錄每一個字母的出現次數 
        並且還要3個變數去保存 window內最多的Key和對應的次數/window的元素數 , 
        在每次調整範圍的時候調整window 
        
        這樣大體的思路就有了 , 但這一題看來細節也挺複雜的
"""


""" 
    解法一. sliding window 
    
    我們去維護window內最多出現的字元和次數 
    -> 當加入新的字元 , 檢查該字元是否比現有最多的更多 
    -> 當移除字元 , 如果移除的是最多次的字元 , 需要檢查那是否有其他字元次數更多了 (或維護第二多的字元)
    
    我寫了一個helper function去處理這個 , 當移除字元是最多的字元的case , 這也是主要的time compleixty的瓶頸來源
    整體來說這個演算法的worst case是O(N^2) , 空間則是O(1) , 因為字母數量有限
    但實際上來說 時間跟空間表現都不太好
"""


class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:

        # window  , 保存著window內所有字母以及各自的出現次數 
        window = dict()
        # window 內最常出現的字元和對應的出現次數
        repeating_char = None 
        # best solution 
        best = 0 
        
        # 用來判斷window內是否滿足解
        def valid(l,r,window,repeating_char): 
            window_size = r-l
            if window_size - window[repeating_char] <= k : return True 
            else : return False 
            
        # 用來判斷現在window內最多次的單字是誰 O(N)
        def most_freq_inWindow(window:dict): 
            return  max(window.keys() , key= lambda k : window[k] )
            
        
        # 初始化sliding window雙指標 , 指標區間為 [left,right)
        left , right = 0 , 0 
        
        while right < len(s): 
            
            add_element = s[right]
            
            if add_element in window : window[add_element] += 1 
            else : window[add_element] = 1 
            
            if repeating_char is None : 
                repeating_char = add_element 
                
            elif window[add_element] > window[repeating_char] : 
                repeating_char = add_element

            right += 1 
            
            # 如果解目前仍然可行 , 就更新解
            effect = valid(left,right , window , repeating_char)
            
            
            # 如果window內已經不符合解了 , 就要開始砍 
            while left < right and not effect : 
                
                remove_element = s[left] 
                # remove的element一定已經在window中了 
                window[remove_element] -= 1 
                
                # 如果移除的這個元素還剛好是出現最多的 -> 要看他是否仍然是出現最多的 
                # 如果不是出現最多的 , 那最多的那個數值不會變
                if remove_element == repeating_char : 
                    repeating_char = most_freq_inWindow(window) 
                    
                left += 1 
                
                effect = valid(left,right , window , repeating_char)
                
            # 走到這邊一定是effect 
            best = max(best , right-left)
        
        return best 


""" 
    解法二. 
        微調了當縮小視窗的過程中遇到repeating_char的處理 , 如果repeating char還小於當前window size的一半才要跳下去解
        否則也不用下去跑O(N) 
        
        空間時間有略微的提昇
"""
class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:

        # window  , 保存著window內所有字母以及各自的出現次數 
        window = dict()
        # window 內最常出現的字元和對應的出現次數
        repeating_char = None 
        # best solution 
        best = 0 
        
        # 用來判斷window內是否滿足解
        def valid(l,r,window,repeating_char): 
            window_size = r-l
            if window_size - window[repeating_char] <= k : return True 
            else : return False 
            
        # 用來判斷現在window內最多次的單字是誰 O(N)
        def most_freq_inWindow(window:dict): 
            return  max(window.keys() , key= lambda k : window[k] )
            
        
        # 初始化sliding window雙指標 , 指標區間為 [left,right)
        left , right = 0 , 0 
        
        while right < len(s): 
            
            add_element = s[right]
            
            if add_element in window : window[add_element] += 1 
            else : window[add_element] = 1 
            
            if repeating_char is None : 
                repeating_char = add_element 
                
            elif window[add_element] > window[repeating_char] : 
                repeating_char = add_element

            right += 1 
            
            # 如果解目前仍然可行 , 就更新解
            effect = valid(left,right , window , repeating_char)
            
            
            # 如果window內已經不符合解了 , 就要開始砍 
            while left < right and not effect : 
                
                remove_element = s[left] 
                # remove的element一定已經在window中了 
                window[remove_element] -= 1 
                
                # 如果移除的這個元素還剛好是出現最多的 -> 要看他是否仍然是出現最多的 
                # 如果不是出現最多的 , 那最多的那個數值不會變
                if remove_element == repeating_char and window[repeating_char] < (right-left)/2 : 
                    repeating_char = most_freq_inWindow(window) 
                    
                left += 1 
                
                effect = valid(left,right , window , repeating_char)
                
            # 走到這邊一定是effect 
            best = max(best , right-left)
        
        return best 
    
