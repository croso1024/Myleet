""" 
    題意:
    
        給定一個字串senate , 其中只會包含"R" , "D" ,分別代表兩個陣營 
        接下來開始進行一輪論的投票環節,按照senate string的順序進行投票 , 每一次輪到一個人可以做以下的事情
        - Ban掉一位令一個陣營的人的投票權 , 包含現在已經接下來的輪次,該使用者就不能再做任何事
        - 發起勝利宣言,只有在剩下還能投票的人中都和自己相同陣營時才可以發動, 結束遊戲
        題目要我們從給定senate字串預測最後的贏家 
    
    思路:

        在這個遊戲中, 當前面的人去Ban掉後面的人後,他的回合結束並且重新排到隊伍的最後, 而那個被ban掉的人輪到他的回合時就需要跳過,並且不再加入queue
        如此往復直到整個queue中只剩下一個陣營的人.我們需要實現的部份大概有:
        
        - 找出在queue中下一個與自己陣營不同的人的編號 , 將其加入ban的清單
        - 檢查queue中是否都是剩下同個陣營的. 
        
        我認為可以實現兩個queue各自儲存一個陣營的人,但需要加上編號來保存,用以確保兩個queue的排頭誰先開始
        當兩邊queue都還有存在時,我們先選出某個陣營的, 他的工作就是popleft掉另一個陣營的下個人,接著修改序號重新排自己所屬的queue
        一直走到有一個queue為空   

"""
"""
    解法一. 就是follow我上面的思路,這邊重新編號我原本想說直接+ 10^4 , 但後來想一下只要加原始size就可以了
        整個解法的TC,MC都很不錯
    
"""
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        Rqueue = deque() 
        Dqueue = deque() 
        size = len(senate)
        # step.1 將兩個陣營的人編號放入queue , 因為我們使用陣營去代表queue了,所以實際上只要放編號
        for i in range(len(senate)): 
            
            if senate[i] == "R" : 
                Rqueue.append(i) 
            else : 
                Dqueue.append(i) 
                
        # step.2 follow遊戲規則開始進行,一直玩到有一個queue空了
        while Rqueue and Dqueue : 
            
            # queue編號不會相等 , Rqueue[0] < Dqueue[0] 代表這回合輪到R陣營
            if Rqueue[0] < Dqueue[0] : 
                
                
                Dqueue.popleft()  
                Rqueue.append(Rqueue.popleft() + size)
            
            else : 
                
                Rqueue.popleft()  
                Dqueue.append(Dqueue.popleft() + size)
                
        if Rqueue : return "Radiant"
        else : return "Dire"