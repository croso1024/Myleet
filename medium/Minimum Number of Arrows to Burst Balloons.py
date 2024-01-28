""" 
    思路: 
        給定多個interval , 代表氣球的範圍 , 求最少需要幾槍可以打中所有氣球 , 
        某些氣球的範圍交疊 , 亦即這題需要找出有"幾團" 氣球 
        
        很直接讓我想到的是union-find algorithms, 走訪一次points arr就可以把每個獨立的氣球塊給連接在一起
        但這個走訪實際上不好執行 , 且時間複雜度也難以維持在O(N) ,

        另一個想法是針對interval的第一個值進行sort , 然後開始連接每一塊地,
        這樣基本上是Take O(NlogN) , 就可以算是總共有幾塊連通
        
"""



from typing import List 

""" 
    解法一. 
        針對interval第一個值做sort , 之後連通並計算有幾塊的方法
        原先的思路大致上合理 , 但有個小問題就在於"連通的一整塊無法確保一槍可以全中" , 
        實際上真正一槍能夠全中的連通 , 必須每個interval都有重疊

        速度還行 , 空間稍差
"""
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # 針對interval[i][0] 做sort 
        points.sort(key = lambda point: point[0] ) 
        # print(points)
        # 保存卻切需要開幾槍
        sol = 0 
        
        temp = points[0] 
        
        
        # 因為針對interval做個sort , 可以確保temp[0]必定小於 interval[0] , 不用處理向左邊擴大的邏輯
        for interval in points : 
            
            # 沒有連通到下一個範圍 , 開槍全破當前範圍 , 以下一個interval繼續了
            if temp[1] < interval[0] : 

                sol += 1 
                temp = interval 
                
            # 有連通到下一個範圍  , 處理向右擴大temp !!! -> 不用處理擴大了 , 因為擴大的話無法確保一槍能全中 
            # 反而是要處理縮小 , 因為我們只對第一個值sort , 為了確保一槍要全中 , 我們需要縮小temp右半邊
            else : 
                temp[1] = min(temp[1] , interval[1])
                
        # 連通得最後一塊也要開槍 
        sol += 1 
        
        return sol 
    
test_case = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
S = Solution()
print(S.findMinArrowShots(test_case))