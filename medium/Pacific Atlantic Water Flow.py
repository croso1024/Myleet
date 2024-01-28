from typing import List 
""" 
    題意: 
        給定一個 m x n 的島嶼 , 島嶼的上方與左方連接 pacific ocean , 下方與右方則是 atlantic ocean
        在給定的島嶼中 , height[i][j] 代表該格子相對於海平面的高度 .
        這做島嶼上會下雨 , 而落在每一格的水會往上下左右四個方向流去( 當自身高度>=周圍高度 ) 
        並且位在邊界的格子水一定會由到海裡 
        
        題目要求返回所有 "水可以從該格流到pacific ocean與atlantic ocean" 的位置

    思路: 
        水可以流到兩個海洋的格子 , 亦即從該格出發 , 可以到達: 上邊界or左邊界 and 右邊界和下邊界
        最naive的作法是針對每一格去展開DFS或BFS , 去檢查該格是否可以抵達pacific 和 atlantic 
        但這樣的作法是 O( (mn)^2 ) 不太靠普 , 我想應該有O(m*n)的算法 
        
        另外一個我想到的方式 , 是從邊界出發讓水往上爬 , 去計算得到所有從上,左邊界出發可以到達的節點 
        以及所有右,下邊界可以到達的節點 , 這樣時間複雜度變為 O( (m+n)*(mn) )
"""


""" 
    解法一. 從邊界展開DFS , 去找到可以流到pacific的座標以及atlantic座標取交集 
        這個解法的時間複雜度如我上面所分析 , 基本上是O((m+n)*(mn)) , 而空間則是只有O(mn) 
        實際表現來說 , 速度很差 , 但空間很優
"""
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        to_pacific , to_altantic = set() , set() 
        m , n = len(heights) , len(heights[0]) 
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]        
        
        def DFS( i , j  , buffer ) : 
            stack = list() 
            visited = set()

            stack.append((i,j)) 
            visited.add((i,j)) 
            buffer.add((i,j))
            while stack : 
                
                i,j = stack.pop() 
                
                
                
                for dir in direction: 
                    
                    next_i = i + dir[0] 
                    next_j = j + dir[1]
                    
                    if 0<= next_i < m and 0<= next_j < n : 
                        
                        if  not (next_i , next_j) in visited and heights[next_i][next_j] >= heights[i][j] :
                            
                            stack.append((next_i , next_j))
                            visited.add((next_i , next_j)) 
                            buffer.add((next_i , next_j)) 
        
        
        for i in range(m):  
            DFS( i , 0 , to_pacific  ) 
            DFS( i , n-1 , to_altantic) 
        
        for j in range(n):  
            DFS( 0 , j , to_pacific)
            DFS( m-1 , j , to_altantic) 
                                
        # 此時 to_pacific , to_altantic 中的元素就是可以到達他們的 , 現在要取交集
        
        return list(to_altantic.intersection(to_pacific))
                        


""" 
    解法二. 
        再次提高速度的解法來源從to_pacific與to_atlantic set去做過過濾 , 
        如果在traverse的過程中遇到已經存在於 buffer的 , 就可以跳過了 
        相當於直接拿buffer作為visited , 因為在buffer中的都是已經計算過得了
        
        時間與空間都相當優 , 基本上雙O(mn)
"""

class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        to_pacific , to_altantic = set() , set() 
        m , n = len(heights) , len(heights[0]) 
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]        
        
        def DFS( i , j  , buffer : set) : 

            if (i,j) in buffer: return 
            stack = list() 
            visited = set()

            stack.append((i,j)) 
            buffer.add((i,j))
            
            while stack : 
                
                i,j = stack.pop() 
                
                
                for dir in direction: 
                    
                    next_i = i + dir[0] 
                    next_j = j + dir[1]
                    
                    if 0<= next_i < m and 0<= next_j < n : 
                        
                        if  not (next_i , next_j) in buffer and heights[next_i][next_j] >= heights[i][j] :
                            
                            stack.append((next_i , next_j))
                            buffer.add((next_i , next_j)) 
        
        
        for i in range(m):  
            DFS( i , 0 , to_pacific  ) 
            DFS( i , n-1 , to_altantic) 
        
        for j in range(n):  
            DFS( 0 , j , to_pacific)
            DFS( m-1 , j , to_altantic) 
                                
        # 此時 to_pacific , to_altantic 中的元素就是可以到達他們的 , 現在要取交集
        
        return list(to_altantic.intersection(to_pacific))


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

S =  Solution()
print(S.pacificAtlantic(heights=heights))