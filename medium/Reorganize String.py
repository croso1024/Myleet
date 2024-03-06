""" 
    題意:
        給定一個string s , 要求我們重新排列這個string,
        使新的string不會出現連續兩個一樣的字母
    
    思路:
        這一題有點greedy的味道 , 我們總是選擇剩餘最多的字母加入,然後選擇第二多的字母再插入(確保不會有一樣的出現)
        如果能順利插完就有解,否則無解
        
        考慮到要快速取出最多和第二多的字母,需要用一個heap來做這件事
        我們用dict去統計每個字母的出現次數,建立一個heap , 接著就是greedy的插入字母
"""


""" 
    解法一. Follow 上述思路, 基本上就是一次要取出,更新解,放回 兩組item , 多寫一個條件去處理只拿到一個item的情況而已
    速度和空間都很優 , 空間的部份因為要建立heap : O(nlogn) , 後續操作插入值, 因為要插入n次 ,也是nlogn , 空間的話則是O(26)
    實際上這邊的n也是26
    
"""
from heapq import heappop , heappush 
class Solution:
    
    def reorganizeString(self, s: str) -> str:
        
        hashmap = dict() 
        for char in s : 
            if char in hashmap : hashmap[char] += 1 
            else : hashmap[char] = 1 

        heap = [] 
        sol = ""
        
        for (char , freq ) in hashmap.items() : 
            
            # cause we want get a Max-heap 
            item = (-1 * freq ,  char)  
            heappush(heap , item) 
        
        # once we establish the heap , we can perform the greedy algorithms to insert char to solution string 
        
        # 每次的插入字母都是成對的 , 拿出剩餘前兩多的字
        while heap : 
            
            first = heappop(heap) 
            
            # 如果沒有第二個item了,且出現最多的這個item還有1個以上就False
            if not heap : 
                
                if abs(first[0]) > 1 : return ""
                else : 
                    sol += first[1]
                    return sol 
            
            second = heappop(heap) 
            
            sol += first[1] 
            sol += second[1] 
            
            if not first[0] == -1 :  heappush( heap ,(  first[0] + 1   , first[1]   )  )
            if not second[0] == -1 :  heappush(heap , (  second[0] + 1   , second[1]   )  )

        # 待表所有字母都被插入完
        
        return sol
            