"""
    題意 : 問給定的字串在全部轉小寫,移除 non-alphabet 字元後是否對稱

    Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

    思路 : 
    使用雙指標,掠過non-alphabet字元後,比較兩端字元是否相同 

    1. 簡單的實作,先清除 non-alphabet字元後,再使用雙指標比較兩端字元是否相同 ( 讓雙指標實作比較簡單 )
    2. 直接雙指標,及時處理non-alphabet字元 

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


class Solution:

    def isPalindrome(self, s: str) -> bool:


        def is_alphanumeric(char:str) -> bool :
            return ('a' <= char <= 'z' ) or ('A'<=char<='Z') or  ('0' <= char <='9')


        left = 0 
        right = len(s) - 1  

        while left < right : 


            while left < right and not is_alphanumeric(s[left]) : 
                left += 1 

            while left < right and not is_alphanumeric(s[right]): 
                right -= 1  
            
            if left < right :  

                if s[left].lower() == s[right].lower() : 

                    left += 1 
                    right -= 1 
                    
                else : 
                    return False 
        
        return True 


c = Solution()
print(c.isPalindrome("A man, a plan, a canal: Panama"))

test_set = [
    ("A man, a plan, a canal: Panama" , True)  , 
    (" ", True) , 
    (" A" , True), 
    ("A",True) , 
    ("ABA" , True),
    ("ABAA" , False),
    ("ABAAA" , False),
    ("AAAA" , True),
    ("AABAA" , True),
    ("AABAC" , False),
    ("1AA1" , True),
    ("1AA111112A1" , False),
    ("@A**@(!!@*2A1" , False),
    ("@A**@(!!@*2A" , True),
]


for test in test_set : 

    input , expected = test   

    if expected == c.isPalindrome(input) : 
        print(f"Pass : {input} | Expected : {expected}") 
    else :
        print(f"Failed : {input} | Expected : {expected}") 


