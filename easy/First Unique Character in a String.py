""" 
    題意:   
        給定字串 , 找出第一個沒有在字串中重複的charater , 並返回index
    思路: 
        直觀想法是hashtable紀錄文字是否出現以及其index 
        最後從只出現一次的那些字中找出index最小的, 這個想法TC:O(N) MC:O(N)

        但我想應該有 TC:O(N) MC:O(1) 的解 但因為only lowercase charater , so maximum memory complexity are O(26) 
    
"""
class Solution:

    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {} 
        
        for i,char in enumerate(s): 
            
            if char in hashmap: 
                hashmap[char][0] += 1 
            else : 
                hashmap[char] = [1 , i] 
        sol = float("inf")
        # 從hashmap char中index為1的去找出index最低的
        for times,index in hashmap.values(): 
            
            if times == 1 : sol = min(sol , index) 
        
        return sol if sol != float("inf") else -1 
                