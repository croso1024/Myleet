from typing import List 

""" 
    思路:
        給定一個array 和 常數k , 返回在這個array中出現頻率前k高的值 
        k的範圍在 [1,總共有幾個不同值] .

        思考一下,直覺上的作法 : 
        先用一個table去紀錄所有值出現的次數 , O(N)時間與空間 
        接著建立一個heap , 以出現次數作為priority丟進去heap , 把table中所有值都丟進去heap , O(NlogN)時間與O(N)空間
        最後把前k個值丟出來結束 , 但實做上會比上面的描述更好 , 因為table儲存的key數量與heap keep的數量都可以優化

        follow-up 題目希望可以有比O(NlogN)時間還要好的算法 

        我猜測題目原始的O(NlogN)算法應該是指用table統計所有值的出現次數後做sorted
"""

"""
    解法一. 先使用我直覺的解法, 整個處理拆成3個part , 紀錄表/heap/pop k    
    
    這個解法的時間與空間都相當不錯 , 我們的儲存實際上就是
    table: 時間O(N) , 空間O(獨立值) 
    heap : 時間O(獨立值 log k) , 空間O(k)
    
    基本上時間就是 O(獨立值數量 log k) , 比題目的O(NlogN)還要好
"""
from heapq import heappush , heappop 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 紀錄表
        table = dict() 
        for item in nums: 
            if item in table : table[item] += 1 
            else : table[item] = 1 
        
        # 這邊heap使用python的特性 , tuple 的比較大小會先比tuple的第一個值 , 如果一樣就比第二個值
        # 以出現次數作為heap的priority ,預設是min heap, 所以出現次數最少的會在頂端 , 我們就是要維持這個頂端就是出現次數排在第k大的

        # heap儲存的東西: ( 出現次數:值 )  , 因為比較的優先是比出現次數
        heap = [] 
        
        for item in table: 
            
            if len(heap) == k and table[item] > heap[0][0] :  
                heappop(heap)
                heappush(heap , ( table[item], item) )
        
            elif len(heap) < k :
                heappush(heap, ( table[item],item)) 
        
        # 把所有仍在heap中的值作為答案
        return [item[1] for item in  heap]
                
"""
    解法二.
        針對每個數字的出現頻率做sorted ,
        計算table一樣O(N)時間加上O(獨立值)空間 
        因此再sorted時應該是O(獨立值log獨立值)    
        
        這個解的時間空間也不錯
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = dict()
        for item in nums:
            if item in table : table[item] += 1 
            else : table[item] = 1
        
        ref = [  ( table[item] , item )   for item in table ] 
        ref.sort()
        
        sol = []
        for i in range(k): 
            sol.append( ref[len(ref)-i-1][1]   )

        return sol 






"""
    解法三. 
        雙table參照 , 一個table紀錄 值:出現次數 , 一個table紀錄  出現次數:set(值1,值2) ...        
        這個解法速度和上面比起來沒有特別突出 , 但空間99% 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        table1 = dict()
        table2 = dict() 

        for num in nums : 
            
            if num in table1 : 
                
                if  table1[num] +1 in table2 : 
                    table2[table1[num]+1].add(num)     
                    table2[table1[num]].remove(num) 
                    
                else :
                    table2[table1[num]+1] = {num} 
                    table2[table1[num]].remove(num)  

                table1[num] += 1 
                
            else : 
                
                if 1 in table2 : 
                    table2[1].add(num) 
                else :
                    table2[1] = {num}
                
                table1[num] = 1
                
        # 此時table2就紀錄了出現次數與在這個次數的值集合
        sol = [] 
        
        # 依照出現次數去sorted table2的key 
        for freq in sorted(table2.keys() , reverse=True) : 
            sol +=  list(table2[freq]) 
            if len(sol) == k : return sol 
            

            
                    
                
                
                
            