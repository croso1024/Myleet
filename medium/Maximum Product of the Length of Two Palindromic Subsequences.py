""" 
    題意:
        給定一個字串S , 我們要在字串中找出兩組disjoint palindromic , 
        並且讓這兩組palindromic的相乘最大化
        ex. 
            "leetcodecom" , 第一個palin可以選ete , 另外一個可以選cdc , 這樣就是 3x3 = 9 
        p.s : 是用palindromic字串的長度相乘 , 不是index距離

    思路:   
        我的想法是可以先找出所有palindromic , 標出他們佔用的index,
        接著把所有palindromic兩兩交乘,排除掉有重疊的就可以找到解
        另外我的palindromic table只紀錄index , 以index作為key
        
        這個解法只能免強解, 會出現Time limit exceed 的狀況, 後來看Solution有個DFS作法讓我驚為天人
"""

class Solution:
    
    def maxProduct(self, s: str) -> int:
        
        sol = 1

        def dfs(current_index , palin1 ,palin2) : 
            nonlocal sol 
            
            if palin1 == palin1[::-1] and palin2 == palin2[::-1] : sol = max(sol , len(palin1)*len(palin2))   
            if current_index == len(s)  : return 
            # 每一個狀態都能做3種事情 , 
            #.1. 挑選當前字母放入palin1 
            #.2. 挑選當前字母放入palin2
            #.3. 不挑這個字母
            dfs( current_index+1 , palin1 + s[current_index] , palin2)
            dfs( current_index+1 , palin1 , palin2 + s[current_index])
            dfs( current_index+1 , palin1 ,palin2) 
        
        dfs( 0 , "" , "") 
        print(sol)
        return sol 
            
            
                
                
                
C = Solution() 
C.maxProduct("leetcodecom") 
C.maxProduct("bbbc") 
C.maxProduct("zqz") 
C.maxProduct("abbcda")
C.maxProduct("accbcaxxcxx")
C.maxProduct("yqqrqqy")
                
        
        