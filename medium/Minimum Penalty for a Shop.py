""" 
    題意:   
        給定一個客戶字串 , 只有包含"Y" , "N" , 
        其順序代表是在第幾個小時 , Y代表在該小時有客人來 ,N則沒有客人 ,
        現在要決定關店的時間 , 並且計算penalty的方式為 :
        1. 如果在店家關閉後 , 有客人來, 則penalty+1 ,
        2. 如過店家開門時,沒有客人 , penalty+1 , 
        
        要找出penalty最小的最早關店時間 
    
    思路:
        這一題看起來是prefix , 從左到右去填充各自有多少客人來和沒來,
        就可以計算 , take O(N) time & space

        -> 這個解法速度上O(N)沒問題但偏慢 , 而空間則不是最佳, 
        最好的解法實際上是看其他人的提交 , 因為原本我還在想如果不prefix , 只有順向可以邊走邊算
        但別人的解法在這一題算是蠻妙的
    
"""
class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # forward[i] : how many customer absense before i th hours
        forward = [ 0 for i in range(len(customers))]
        # backward[i] : how many customer come after i th hours 
        backward = [ 0 for i in range(len(customers))]
        
        forward[0] = 1 if customers[0] == "N" else 0  
        backward[-1] = 1 if customers[-1] == "Y" else 0 
        
        for i in range(1 , len(customers)): 
            if customers[i] == "N": forward[i] = 1 + forward[i-1] 
            else : forward[i] = forward[i-1]
        for i in range(len(customers)-2 , -1,-1): 
            if customers[i] == "Y" : backward[i] = 1 + backward[i+1]
            else : backward[i] = backward[i+1]
                
                
        penalty = float('inf')
        sol = 0
        for i in range(len(customers)+1): 
            
            if i == 0 : cur_penalty = backward[i]
            elif i == len(customers) : cur_penalty = forward[i-1]  
            else :
                # 如果在i小時關店 , penalty就是在截止i-1小時所有沒來的 , 加上自從i小時候有來的
                cur_penalty = forward[i-1] + backward[i]

            if cur_penalty < penalty:
                penalty = cur_penalty 
                sol = i 
        return sol 
                
S = Solution()
# print(S.bestClosingTime("YYNY"))         
print(S.bestClosingTime("YNYY"))         
       

""" 
    實際上我們可以把遇到有客人這件事情當作減少penalty, 遇到沒客人才加,
    "而且我們不需要實際的最小penalty值" , 因此我們可以改成maintain讓penality減少最多的關店時間
    這樣我們就可以在一次的順向去計算答案 , 這個想法比較特別一點 , 
    如果前面都是有客人 , 我們實際上就可以一直扣減current-penalty
"""
class Solution:

    def bestClosingTime(self, customers: str) -> int:

        size = len(customers) 
        
        # 一開始出發的penalti是0 , 在第0小時關店, 如果後面有更多客人,那這就會被更新,如果都是沒客人,那這就是最後的解答
        minimum_penalty = 0  
        sol = 0
        cur_penalty = 0 
        for i in range(size): 

            if customers[i] == "Y": 
                cur_penalty -= 1 
            else : 
                cur_penalty += 1 
                
            if cur_penalty < minimum_penalty: 
                # 我們先考慮了第i小時的來客狀況才更新cur_penality , 所以這實際上是第i+1小時的操作
                cur_penalty = minimum_penalty
                sol = i + 1 
        return sol 
        