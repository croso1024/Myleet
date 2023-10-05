from typing import List 

""" 
    思路 : 
        這一題看似上去就是需要Backtrack來暴力列舉 , ( 從題目最多只解到n=20也可以看出端倪 )
        
        使用回溯框架 , 動作清單使用剩下來能挑的數字 , 軌跡比較單純的就是紀錄 , 
        這題比較tricky的部份在於我們要如何剪枝 , 才能使得不會有重複的組合(不考慮順序)被加入解
"""

""" 
    原始寫法 , 會產生有重複但順序不同的解 , 因為我們爆搜了整個決策樹展開 
    例如產生[1,2] , 同時也有[2,1] 
"""
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = list() 
        
        # 題目已經指定了k的大小 , 因此我們直接使用track的長度等於k來判斷end case 
        def backtrack(actions , track : List ): 
            nonlocal result
            # end-case , 
            if len(track) == k :                 
                result.append(list(track))
                return   
            
            # 回溯框架 - 選擇清單中挑選動作 
            for idx , action in enumerate(actions) : 

                # 做選擇 -> 傳入新的可用動作 --> 撤銷選擇
                track.append(action) 
                backtrack( actions[:idx] + actions[idx+1:] , track )  
                track.pop() 
        
        backtrack([i for i in range(1,n+1)]  , [] ) 
        
        return result 

""" 
    解法二. 
        這題的關鍵在於如何適當的剪枝 , 使得tree不會有重複的軌跡出現 , 最終這一棵樹應該會長成:
        ex. n=3 ( [1,2,3] ) , k=2 , 
        最左邊的樹可以使用到1作為動作 , 剩餘[2,3]繼續展開 , 
        而中間的樹則應該只用[2,3]開始展開 , 因為有選過1的都已經在第一棵樹的分支底下了 
        
        所以解法二修改了傳入backtrack的動作清單 , 只保留" 先前都沒往下展開過的分支 " ,
        
        另外end-case應該還會有actions為空的情況 , 但因為我們寫了for .. (actions) , 
        因此也不用特地寫action為空的判斷來return

"""

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = list() 
        
        # 題目已經指定了k的大小 , 因此我們直接使用track的長度等於k來判斷end case 
        def backtrack(actions , track : List ): 
            nonlocal result
            # end-case , 
            if len(track) == k :                 
                result.append(list(track))
                return   
            
            # 回溯框架 - 選擇清單中挑選動作 
            for idx , action in enumerate(actions) : 

                # 做選擇 -> 傳入新的可用動作 --> 撤銷選擇
                track.append(action) 
                backtrack( actions[idx+1:] , track )  
                track.pop() 
        
        backtrack([i for i in range(1,n+1)]  , [] ) 
        
        return result 
