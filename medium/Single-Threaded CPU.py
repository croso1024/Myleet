from typing import List 

""" 
    題意:
        這一題也很有趣 , 設置 , 給定一個任務array : task , task[i] = [enqueueTime_i , processingTime_i] ,  
        假設CPU在切換執行的任務只要瞬間 , 同時一個任務進入CPU後並不會被打斷地直到完成任務 
        接下來follow以下規則
        - CPU idle的時候如果沒有其他任務 , 就是繼續idle
        - CPU idle時如果有任務可以做 , 他會挑選processing Time 最低的開始做 , 如果有多個processing Time相同 , 會挑index最小的
        - 時間從 t=1 開始計算
        這題要求的就是CPU完成任務的順序
    
    思路: 
        這一題要做的事情 ,主要就是做挑選任務 , 同時maintain當前的時間軸 
        細分來說 : 1.選擇哪些任務加入ready queue , 2.選擇任務出來 3. Update時間軸 
        
        拆解完成後,這一題實際上蠻容易去做暴力解 ,針對任務被加入ready queue的時間進行sorting ,就可以讓我們取得正確加入時間的順序 ,
        只是我們還需要將index也加入sorting的一部分 
        
        接著在選擇任務時 , 只要比較priority以及index就可以做任務選擇 , 但也就是這一步 , 暴力解可以使用heap去優化
        
        最後maintain時間軸 , 因為這一題拿到任務就一定會做完 , 算是比較簡單
        
"""

""" 
    解法一. 上述思路 , 
        對tasks加入 index , 接著針對任務加入時間做sorting ( O(NlogN) )
        之後maintain當前時間軸 , 透過pop去做加入任務到ready queue , 每次執行linear search去找到一個適合任務執行 , 並更新時間軸
        這個解法是OK的 , 但瓶頸在於中間"找任務"這件事情是linear search ,卡死了時間 ,
        worse case來說每次while loop都做線性搜索 , 即O(N^2) , 
"""

class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # 將index 也加入tasks
        # 接著對其做Reverse , sorting , 在這個sorting中我們要的只有enqueueTime , list尾巴是最早能加入的
        tasks = [  (enqueue , processing, idx) for idx,(enqueue,processing) in enumerate(tasks)      ] 
        tasks.sort(key = lambda x: x[0]  , reverse=True)
        # 初始時間軸為1
        timeline = 1 
        # ready執行的任務set
        ready = set()   

        sol = []

        # 只要tasks或著ready queue還有任務 , 
        # 迴圈步驟如下 :  1. 根據時間軸 , 把任務從tasks加入ready 2. 從ready選擇任務執行 3.更新時間 
        while tasks or ready : 

            # step1.根據當前時間從tasks加入任務 
            while tasks and tasks[-1][0] <= timeline : 
                ready.add(tasks.pop())
            
            # stpe2. 如果ready queue有任務 , 開始做linear search去找任務 
            # ready裡面的task : (  ( enqueueTime , processingTime  )     , idx   )
            if ready : 
                
                do_task = None

                for task in ready :  
                    if do_task is None : do_task = task 
                    # 如果task的processing time更小 , 或著一樣小但index更小
                    elif task[1] < do_task[1]  or ( task[1] == do_task[1]  and task[2] < do_task[2] ): 
                        do_task = task 

                ready.remove(do_task)                    
                # 拿出do_task的index,以及要執行的時間 
                
                sol.append( do_task[2] )
                timeline += do_task[1]
                
            else :  
                # 這裡time line可以直接換成下一個tasks中的任務enqueue時間
                timeline = tasks[-1][0] if tasks else -1 
                
        return sol 

""" 
    解法二. 將找任務改為maintain heap
        
        也算是原先就想好的解法 , 只是linear search的解法在這一題居然time exceed limit有點出乎意料 , 
        但實際想如果一開始就有一堆任務進入ready , 確實會發生O(N^2)的情況
        
        這邊把linear search還有加入任務改為用heap來執行  , 這樣整體算法為O(NlogN) , 空間則是O(N) 
        
        實際結果來說速度普通 , 空間挺不錯 
"""

from heapq import heappush , heappop

class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # 將index 也加入tasks
        # 接著對其做Reverse , sorting , 在這個sorting中我們要的只有enqueueTime , list尾巴是最早能加入的
        tasks = [  [enqueue , processing, idx] for idx,(enqueue,processing) in enumerate(tasks)      ] 
        tasks.sort(key = lambda x: x[0]  , reverse=True)
        # 初始時間軸為1
        timeline = 1 
        # 將儲存可行任務的container換成priority heap , min heap ,所以自然會以(processing time , idx) 作為排序
        ready = []
        sol = []

        # 只要tasks或著ready queue還有任務 , 
        # 迴圈步驟如下 :  1. 根據時間軸 , 把任務從tasks加入ready 2. 從ready選擇任務執行 3.更新時間 
        while tasks or ready : 

            # step1.根據當前時間從tasks加入任務到heap
            while tasks and tasks[-1][0] <= timeline : 
                
                heappush(  ready , tasks.pop()[1:] )
                
            
            # stpe2. 如果ready heap有任務 , heappop拿出來
            # heap的保存的內容被更改為了(processing , idx)
            if ready : 
                
                task = heappop(ready) 
                sol .append(task[1]) 
                timeline += task[0]                
                
            else :  
                # 這裡time line可以直接換成下一個tasks中的任務enqueue時間
                timeline = tasks[-1][0] if tasks else -1 
                
        return sol 

# tasks = [[1,2],[2,4],[3,2],[4,1]]
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
S = Solution()
print(S.getOrder(tasks=tasks))