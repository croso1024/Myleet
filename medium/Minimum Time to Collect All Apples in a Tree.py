""" 
    題意:   
        給定一個undirected tree , 包含 0到n-1編號的節點 , edges array標示這些節點間的連通關係
        以及一個boolean array,代表特定編號的節點是否有apple. 
        題目要求從節點0出發 , 蒐集所有蘋果的最短時間 ( 走一條edge spend 1 second )
        
        注意這些節點的排序方式除了root以外看起來就是亂序,所以實際上可以看成給了一個graph , 從root出發.
        
    思路:
        原先我的直覺想法是可以想像成一個recursion問題 , 我不知道整棵樹拿完所有蘋果需要多久,
        但我知道一棵只有3個節點的樹拿完蘋果要多久 , 利用類似的思路來解 .
        
        稍微去思考一下,我認為就是使用recursion概念 , 只是因為不是普通的tree , 
        我們要使用edge list在這張graph上去施展recursion. 
        同樣將大問題拆為小問題 : 計算以特定節點為root的tree蒐集所有蘋果要多久     
    
        
"""
from typing import List 

""" 
    解法一. 
        follow我的recursion思路 , 將大問題拆解成小問題  , 這一題的特別之處在於他是非典型tree structure 
        使用edge-list來表示 .  
        
        在定義蒐集蘋果所需要的時間的function上 , 我定義為 "蒐集以node為root的子樹需要的時間"
        但實際回傳除了時間以外還要給這顆tree下面是否有apple , 用來給parent判斷是否要往下探
        如果有的話parent必須往下探 , 並且collection_time 要加上2秒
        如果一棵子樹完全往下都沒apple , 則一層層遞迴回到parent時他的collection time也會是0秒
        而如果一顆樹的left_child下面有不只一個apple , 我們在parent這一層也只是left-child的蒐集時間+2秒 ,因為只要下去一次
        
        
        後面在實際測資的時候發現會有一些edge給的讓我graph只建到一半 , 所以在建graph的步驟也建dst->src
        同時加入visited array避免重複尋訪
        
        時間 : O(N) , 空間 : O(N) , 實際表顯時間還不錯 , 空間稍差    
"""
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        
        
        graph = dict()
        # extra-part , avoid jumping into loop in undirected-graph 
        visited = set() 
        visited.add(0)
        # -------------------------------------------------------
        for src , dst in edges: 
            if src in graph: 
                graph[src].append(dst) 
            else : 
                graph[src] = [dst]
        
        # extra-part , avoid jumping into loop in undirected-graph 
            if dst in graph : 
                graph[dst].append(src) 
            else :
                graph[dst] = [src] 
        # -------------------------------------------------------
        
        # 計算以node為root的tree需要多久時間來蒐集蘋果
        def collectApple(node): 
            nonlocal visited
            
            collect_time = 0 
            apple = True if hasApple[node] else False 
            
            if node in graph : 

                for child in graph[node]:
                    
                    if child in visited : continue

                    visited.add(child) 

                    ct , has = collectApple(child) 
                    
                    if has :  
                        collect_time += ( ct + 2 )
                        apple = True 
                        
                    else : collect_time += ct 
            
            else : 
                # 如果這個節點沒有child , 那從這個tree裡面蒐集蘋果只需要0秒
                # 但也要回傳從這個節點開始的蒐集時間
                return collect_time , hasApple[node] 
            
            # 對於有child的tree來說 , 就是回傳這顆子樹下是否有apple , 如果有的話parent必須花2秒下去
            return collect_time , apple
        
        ct , has = collectApple(0) 
        return ct 
        
            
            
            
            
            