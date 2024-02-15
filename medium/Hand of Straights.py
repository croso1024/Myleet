from typing import List 

class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize !=  0 : return False 
        
        hashMap = dict()
        for i in hand : 
            if i in hashMap : 
                hashMap[i] += 1 
            else : 
                hashMap[i] = 1 
        
        # Use Queue 
        # sortedHand = sorted(hashMap.items() ) 
        sortedHand = sorted(list(set(hand)) , reverse=True ) 
        
        # 開始檢查是否可以組裝完成
        while hashMap : 
            
            cur_val = sortedHand.pop() # get val 

            while cur_val not in hashMap : 
                cur_val = sortedHand.pop()             
            
            for i in range(groupSize) :  
                
                if cur_val+i in hashMap and hashMap[cur_val+i] > 0 : 
                    hashMap[cur_val+i] -= 1
                else : 
                    return False 
                
                if cur_val+i in hashMap and hashMap[cur_val+i] == 0 : 
                    del hashMap[cur_val+i] 
                    
            if cur_val in hashMap : 
                sortedHand.append(cur_val) 
        
        return True                      
            
            
            
            
        
        