from typing  import List 

""" 
    思路: 
        給定array: people , people[i]代表每個人的重量 , 以及常數limit 代表一艘船的最大載重 ,
        假設我們一次最多能載兩個人 , 求最少需要幾艘船才能運送所有人 , 已知limit>=people[i] , 確保一定能送完
        
        這一題有點類似koko eating banana , 差別在於這題有說我們一次最多能載兩個人 ,
        
        如果要"驗證"我們選的船數夠不夠載運 , 我的想法是左右雙指標 , 一左一右的去填充船的人數 , 這要take O(N) 
        假設用Binary search去切分我們需要的船數 (最多需要 len(people) 艘 ) , 則需要切 O(LogN) 次數
        
        因此上面的algorithms要花O(NLogN) , 唯一的疑慮是雙指標戰術能夠確實地確認是否載運的完 , 
        另外要實現這套戰術需要先sort people  , 因此也要O(NlogN)
"""


""" 
    解法一. 
        依照上述思路 , 拆分整個algorithms為兩個部份 "驗證" 與 "binary search for left bound" 
        去找到最少的船需求 
        
        速度極差 , 空間也不佳 , 我猜這個問題應該有O(N)的algorithms
"""
class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # 驗證使用給定的船數量到底能不能運送完
        def valid(amount): 
            
            left , right = 0 , len(people) - 1 
            # 剩餘的船數量
            rest = amount 
            
            # 一次最多載兩個人 , 如果左右兩個人都上船了就代表必須-1艘船
            while left <= right and rest > 0 : 
                
                # 兩個人搭上去剛好ok , 那就減少一艘船出發了
                if people[left] + people[right] <= limit : 
                    left += 1
                    right -= 1 
                    rest -= 1  
                    
                # 如果沒有辦法一次搭兩個 , 先讓重的搭船 
                else : 
                    right -= 1 
                    rest -= 1 

            # 出了這個while loop , 只有可能是 left > right or rest = 0 
            
            # 如果left > right ,代表所有人都運完了 
            if left > right : return True 
            else : return False 
            
        # 先對people進行sorting , 使得左右雙標能夠順利運行
        people.sort()
    
        # binary search framework for left bound search        
        left, right = 0  , len(people) 
        
        while left <= right : 
            
            mid = ( left + right ) // 2 
            
            # 如果能夠運的完 , 我們就繼續嘗試縮小船的數量
            if valid(mid) :  
                right = mid - 1   
            # 如果運不完 , 只好增加船的數量            
            else : 
                left =  mid + 1  
                
        return left 
        
        

""" 
    解法二. 
        稍微思考一下 , 我在驗證的部份 , 應該就可以作為計算需要幾部車的algorithms , 但仍需要經過sort 
        因此雖然會比第一個算法快 , 但整體複雜度還是O(NlogN) , 這一題就是一個標準雙指標 
        
        這個解法計算速度有明顯提昇, 基本上應該就是Optimal time complexity , 
        但如同上述 , 仍然是O(NlogN) , 至於空間不曉得是怎樣反而退步
"""         

class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort() 
        sol = 0 
        left , right = 0 , len(people) - 1 
        
        while left <= right : 

            if people[left] + people[right] <= limit : 
                left += 1 
                right -= 1
            
            else : 
                right -= 1 
            
            sol += 1 
        
        return sol                 
        
    