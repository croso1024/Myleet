"""
    題意 : 問給定的字串在全部轉小寫,移除 non-alphabet 字元後是否對稱

    思路 : 雙指標指向兩端,開始迭代中間跳過所有non-alphabet 

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        clear_string = ""

        
        def is_alphanumeric(char:str) -> bool :
            return ('a' <= char <= 'z' ) or ('A'<=char<='Z') or  ('0' <= char <='9')

        for char in s : 
            if is_alphanumeric(char): 
                clear_string += char.lower()
        left = 0 
        right = len(clear_string) - 1

        while left < right : 
            if clear_string[left] == clear_string[right] : 
                left +=1 
                right -=1 
            else : 
                return False  

        return True 

        # left = 0 
        # right = len(s) - 1 

        # while left < right : 
            
        #     while left < right : 
        #         if not is_alphanumeric(s[left]) : 
        #             left += 1 
            
        #     while left < right : 
        #         if not is_alphanumeric(s[right]): 
        #             right -= 1 
            
        #     if left 
                    


c = Solution()
c.isPalindrome("A man, a plan, a canal: Panama")


