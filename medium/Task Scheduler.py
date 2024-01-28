from typing import List 

""" 
    思路:  
        這一題給定一個Tasks array , 裡面有著多個不同的Char代表不同的任務單元 , 
        並且給定一個數值n代表"執行完特定任務後至少需要等待多久才能再執行這個任務" (而不是連續執行這個任務要等待的時間) 
        
        因此題目要找的就是至少需要多少個時間單元可以執行完所有任務
        ex. [A,A,A,B,B,B] n = 2  則最佳seq = A -> B -> idle -> A -> B -> idle -> A -> B (不能ABA , 因為至少要idle兩格才能再做A)
        
        我第一個想到的方法是維持一個 "冷卻任務" 計時器 , 把做過得任務丟進去, 每一輪則是從未完成與未冷卻的任務中選一個出來做 
        每做完一個任務就將計時器所有值-1 , 直到0代表可以回到等待執行
        
        上面的版本只考慮了做完任務，但不一定能得到最佳，我實做的感受上是"優先執行剩下最多的那個任務"才會有最佳解
        
        
"""


""" 
    解法一. 每一輪都選擇一個可以做的動作來執行 , 
           但這個作法無法到達最佳解 ,要到最佳解, 我們要優先從剩下較多的任務開始做 , 並且take O(N^2)
"""
class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cooldown = dict() 
        rest = dict() 
        
        for task in  tasks : 
            if task in rest : rest[task] += 1 
            else : rest[task] = 1  
        
        time = 0 
        # 每一輪從可以做的任務中選一個出來
        seq = ""
        while rest : 
            
            time += 1 
            choose_task = "<Idle>"
            for task in list(rest.keys()): 
                
                if task in cooldown : continue
                
                choose_task = task 
                                
                rest[task] -= 1  
                
                if rest[task] == 0 : rest.pop(task)    
                # 這邊 n+1 只是因為待會要全部減一
                else : cooldown[task] = n + 1 
                
                # 執行到這邊就可以跳出 , 因為一輪只能做一個任務
                break
            
            seq += choose_task
            
            # 經過一個時間單位
            for task in list(cooldown.keys()) : 
                cooldown[task] -= 1 
                if cooldown[task] == 0 :  cooldown.pop(task)
        
        print(seq)        
        
        return  time 
                                    
                
""" 
    解法二. 修改解法一 我們在"選擇"要做的動作時去選剩下最多的任務  
        
        這邊的"選擇" , 我使用linear search , 基本上這個演算法是Take O(N^2)的暴力解 ,但因為任務的數量只有大寫英文字母,
        因此rest , cooldown dict的最大長度都是26 ,外層while迴圈跑Task總量N , 內層for loop只要跑26的長度 所以這個解法能AC ,
        但時間空間都很差 
"""

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cooldown = dict() 
        rest = dict() 
        
        for task in  tasks : 
            if task in rest : rest[task] += 1 
            else : rest[task] = 1  
        
        time = 0 
        # 每一輪從可以做的任務中選一個出來
        while rest : 
            
            time += 1 
            # 為了要找出"剩下最多的任務,這邊要走整個loop"
            choose_task = None 
            most_amount = float("-inf")
            for task in list(rest.keys()): 
                
                if not task in cooldown and rest[task] > most_amount : 
                    most_amount = rest[task]
                    choose_task = task 

            if not choose_task is None:
                rest[choose_task] -= 1  
            
                if rest[choose_task] == 0 : rest.pop(choose_task)    
                # 這邊 n+1 只是因為待會要全部減一
                else : cooldown[choose_task] = n + 1 
                
            # 經過一個時間單位
            for task in list(cooldown.keys()) : 
                cooldown[task] -= 1 
                if cooldown[task] == 0 :  cooldown.pop(task)
        
        
        return  time 

                
""" 
    解法三. 
    
        這一題內迴圈的速度bottleneck在選擇任務與更新冷卻表上 , 優化得當應該可以到O(N)複雜度
        
        我的想法是用heap , 依照該任務剩下的數量來做優先序 ,當一個任務被執行完成後,我就將他丟掉一個Queue (長度等於n) 
        每個時間單位Queue會走一格 , 走出來的任務就可以加回heap 
        
        這個解法在速度上有明顯提昇 , 比解法二快上3倍 , 但insert進heap本身還是O(logN)的操作
"""

class unit_task : 
    
    def __init__(self,name,amount):
        self.name = name 
        self.amount =  amount 
    def __eq__(self,other):
        return self.amount == other.amount 
    def __gt__(self,other):
        return self.amount > other.amount 
    def __lt__(self,other):
        return self.amount < other.amount 
    
from heapq import heappush , heappop 
from collections import deque 

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # 一樣還是要計算每個任務各自剩下多少 : 並且放進queue 
        Rest = dict() 
        for task in tasks : 
            if task in Rest : Rest[task] += 1 
            else : Rest[task] = 1 
        
        # 接下來要將這些任務全部放進Queue , 以任務數量最多的在最上，注意我們乘上一個-1,使得剩下最多的在heap頂
        heap = [] 
        for task in Rest : 
            unit = unit_task(name = task , amount= -1 * Rest[task]) 
            heappush(heap , unit) 
        
        # 接著初始化一個queue , 長度與等待時間相同 , 當任務被放進queue後就要經過 n 次的單位時間才會出來
        queue = deque([None for i in range(n)])

        time = 0         
        # 只要還有任務沒有做完就繼續
        while Rest : 
            time += 1 
            # 實際步驟:
            # ---如果 heap有值 
            # 1.從heap拿出任務 , 更新Rest
            # 2.如果該任務還有剩下的 , 新增一個unit_task加入queue , 否則queue加入一個None
            # 3.從queue取出排在最前的 , 如果不是None就加入heap
            # ---如果 heap 為空 
            # 1.heap為空代表這一回合idle , 從queue取出排在最前的,不是None就加入heap
             
            # 如果heap有值 , 代表這回合是有任務可以做的
            if heap : 
                
                # 從heap拿出要做的任務 , 修改Rest , 並依據結果 , 如果該任務還沒全部完成 ,就加入queue排隊 , 如果完成了這回合queue就加None
                next_task = heappop(heap) 
                Rest[next_task.name] -= 1 
                
                # 這邊修改次數要注意一下 , 我們前面在放入heap時 ,amount的時候是乘以-1的,這邊要轉回來
                next_task.amount = (-1*next_task.amount) - 1 
                
                
                if Rest[next_task.name] == 0 : 
                    Rest.pop(next_task.name) 
                    queue.append(None) 
                else :  
                    queue.append( unit_task(name=next_task.name , amount= -1*next_task.amount )     )
                
                # 接著更新完成冷卻 , 可以重新加回來的任務 , 從queue拿出排在最前的 , 如果是個任務就加回heap
                new_task = queue.popleft() 
                if not new_task is None : heappush(heap , new_task) 
            
            else : 
                
                queue.append(None) 
                new_task = queue.popleft() 
                if not new_task is None : heappush(heap , new_task)   
        
        return time 
            
            
                    
            