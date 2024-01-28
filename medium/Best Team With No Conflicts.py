""" 
    思路: 
        給定兩組array , scores與ages  , 代表每一個球員的年紀和能力值 ,
        我們的目標是要湊出一支總分數值最高的球隊 (但沒有限制人數) ,    
        但有一個限制 , 即球隊中不能有 "年紀低的人分數值高於年紀大的人" , 如果同年紀就沒差
        要找出在這個限制條件的情況下可以湊出的最高分數球隊
        
        
        看到這一題我的一個直覺可能是讓scores針對ages進行sorted , 
        接下來做1D-DP , 在選擇過程中keep 目前我選入的最高分數 , 而後面的選手(年紀一定大於等於)不能低於這個分數這件事 
        每一個DP回合都是紀錄目前累積的總分數值 , 以及目前選擇的選手最高分數值與年紀
        
        dp表格紀錄 dp[i] = ( 選擇選手i, 從0到i範圍的最高分數 , 不選選手i 從0到i範圍的最高分數 )
        
        我的解法是透過雙loop推進DP  , 內迴圈負責計算 " 如果選了選手i " 的最高分數值 ,
        因為要選擇選手i就不能選擇前面分數高過選手i但年紀又比選手i小的 , 
        

"""

""" 
    解法一. 雙Loop , 在計算選手i時要去回顧前面 0~i-1 範圍的分數值來作為計算
        在我的dp表紀錄了選擇選手i與不選擇選手i的最高分數值
        
        時間偏差 , 空間普通
        
"""
from typing import List 
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        # 第一步,需要針對年紀進行sorted , 透過zip組合後 , 按照tuple排序規則 , 優先排年紀再排分數值
        ref = sorted(zip(ages , scores))

        # ref[i] = (年紀,分數值)
        # create dp table , 
        dp = [   None for i in range(len(ages))   ]
        # base-case 
        dp[0] =( ref[0][1] , 0 )
        for i in range(1 , len(ages)): 
            # 選擇i至少有的分數
            choose_i = ref[i][1]  
            # 改為內迴圈去比較在自己之前的所有值 
            for j in range(i): 
                
                # 如果前面的分數值大於自己 , 年紀又小於自己,就不能納入
                if ref[j][1] > ref[i][1] and  ref[j][0] < ref[i][0] : continue
                # 否則就可以去更新加入自身的最大分數值
                choose_i =  max(choose_i  ,  dp[j][0] + ref[i][1] )
            
            dp[i] = (choose_i , max(dp[i-1])) 
            
        return max(dp[len(ages)-1])
            


""" 
    解法二. 似乎根本不需要在dp表紀錄 選擇了選手i與不選擇選手i這件事 

        一樣使用雙loop , 如果遇到了前面的分數大於自己年紀又低於自己的 ,就不參與計算
        否則 dp[i] 直接等於 自身加上先前條件許可下的最高分數就可以了 , 另外稍微優化了一下迴圈內對list的參考
        
        稍微優化迴圈這件事情有蠻大幫助的 ,改為enumerate , 然後同時dp table只存一個值 
        時間與空間都到了還不錯的程度"""


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        # 第一步,需要針對年紀進行sorted , 透過zip組合後 , 按照tuple排序規則 , 優先排年紀再排分數值
        ref = sorted(zip(ages , scores))

        # ref[i] = (年紀,分數值)
        # create dp table , 
        dp = [   None for i in range(len(ages))   ]
        # base-case 
        for i , (age , score) in enumerate(ref): 
            # 選擇i至少有的分數
            dp[i] = score 
            # 改為內迴圈去比較在自己之前的所有值 
            for j in range(i) : 
                # 如果前面的分數值大於自己 , 年紀又小於自己,就不能納入
                if ref[j][1] > score and ref[j][0] < age : continue 
                # 否則就可以去更新加入自身的最大分數值
                dp[i] = max(  dp[i] , dp[j] + score )
        return max(dp)

        
        

# scores = [4,5,6,5]
# ages = [2,1,2,1]

scores = [1,2,3,5]
ages = [8,9,10,1]
S = Solution() 
S.bestTeamScore(scores , ages) 