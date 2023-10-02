from typing import List 

""" 
    思路: 
        這一題也是書本上在回溯算法的示範題目 , 在一個NxN的棋盤上擺放N個皇后 , 讓這N個皇后彼此無法攻擊到對方 
        皇后的攻擊範圍: 其所在的整個列&行 , 以及左上,左下,右上,右下的整條 
        
        透過回溯算法的暴力列舉 , 在每一列去選擇某一行來放置queen , 然後往下展開 
        在展開的過程中要去檢查每個位置是否可以放置皇后 , 在那些可以放置的位置繼續展開 , 一路展開到最下層都能放皇后後代表這是一個可行解
"""

""" 
    解法一. 我閱讀完東哥的思路後自己手刻
"""

class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.n = n 
        self.solution = list() 
        
        
        # 就是在回溯的過程中累積的軌跡以及還可以做的動作
        # 我把Action定義為一個 bool list , True表示還可以放置的column (沒被選過的column) , 至於要放新的queen時 ,
        # 他前一列的queen會不會砍到他就用另外一個函數來檢查

        def backtrack( actions ,  track ): 
            
            # 中止條件 , 所有的行都為False,不能再放queen代表結束,就把累積到目前的track重新copy一份放入solution list
            if not any(actions) :
                self.solution.append( list(track) )
                
            for idx,action in enumerate(actions) : 

                # 如果action為True代表該行還沒有放過queen , 是"可能能放"的位置 
                # 透過validAction來進一步過濾 , 確保該索引位置能放置queen
                if action and validAction(idx , track) : 
                    
                    # 對於合法的動作 , 新增進入track , 並在actions中對應位置改為false
                    act = list("."*n) 
                    act[idx] = "Q"  
                    act = "".join(act) 

                    actions[idx] = False
                    track.append(  act  )
                    backtrack( actions , track )

                    actions[idx] = True
                    track.pop()    
                
                # 如果沒有action無法執行就跳過 , 頂多就是全部跳過 , 這個分支不再展開 
                else : 
                    continue
            
            return 
            
        
        # 定義另外一個函數,用來檢查某個action(放在某一行) 是否在該track下合法 
        def validAction(action_idx,track:List[List[str]]) : 
            
            # 如果track是空的 , 那麼所有的行都可以放置Queen 
            if not track : 
                return  True 
            
            # 如果track不是空的 , 那麼就要檢查一下我們想放的位置是否合法
            # 我們要檢查當下的action是否在左上或右上整排是否有其他queen , 正下方的可能性在外面actions就已經排除 

            # 由前一列往更上方堆進, 把track反轉過來 
            for idx , row in  enumerate(track[::-1]) :  
                # 拿出該row中queen的位置索引
                queen_pos = row.index("Q")  
                # 該索引和我們想要放的action_idx , 其abs差距(columns數差距)不能等於row數的差異
                # ex. 前一列在3有queen , 那我們2,4都不能放   , 前兩列在5有queen , 那我們3,7不能放
                if  abs(action_idx - queen_pos) == (idx+1) : return False 
            
            # 都走完 , 確認了我們想放的位置左上右上都ok, 就可以放了
            return True 
            
    
        backtrack([True] * self.n , [])
        return self.solution

S = Solution() 
print(S.solveNQueens(n=4))