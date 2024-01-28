""" 
    思路 :  
        這一題給定兩個array , gas , cost , gas[i]代表在這裡可以補充的瓦斯 , 
        cost[i]則是從gas[i]到gas[i+1 % len(gas)]的代價 
        這一題要問從哪出發可以繞完一整圈 ,如果有答案 , 則答案是唯一的
        

        把gas和cost陣列相減 , 可以得到每一步的淨瓦斯消耗 , 如果這個淨消耗總和>=0才能走得回來
        計算得到這個陣列後 , 暴力解就比較明瞭了 , 雙迴圈
"""


""" 
    解法一. 
        雙迴圈 , 算出淨瓦斯增減 ,這邊其實還是有一些優化的手段能做 
        1. 如果起點的淨值<0 , 跳過
        2. 從淨值>=0的開始 ,如果該index也是無法完成一圈 , 那與其相鄰的正淨效率也都一定無法(可以全跳)
        這個解法看起來是可行的 , 問題出在說速度還是不夠
"""
from typing import List 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        size = len(gas)
        net = [  gas[i]-cost[i] for i in range(size) ] 
        start = 0 
        
        # 外層迴圈走過所有可能
        while start < size : 

            # 起點淨值必須得大於0 
            if net[start] >= 0 : 
                
                acc = 0
                step = 0

                # 只要瓦斯維持是正的 , 就能一直走 
                while step < size and acc >= 0 : 
                    acc += net[(start+step)%size] 
                    step += 1  
                #如果成功走了一整圈,還有瓦斯(代表還能走 ,可以走到一開始的起點) , 那就是答案 
                if step == size and acc >=0 : return start 
                # 如果從這邊無法走完 , 那我們可以跳轉到下一個正出現
                else : 
                    
                    step = 1 
                    while start+step < size and net[start+step] < 0 : 
                        step += 1 
                    start += step 
            
            else : 
                start += 1 
        
        return -1


""" 
    解法二 . 實際上我一開始就有想到這個思路 , 但細節失誤沒有成功 
    
    比起解法一 , 我們在某個點失敗後就跳過那個點開始其他是正淨效率的繼續開始 ,
    在這邊如果從起點i開始走到j走不下去 , 那i與j之間所有點都是不可能作為起點 
    
    所以這樣可以把計算速度拉到O(N)級別 
    
    實際上這解法就是能過測資 , 但時間還是普通 , 比較好的是空間很優 , 
    參考東哥版 , 這一題的另一種解法應該是圖像平移 ,我想那個解法就是需要空間的 ,但速度應該更快    

"""

from typing import List 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        size = len(gas)
        net = [  gas[i]-cost[i] for i in range(size) ] 
        start = 0 
        
        # 外層迴圈走過所有可能
        while start < size : 

            # 起點淨值必須得大於0 
            if net[start] >= 0 : 
                
                acc = 0
                step = 0

                # 只要瓦斯維持是正的 , 就能一直走 
                while step < size and acc >= 0 : 
                    acc += net[(start+step)%size] 
                    step += 1  
                #如果成功走了一整圈,還有瓦斯(代表還能走 ,可以走到一開始的起點) , 那就是答案 
                if step == size and acc >=0 : return start 
                # 如果從這邊無法走完 , 實際上從中間的過程開始走也不可能繞的完
                else : 
                    start += step
            
            else : 
                start += 1 
        
        return -1
                    