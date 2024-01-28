
""" 
    思路:   
        此題要我們反轉字串中母音的部份  hello -> holle , 
        我看test-case的感覺就是要找到成對的母音部份進行反轉 , 
        
        思路就是左右雙標 , 一個從左一個從右, 找到母音部份後swap即可 , 但因為不能直接操作字串
        需要先轉化成list來操作再join回去
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left , right = 0 , len(s) - 1 
        vowels = {"a","e","i","o","u" , "A","E","I","O","U"} 
        
        Solution = list(s) 
        
        while left < right : 
            
            # 讓left 走到定位 
            while left < right and not s[left] in vowels : 
                left += 1 
            
            # 讓right 走到定位 
            while left < right and not s[right] in vowels : 
                right -= 1 
            
            # 走到定位後兩邊都指向一個母音 , 進行swap 
            Solution[left] , Solution[right] = Solution[right] , Solution[left] 
            # 做完操作後再次內縮 
            left += 1 
            right -= 1 
        
        
        return "".join(Solution)