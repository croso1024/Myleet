""" 
    題意:   
        分別給定兩個array:  server , tasks , 
        server[i]代表了第i台server的優先度 , 越低越高 , 當兩個server優先度相同時 , 則以index小的為優先
        tasks[i]代表第i個任務需要的耗費時間 , 並且第i個任務會在第i秒才可用
        題目要我們返回一個array sol , sol[i]代表task[i]是被分配在哪一台server上
        
    思路: 
        這一題蠻直觀可以想到使用heap , 但問題出在有哪些東西要被model成heap .
        我們在最初直接嘗試把所有東西都model起來.
        1.可用server : 一個min-heap , (priority , index) 來排序 
        2.正在被執行的server : 一個min-heap  (complete_time , index) , 紀錄該任務的完成時間 , 以便在時間對應到時取回任務
        3.尚未被執行的任務 : 這邊我認為就直接延續使用題目給的list , 利用指標來控制就好(因為任務必須照順序分配)

        所以總結來說 , 初始化上面幾個部份,同時使用一個variable去存當前的時間,隨著時間推進 ,
        step.1 看哪些任務可以被使用 , 以及把執行完成的server加回可用server -> O(log server數)  
        step.2 確認要使用哪個server去執行任務 , 把其從可用server移動到執行中的server , 在sol做紀錄 -> O(log server數)
        

"""

""" 
    解法一. 
        將上述演算法思路標標準準的實現,可以順利過測資 ,但在實際sumbit的時候發現,
        當running_server下一個要完成的任務時間與當前times相差巨大的時候 , 會導致while不斷在loop對times++
        而這會使得time limit exceeded . 在下一個解中修正這個問題
"""
from typing import List 
from heapq import heappop , heappush 
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        availble_server = [] 
        running_server = [] 
        
        # use times to bound the availble tasks 
        times = 0 
        next_task = 0
        
        sol = [None for i in range(len(tasks))]
        
        # put all server to availble queue
        for i in range(len(servers)):  heappush( availble_server ,  ( servers[i] , i  ) )
            
        while next_task < len(tasks) : 
            
            # check the running server 
            while running_server and times >= running_server[0][0]  : 
                server = heappop(running_server)[1]
                priority = servers[server] 
                heappush( availble_server , (priority , server ) )
            
            # 當還有可用的server , 同時不能先使用將來的任務 , 並且還沒爆index
            while availble_server and next_task <= times and next_task < len(tasks) : 
                
                task = tasks[next_task] 
                use_server = heappop(availble_server)[1]  
                heappush( running_server  , ( times + task  , use_server ) ) 
                sol[next_task] = use_server
                next_task += 1 
            
            times += 1 
                
                
        return sol 
    
S = Solution() 
print(S.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))
print(S.assignTasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]))


""" 
    解法二.
        為了解決前面所說任務時間太長導致times++要跑非常多次loop這件事 .
        直接在running_server那邊去修改時間 , 增加一行程式碼,使得當沒有任何server可用時,直接跳到下一台server完成的情況
        
        速度還不錯 , 空間則是很優 , 只使用O(Server數)的空間 (running + available)
"""

from heapq import heappop , heappush 
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        availble_server = [] 
        running_server = [] 
        
        # use times to bound the availble tasks 
        times = 0 
        next_task = 0
        
        sol = [None for i in range(len(tasks))]
        
        # put all server to availble queue
        for i in range(len(servers)):  heappush( availble_server ,  ( servers[i] , i  ) )
            
        while next_task < len(tasks) : 
            
            # 加入這一條,用來提昇速度
            if not availble_server : times = running_server[0][0]
            
            # check the running server 
            while running_server and times >= running_server[0][0]  : 
                server = heappop(running_server)[1]
                priority = servers[server] 
                heappush( availble_server , (priority , server ) )
            
            # 當還有可用的server , 同時不能先使用將來的任務 , 並且還沒爆index
            while availble_server and next_task <= times and next_task < len(tasks) : 
                
                task = tasks[next_task] 
                use_server = heappop(availble_server)[1]  
                heappush( running_server  , ( times + task  , use_server ) ) 
                sol[next_task] = use_server
                next_task += 1 
            
            times += 1 
                
                
        return sol 
    