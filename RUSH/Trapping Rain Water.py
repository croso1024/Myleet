from typing import List 


# 核心思路是 , 每一格能夠裝的水與周圍兩側的block有關, 若是兩側都至少存在比自己目前這格還要高的牆 , 那裝水量為 min(left_max,right_max) - cur 
# 依照這個想法,使用prefix就能O(N)得到解, total time compleixty是O(N) , space是O(N)

class Solution:

    def trap(self, height: List[int]) -> int:
        
        left_prefix = [None for i in range(len(height))]
        right_prefix = [None for i in range(len(height))] 
        
        # 填充left prefix , 對於第0格就直接放成None
        left_acc = height[0] 
        for i in range(1 , len(height)): 
            left_prefix[i] = left_acc
            left_acc = max(left_acc , height[i]) 
        
        # 填充right_prefix , 同理在最後一個放None 
        right_acc = height[len(height)-1]
        for i in range(len(height) - 2 , -1 , -1 ): 
            right_prefix[i] = right_acc 
            right_acc = max(right_acc , height[i]) 
        
        total_water = 0 
        # 最後只要走一次O(N)就可以計算裝雨量 ,要扣掉最兩側無法裝
        for i in range(1 , len(height)-1): 
            
            neighbor_height = min(left_prefix[i] , right_prefix[i])
            
            if neighbor_height > height[i] : 
                
                total_water += neighbor_height - height[i] 

        return total_water

S = Solution()
print(S.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))