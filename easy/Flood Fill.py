""" 
    題意 : 
        給定一個 image List[List[int]] , 為一個 m x n 的matrix,當中元素代表該位置的像素值 
        同時給定sr,sc , color三個值 , 我們要來做 flood fill 
        
        執行flood fill的方式 : 從 image[sr][sc]開始 , 以其4個鄰近像素的方式擴展 , 在檢查鄰近像素的時候 , 如果是相同的值就可以流過去
        並不斷執行這個操作 , 最後將所有可以流到的部份替換成color
        
    思路 : 
        實際上這一題就是要找所有可以用 4-direction 以和image[sr][sc]相同值連接的所有位置 , 最後將他們替換成一個constant結束
        做BFS , DFS都可以 , 我這一題使用DFS來解
"""
from typing import List 

""" 
    解法一. DFS , 這一題不能做直接修改matrix的 , 因為修改成color可能會和原始image[sr][sc]一樣導致不斷迴圈
"""
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        direction = [(-1,0),(1,0),(0,1),(0,-1)] 
        stack = [] 
        m , n = len(image) , len(image[0])
        # store the target pixel value 
        ref = image[sr][sc]
        marker = set()
        # Inplace modify the array 
        stack.append((sr,sc)) 
        marker.add((sr,sc))

        while stack : 
            
            cur_x , cur_y = stack.pop() 
            
            for dir in direction : 
                
                next_x , next_y =  cur_x + dir[0] , cur_y + dir[1]
                
                if not ( 0 <= next_x < m) or not ( 0 <= next_y < n ) : continue 
                
                if image[next_x][next_y] == ref and not (next_x , next_y) in marker :  
                    
                    stack.append( (next_x,next_y) ) 
                    marker.add((next_x , next_y))             
        
        for (mx,my) in marker:  image[mx][my] = color 
            
        
        return image 