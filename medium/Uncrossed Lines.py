""" 
    題意:
    
        給定兩個整數數列nums1, nums2 並且依照給定的order , 現在我們要將兩個數列兩兩劃線連接起來,
        ex. nums1=[1,4,2] , nums2 = [1,2,4] :
        1 4 2  
        1 2 4 
        這個情況下1,1可以相連 , 4,4也可以相連 .
        我們劃線的條件是: 不能有任何線段相交 , 並且一個數字只能被一條線配對到 , 題目問我們最多可以畫出幾條線 
        
        2 , 5 , 1 , 2 , 5
        
        10, 5 , 2 , 1 , 5 , 2
        
    思路:

        這一題蠻直觀來說是DP題, 如果我們的2個陣列各只有一個數值 , 只需要看兩個數字是否相同即可 . 
        而這一題所謂的劃線無法交叉,我的理解是我們必須track目前兩邊最靠右邊有參與劃線的index , 新的線兩端index都必須大於他們
        
        這邊我想到一個Top down的解法 , 但不確定是否會爆complexity , 
        於每一個state下我們都能做以下兩個選擇 , 
        -1. 從nums1盡量靠左選一個數字 , 將其連接到最靠左的nums2數字 , 更新index傳遞下去, 
        -2. 從nums2盡量靠左選一個數字 , 將其連接到最靠左的nums1數字 , 更新index傳遞下去
        
        --------------------------
        這一題的狀態轉移看似複雜 , 實際上很直接.
        令dp[i][j]代表nums1[0:i]和nums2[0:j]範圍內的最大連接數 .
        
        dp[i][j] = 1 + dp[i-1][j-1] , 如果 nums1[i] == nums2[j] ,否則 = max(dp[i-1][j] , dp[i][j-1])
        即若i,j對應的數字不一樣 , 則就看 nums1[0:i]和nums2[0:j-1] 與 nums1[0:i-1]和nums2[0:j]誰大
        
"""

""" 
    解法一. 
        使用Top-down + memo , 但是會爆時間, 這題就算稍微優化 , memo + DFS可能仍然不是好方法
"""

from typing import List 
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        size1 , size2 = len(nums1) , len(nums2)
        sol = 0
        table = set()
        
        def DFS(nums1_index , nums2_index , lines) : 
            nonlocal sol 
            
            sol = max(sol , lines) 
            # if nums1_index < size1 : 
            jump1 = False 
            jump2 = False 
            for i in range(nums1_index , size1):
                for j in range(nums2_index , size2): 
                    if nums1[i] ==  nums2[j] and not (i,j) in table :
                        table.add((i,j))
                        DFS(i+1 , j+1 , lines+1) 
                        table.remove((i,j))
                        jump1 = True 
                        break     
                if jump1 : break 

            
            for i in range(nums2_index , size2): 
                for j in range(nums1_index , size1): 
                    if nums2[i] == nums1[j] and not (j,i) in table : 
                        table.add((j,i))
                        DFS(j+1 , i+1 , lines+1 )
                        table.remove((j,i))
                        jump2 = True 
                        break 
                if jump2 : break 
                        
            return 
        
        DFS(0,0,0) 
        
        return sol             

""" 
    解法二. 第二版本的DFS,只操作一個array,每一步的選擇,找線連接或著不做事 .
        這個版本的效果就很不錯了 , 簡單而且比第一版本高效 , 但仍然會Time limit exceeded
"""
class Solution2:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        size1 = len(nums1)
        size2 = len(nums2) 
        sol = 0 
        
        def DFS(idx1 , idx2 , lines): 
            nonlocal sol 
            
            sol = max(sol , lines) 
            if idx1 == size1 : return 
            
            for j in range(idx2 , size2): 
                
                if nums1[idx1] == nums2[j] : 
                    DFS(idx1+1 , j+1 , lines+1) 
                    break
                
            DFS(idx1+1 , idx2 , lines) 
        
        DFS(0 , 0 , 0)
        
        return sol             


""" 
    第三版本 , bottom-up , 推表格 ,
        這一題的狀態轉移看似複雜 , 實際上很直接.
        令dp[i][j]代表nums1[0:i]和nums2[0:j]範圍內的最大連接數 .
        
        dp[i][j] = 1 + dp[i-1][j-1] , 如果 nums1[i] == nums2[j] ,否則 = max(dp[i-1][j] , dp[i][j-1])
        即若i,j對應的數字不一樣 , 則就看 nums1[0:i]和nums2[0:j-1] 與 nums1[0:i-1]和nums2[0:j]誰大
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        size1 , size2 = len(nums1) , len(nums2)
        
        dp =[ [None for i in range(size2)]  for j in range(size1) ] 

        dp[0][0] = 1 if nums1[0] == nums2[0] else 0 
        # 填充第0列0行
        for i in range(1,size2): 
            dp[0][i] = 1 if dp[0][i-1] == 1  or nums1[0] == nums2[i] else 0
        for i in range(1,size1):
            dp[i][0] = 1 if dp[i-1][0] == 1 or nums2[0] == nums1[i] else 0 
            
        for i in range(1,size1): 
            for j in range(1,size2): 
                
                
                if nums1[i] == nums2[j] : 
                    
                    dp[i][j] = 1 + dp[i-1][j-1] 
                else : 
                    
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1]) 
        
        return dp[size1-1][size2-1]
        
             
# nums1 = [4,2,1,4,2,2,5,1,4,4,1,2,4,2,1,4,1,4,1,5]
# nums2 = [4,3,4,4,3,3,1,1,4,2,3,2,5,1,2]

nums1 = [3,1,2,1,4,1,2,2,5,3,2,1,1,4,5,2,3,2,5,5]
nums2 = [2,4,1,2,3,4,2,4,5,5,1,1,2,1,1,1,5,4,1,4,2,1,5,4,2,3,1,5,2,1]
S = Solution2() 
print(S.maxUncrossedLines(
    nums1=nums1 , nums2=nums2
))