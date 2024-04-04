""" 
    題意:
        給定一個graph , 包含city 1 -> city n , 要找在city1->n路徑上的最小score(distance) , 
        但這題比較奇妙的點在於他可以接受走回頭路 , 假設 1->2的score最小 , 但實際上1->4直接相連時
        答案也會是 1->2->1->4 , 題目已經給定至少有一條path會到達city n , 所以在我看來這一題就是
        找出從city1可以到達的所有城市中的最小distance 

    思路: 

        由於題目已經告知了可能有些節點並沒有與city 1 連接在一起,使得我不能直接拿距離矩陣內的distance找最小
        這種連通性的題目 , 看起來是可以做Union find , 但如果用union find然後將edge一條條加入來建立連通,
        我們可能無法判斷在加入的過程中目前這條edge所連接的接點將來會不會與city 1連接,因此可能在更新最佳解會有點麻煩
        這邊我認為直接走最簡單的DFS/BFS就好, 反正題目已知必定有path走到city n , 那就用個visited set從city1開始擴張
        走到city n也不要停下的擴張完成,取最小edge value
        
        --------
        DFS解法速度不錯,但空間有些差 , 後來想想給其實union find只要做兩次就可以解決我上面所說的,不確定當前edge連通節點是否通到0的問題
        第一次做完union find就可以有所有節點的連接資訊,第二次只要專住在確認是否該edge有連在那塊上
        


"""
from typing import List 

""" 
    DFS implement ,速度不錯但空間很差
"""
class Solution:
    
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = dict() 
        # step1. build the graphh ( given no any repeat edges )
        for (src,dst, distance) in roads : 
            if src in graph: graph[src].update({dst:distance}) 
            else :graph[src] = {dst:distance}
            if dst in graph : graph[dst].update({src:distance})
            else : graph[dst] = {src:distance}
        
        # DFS 
        stack = [] 
        stack.append(1) 
        visited = set() 
        visited.add(1)
        solution = float("inf")
        while stack: 
        
            node = stack.pop()                     
            
            for (neighbor,distance) in graph[node].items(): 
                solution = min(solution , distance)
                if not neighbor in visited : 
                    visited.add(neighbor)
                    stack.append(neighbor)
                    
        return solution                      
