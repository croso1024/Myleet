"""
題意 : 給兩字串,看一下A和B是否是相同字串的不同排列
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters

思路 : 直覺是Hashmap , 一個寫入字母/次數,另一個扣. 若兩者相同則應該剛好扣完, 另一種思路是 sorted 直接比Equal 

- sorted比 equal : 2 x O(NlogN)   ,空間O(N)
- hashmap : 儲存 2 x O(N) , 時間O(N)


複雜度 : Time O(?) / Space O(?)

Trade-off :

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) : return False

        sorted_s = sorted(s) 
        sorted_t = sorted(t) 

        return sorted_s == sorted_t 


class Solution : 
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) : return False 

        map = dict() 

        for element in s : 
            if element in map :
                map[element] += 1 
            else : 
                map[element] = 1 

        for element in t : 
            if element not in map : 
                return False 
            else : 
                if map[element] == 1 : 
                    del map[element] 
                else : 
                    map[element] = map[element] - 1 

        return len(map) == 0                  
        
