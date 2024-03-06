""" 
    題意:

        給定一組整數array以及兩個整數k,threshold , 返回在這組array中有多少組size為k的sub-array其平均值>=threshold
        另外雖然題目沒有寫清楚,但看起來sub-array的定義是要連續的陣列
        
    思路:

        這題重點在於知道是連續陣列,這樣一來就直接走sliding window with fixed size window. 
        然後將滿足的答案次數記錄下來即可
    
"""

""" 
    解法一. sliding window 模板,已經有不錯的速度以及很優的空間 , 但考慮到這一題是fixed-size window,
        我覺得用for-loop的寫法有更好的readibility 
"""
from typing import List 
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        left , right = 0 , 0 
        size = len(arr) 
        window_avg , window_size = 0 , 0 
        solution = 0 
        
        
        while right < size : 
            
            window_avg += (arr[right]/k) 
            window_size += 1 
            
            
            while window_size == k : 
                
                if window_avg >= threshold : 
                    solution += 1
                
                window_avg -= (arr[left]/k) 
                window_size -= 1 
                left += 1 
            
            right += 1 
        
        return solution 
                
""" 
    解法二. 使用for-loop的解法 , 時間反而比較慢,空間更好
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_avg = sum(arr[:k])/k 
        solution = 0 
        
        if window_avg >= threshold : solution+=1 
        
        for i in range(k , len(arr)): 
            
            window_avg -= (arr[i-k]/k) 
            window_avg += (arr[i]/k) 
            
            if window_avg >= threshold : solution += 1 
            
        return solution 