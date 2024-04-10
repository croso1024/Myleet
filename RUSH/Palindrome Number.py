class Solution:

    def isPalindrome(self, x: int) -> bool:

        probe = 10
        y = 0 
        ref = x 
        while (x > 0):
            
            # last digits 
            lastDigits = x % probe 
            # print(y,probe, lastDigits)
            y = (10*y) + lastDigits 
            x = x //  10 
                    
        return ref == y 

S = Solution()
S.isPalindrome(121)
S.isPalindrome(10)

S.isPalindrome(-3254)
S.isPalindrome(32323)
        