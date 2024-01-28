""" 
    思路 :  
        這一題給定一個沒有cycle的graph , 要求我們找到所有可以從節點0到節點n-1的路徑 
        看起來就是典型的Graph traverse的題目 , 但不是只是要找到是否存在或著一條最短路徑 , 而是要返回所有路徑
        用DFS的架構來解 , 這一題沒有cycle ,可以不用visited  array , 就直接做展開這樣

"""


from typing import List 
class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        
        solution = [] 
        # 往下展開路徑 , 並持續紀錄走到的節點 -> 遇到終點後將這條路徑記錄下來 
        def traverse(node , path:list ): 

            path.append(node)
            
            # 我們先加入節點到路徑 , 再來判斷該節點是否是終點 
            if node == len(graph) -1 : solution.append(list(path))
            for neighbor in graph[node] : 
                traverse(neighbor , path) 
            path.pop()                 
        
        traverse( 0 ,  [])

        return solution