"""
    題意 :
    給定一組 CPU 任務 tasks,每個任務用大寫字母 A 到 Z 表示,
    以及一個冷卻時間 n。每個時間單位可以完成一個任務。

    相同任務兩次執行之間,至少要隔 n 個時間單位。
    這中間可以做別的任務,也可以閒置(idle)。
    任務的執行順序可以自己排。

    回傳完成所有任務所需的最少時間單位。

    LeetCode 621 · Medium
    URL : https://leetcode.com/problems/task-scheduler/

    Example :
    tasks = ["A","A","A","B","B","B"], n = 2 -> 8
    一種排法: A -> B -> idle -> A -> B -> idle -> A -> B

    tasks = ["A","C","A","B","D","B"], n = 1 -> 6
    tasks = ["A","A","A","B","B","B"], n = 0 -> 6

    Constraint :
    1 <= tasks.length <= 10^4
    tasks[i] 是大寫英文字母
    0 <= n <= 100

    思路 :
    這一題直覺沒有馬上想到方案,但會想是不是要打散所有任務.
    我的想法是維護一個任務池. 
    這個任務池以"該任務有多少筆為優先度" , 每一回合取出一個任務. 
    做完該任務後,將任務記錄到一個冷卻表.
    同時從冷卻表檢查有沒有可以離開冷卻的任務 , 重新丟回任務Queue.
    

    複雜度 :

    按照我上述的想法 , 第一輪建立Heap 需要先走O(N)蒐集所有任務的數量, 接著 O(ALogA) A為英文字母數的建立Heap.
    以 t=0 開始 ,
    每一回合做一次 Heap pop , 冷卻表寫入. ,檢查離開冷卻 , 重新丟回Heap.
    檢查離開冷卻這件事 , 可以做 HashTable 掃描 , 也可以用一個單獨的Heap去紀錄進入冷卻的回合數,把早於當前回合+n的都拿出來. 
    這一題因為是 Heap , 就選擇用單獨 Heap 去紀錄進入冷卻的回合

    Trade-off :

"""

from typing import List, Dict

from heapq import heappop , heappush 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Record the amount of rest tasks by Letter
        task_heap = [] 

        # Record the latest turn of every task completed. 
        cooldown_heap = [] 

        task_count : Dict[str,int] = {}
        for task in tasks : 
            if task in task_count : task_count[task] += 1  
            else : task_count[task] = 1 
        
        # Insert into heap , Top of heap is most frequent tasks , Use string order as tie-break
        for task in task_count : heappush(task_heap , ( -1 * task_count[task] ,task ) ) 
            
        
        step = 0
        # 只要還有任務就要在清單或冷卻池就要繼續
        while task_heap or cooldown_heap : 

            # 若任務池還有 , 則先從任務池拿一個任務出來解. 
            if task_heap :  
                _, task = heappop(task_heap)  

                # 如果任務做完就做完了,不用進入冷卻池
                if task_count[task] == 1 : 
                    del task_count[task] 
                # 如果任務還有剩,那表示要進入冷卻池
                else :
                    task_count[task] -=1 
                    # 冷卻池的內容是基於冷卻時間,先結束的先出來. 以回合數來計算,則自然在較早回合的會在Heap頂
                    heappush(cooldown_heap , ( step , task ) )  
            
            # 檢查冷卻池,有沒有可以取出的.
            # 取出的標準是當前回合 >= 存入回合 + n  (step=0 存入,n=2 , 則 step2回合結束才能拿 ( step3 才能用 ))
            while cooldown_heap and  step >= cooldown_heap[0][0] + n : 

                _ , task = heappop(cooldown_heap) 
                # 再把任務紀錄回去
                heappush(task_heap ,  ( -1 * task_count[task] , task ) ) 

            # 完成後算做 step + 1 
            step += 1 

        return step 

        


if __name__ == "__main__":
    c = Solution()

    # (輸入參數 tuple, 預期輸出) —— LeetCode 官方範例 + 邊界案例
    test_set = [
        ((["A", "A", "A", "B", "B", "B"], 2), 8),     # 官方範例,中間要閒置
        ((["A", "C", "A", "B", "D", "B"], 1), 6),     # 官方範例,其他任務填滿冷卻
        ((["A", "A", "A", "B", "B", "B"], 0), 6),     # 官方範例,n = 0 不必冷卻
        ((["A"], 100), 1),                            # 邊界:只有一個任務,冷卻用不到
        ((["A", "A", "A"], 2), 7),                    # 只有一種任務: A _ _ A _ _ A
        ((["A", "A", "A", "A"], 3), 13),              # 同一任務拉得很開
        ((["A", "B", "C"], 50), 3),                   # 每種任務只出現一次,不需要閒置
        ((["A", "A", "B", "B"], 1), 4),               # 兩種任務次數相同,剛好交錯
        ((["A", "A", "A", "B", "B", "B", "C"], 2), 8),  # 兩種任務並列最高頻,C 只能填一個空檔
        (
            (["A", "A", "A", "B", "C", "D", "E", "F"], 2),
            8,
        ),                                            # 其他任務夠多,答案等於任務總數
    ]

    for args, expected in test_set:
        result = c.leastInterval(*args)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={args} | expected={expected} | got={result}")
