""" 
    題意:
        給定一個字串s , 要求計算所有唯一的 長度為3的"subsequence" 
        ex. "aabca" -> "aba" , "aaa" , "aca" 
        只會有小寫英文字
        
    思路: 
        這一題最naive的解法是 O(N^2) , 以每個字串為中心向左右擴散 ,
        我這邊直覺上想到的解法是 , 初始化雙指標在左右兩端 , 接著開始內縮
        一旦遇到雙指標指向了一樣的值 , 則中間的部份都可以作為長度為3的回文串  ,之後左右都內縮
        只是會有一個問題在於當雙指標指向不同的值 , 究竟應該要內縮左邊還右邊 , 我的解法是解兩次 ,一次遇到這個情況縮左,一次縮右
        就可以cover所有的答案 , 並用set去存unique的答案
        
        -------
        
        在上述作法不太可行後 , 我的第二個想法是hashtable ,去紀錄每個單字的第一次與最後一次出現,
        並將兩次出現中間的範圍加入set去計算 , 這就是個可行的解了 ,
        後來在Solution看到其他人的作法很類似 , 找該單字第一次和最後一次出現 ,
        但他們使用 len(set(s;[ first+1 : last ]))的方式 ,我自己認為這還是O(N) , 但在速度上確實有很大提昇
        
        
"""

""" 
    解法一. 按照原先的思路 , 但這樣做無法通過所有的測資 ,因為實際無法cover到所有可能的sequence , 即便我加上了flag的機制
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        sol = set() 
        
        left , right = 0 , len(s) - 1 
        flag = True 
        while left + 2 <= right :
            if s[left] == s[right] : 

                for i in range(left+1 , right): 
                    element = s[left]+s[i] + s[right]
                    if not element in sol : sol.add(element) 
                        
                left += 1 
                right -= 1 
                  
            # 當發生了不等於                      
            elif flag :   
                left += 1  
                flag = False 
            else: 
                right -= 1 
                flag = True 
                
        left , right = 0 , len(s) - 1 
        
        flag = False
        while left + 2 <= right :
            if s[left] == s[right] : 

                for i in range(left+1 , right): 
                    element = s[left]+s[i] + s[right]
                    if not element in sol : sol.add(element) 
                        
                left += 1 
                right -= 1 
                  
            # 當發生了不等於                      
            elif flag :   
                left += 1  
                flag = False 
            else: 
                right -= 1 
                flag = True 
                
        
        return len(sol)



""" 
    解法二. hash table
        我的下一個想法是使用hash table去紀錄每個字元第一次與最後一次的出現
        接下來遍瀝hashtable的key , 遇到有字元在這之間的就可以組合成一個解 
        
        這個解法就是正確的 , 只是時間很差worse case O(N^2) , 空間普通 O(unique char)
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashmap = dict() 
        sol = set() 
        for idx , char in enumerate(s): 
            if char in hashmap : hashmap[char][1] = idx 
            else : hashmap[char] = [idx,idx] 
        
        # 遍瀝hashmap裡面的itmes
        for key , (start , end ) in hashmap.items(): 
            # 如果這個字只出現一次 , 就不可能作為兩端
            for i in range(start+1 , end): 
                element = key + s[i] +key
                if not element in sol : sol.add(element) 
        
        return len(sol)
                


""" 
    解法三. 
        我在Solution看到了類似這樣的解法 , 被稱作使用O(N)的時間 , 主要還是得看把一段list轉為set到底需要多少時間複雜度
        我自己認為還是O(N) , 只不過因為是build-in function速度很快而已
        
        這個解的速度很優 , 但空間一樣不佳
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashmap = dict() 
        sol = 0 
        for idx , char in enumerate(s): 
            if char in hashmap : hashmap[char][1] = idx 
            else : hashmap[char] = [idx,idx] 
        
        # 遍瀝hashmap裡面的itmes
        for key , (start , end ) in hashmap.items(): 
            # 如果這個字只出現一次 , 就不可能作為兩端
            sol += len(set(s[start+1:end])) 
        
        return len(sol)
                
            

S = Solution()
test_case = "ckafnafqo"
print(S.countPalindromicSubsequence(test_case))
                