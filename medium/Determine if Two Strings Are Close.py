""" 
    思路 :  
        這一題給定兩個字串 , 問這兩個字串是否"Close" 
        Close的定義為 , 如果其中一個字串可以透過以下的操作變成另外一個 , 即close : 
        - 任意swap字串中的兩個字元  ex. abcde -> aecdb , swap了b,e
        - 選定兩種字元 , 將整個字串中他們出現的部份彼此對調 , ex. aacabb -> bbcbaa  
        
        這一題想法上我認為就是去找上面兩種operation的限制 , 實際上兩種operation都無法改變字串的長度 
        第一點能夠任意swap元素 , 代表如果兩個字串有著相同的字母,我們就不需要考慮他的位置問題
        第二點較為複雜 , 可以對調部份元素 , 這一點會讓字串中某個字元的數量改變 
        
        但簡單總結一下 , 兩個可以經由以上operation後變為相同的字串至少有以下幾點
        - 長度相同
        - 裡面所出現的單字種類數相同  
        - !? 將各個單字出現頻率經過sort 可以得到一個相同的陣列 
            例如原始範例 aacabb : a:3 b:2 c:1  , bbcbaa : a:2 b:3 c:1  
            依照相同思路  abccbc : a:1 b:2 c:3 也可以 
            
"""

""" 
    解法一. 就是follow上面的思路 , 只是速度不佳,空間很差 
    因為sorted的關係take O(NlogN) , 空間則是O(N) ,我存了兩個字串的內容
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2) : return False 
        
        # 建立dict
        dict1 , dict2 = dict() , dict() 
        
        for char in word1 : 
            if char in dict1: dict1[char] += 1 
            else : dict1[char] = 1 
        
        for char in word2 : 
            if char in dict2 : dict2[char] += 1 
            else : dict2[char] = 1 
        
        if len(dict1.keys()) != len(dict2.keys()) : return False 
        for key in dict1: 
            if not key in dict2: return False 
            
        # 至此, 字串長度一樣 , 有著相同的單字組成 , 就要比較內容結構的sort是否也相同 
        return  sorted(dict1.values()) == sorted(dict2.values())
    

""" 
    解法二. 優化速度至O(N)
        上述解法一最後一步我使用sort去檢查內容結構 , 但這一部份也能夠轉成使用dict
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2) : return False 
        
        # 建立dict
        dict1 , dict2 = dict() , dict() 
        
        for char in word1 : 
            if char in dict1: dict1[char] += 1 
            else : dict1[char] = 1 
        
        for char in word2 : 
            if char in dict2 : dict2[char] += 1 
            else : dict2[char] = 1 
        
        if len(dict1.keys()) != len(dict2.keys()) : return False 
        for key in dict1: 
            if not key in dict2: return False 
            
        dict3 = dict()
        dict4 = dict() 
        
        for value in dict1.values(): 
            if value in dict3 : dict3[value] += 1 
            else : dict3[value] = 1 
        
        for value in dict2.values(): 
            if value in dict4 : dict4[value] += 1 
            else : dict4[value] = 1 
        
        return dict3 == dict4
    