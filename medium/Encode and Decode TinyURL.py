""" 
    題意:
        這一題是短網址服務系統設計的考題，要實做將長網址(原始網址)進行encode成為短網址的功能.
        另一方面就是要將被我們Encode的短網址map回原始網址.
        
        題目沒有限制要使用怎樣的encode/decode algorithms , 只要確保我們轉換過去的url能夠轉回來.
        總結來說,實做encode/decode的界面:
        - encode : 給定longUrl return tinyUrl 
        - decode : 給定tinyUrl return longUrl
        
    思路:
        這一題的設定蠻有趣的,我最直接的想法是hash or random之後使用一個dict去存. 而這樣的implement方式實際上有很多種
        我直覺想到的
        1. hash()值作為key , 但會需要處理collection 
        2. hash()+原始url作為Key , 這樣不會有collection , 但我在想key會不會太長而影響效能 -> 這樣反而增加網址長度,不可行
        3. random() 作為key , 並且透過while loop確保key不衝突(除非item相同) , 這樣做的缺點在於可能會有少量的重複key:value pair,
        
        一開始我認為是hash+separate chain比較好,但實際實做後想到,separate chain在同一個bucket內的節點都有相同key,即相同shortUrl,
        我沒辦法再透過這個shortUrl去找到到底哪個longUrl是對的 , 除非再返回的shortUrl再動些手腳
        而以random()作為key的方式則展現比較高效的結果,缺點可能是有更多的duplicate被放入
        
"""

""" 
    解法一. 方案3的實現,使用random來編碼 ,但無法排除可能有重複的key:value
        實際上這個解法的TC與MC都還挺不錯的, 如果在沒有'刻意'放重複的,那這個算法就算是相當有效了
"""
import random 
class Codec:

    def __init__(self): 

        self.hashmap = dict() 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = random.randint(0,100000) 
        
        while key in self.hashmap:
            key =  random.randint(0,100000) 
        
        self.hashmap[key] = longUrl
        return key 
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.hashmap[shortUrl]
        
        

""" 
    解法二. open address 
        這個解法在速度與空間就不如上面的random
"""


class Codec:

    def __init__(self): 

        self.hashmap = dict() 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hashVal = hash(longUrl) 
        
        while hashVal in self.hashmap : 
            hashVal = hash(hashVal+1)
        
        self.hashmap[hashVal] = longUrl
        return hashVal
        
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hashmap[shortUrl]
       
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))