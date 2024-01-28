""" 
    題意 :  
        設計一個class , 在初始化時給定一個首頁的url , 接下來每當我們造訪一個新的網站 , 就要將這個網站加入列表中
        (同時如果這個網站出現在先前列表中 , 則要將其移除並放到最新的位置)  , 
        同時要能夠後退與前進指定步數 . 
        
        總而言之 , 就是用visit造訪新頁面的時候需要刷新歷史紀錄 , 將造訪的頁面放到最新 , 
        而back , forward可以用來在歷史紀錄中移動 , 但不會刷新整個history

    思路 :

        這一題我認為一個完善的作法是 linked-list with hashtable , 利用linked-list來接歷史資料 , 
        同時使用hashtable去紀錄他們 , 這樣使用visited的時候才可以快速存取到他們
        
        這邊我就實做一個雙向linked list , 其中的每個節點都使用hashtable去保存 
        由於這一題並不存在 "刪除url"這件事 , 可以得知我們的linked list /hashtable 大小是單調增加的 ,
        
        
        <
        實際實做發現我原先的理解和題意不太一樣 , visited的重點在 "當下所在的網站移動到目標url" , 亦即current.next就要是目標 
        這會改動到linekd list的結構 , 因為當我們先back , 在visited新的 就會把back所退後的部份刪除 
        
        另外visited是不會更動到"前方的歷史紀錄 , 意思就是visited曾經出現的網站是沒差的"
        
        因此我這邊做的應對就是在back , forward時會改動hashtable , hashtable的意義變為 "還存在於linked list的內容"
        而tail的意義就不大了 , 因為在這個題意下 current就相當於tail  , 但我大部分的code用的都是tail , 所以這邊把current砍了
        >
        
        
        ----- Summary -----
        我這一題使用 hashtable加上linked list實際上就是我自己一箱情願 , 因為visited只清除曾經back過得瀏覽紀錄 , 並且不會需要把
        更前面的瀏覽網頁節點更改位置 , 因此這一題實際上就可以一個簡單的linked list辦到
"""


class website : 
    def __init__(self, url):
        self.url = url 
        self.next = None 
        self.prev = None 


""" 
    這個解法就是 hashtable + linkedlist , 可以正常運行 , 但實際上邏輯和原始題意要的不同 , 不過寫完也就當練習
    不同之處包含 :
    1. 一開始我以為back之後visited新頁面要保留因為back退後的部份 (visite的新頁加在linked list尾巴)  
        , 但實際上就是從當前頁面直接接上新頁 , 我的處理就是在back / forward 修改 hashtable
    2. 我原本以為visitd一個曾經到達的網頁會刷新他在history的位置 , 這也是一開始使用linked list + hashmap的原因 
        , 因為想要快速定位該頁面先前在哪 , 但實際上不需要這樣 , 新頁面就是直接接上linked list , 不用鳥先前已經出現過
"""
class BrowserHistory:

    # Browser histroy本質上就是一條linked list用來存著瀏覽紀錄 , 利用hashtable做快取
    def __init__(self, homepage: str):
        
        self.history = website(homepage) 
        
        # 快取網頁使用的url , key為url , value為對應的節點
        self.hashtable = {homepage : self.history}
        
        # 紀錄linked list的頭 , self.tail則是當前所在頁面
        self.head =  self.tail =  self.history
        
    # visited的實現包含在瀏覽新的頁面時 , 將其加入linked-list與hashtable , 並移動current
    def visit(self, url: str) -> None:
        
        # 如果url在hashtable中 , 說明必定在linked list中  
        # 需要移動該節點在linked list中的位置,必要時調整 head , tail 
        if url in self.hashtable : 
            
            # 如果該url就在linked-list的尾巴,則不用做任何事情 , 否則就要進行移動
            if self.hashtable[url] == self.tail : return 
                 
            # 如果該url是head , 就要移動head到下一個,同時把這個節點放到tail
            if self.hashtable[url] == self.head : 
                self.head.next.prev = None 
                self.head = self.head.next  
                
                self.tail.next = self.hashtable[url]
                self.hashtable[url].prev = self.tail 
                self.tail = self.hashtable[url]
                self.tail.next = None # 記得把新的tail的next設置為None
        
            # visit的目標不是head , tail 
            else : 
                
                self.hashtable[url].prev.next = self.hashtable[url].next  
                self.hashtable[url].next.prev = self.hashtable[url].prev  
                
                self.tail.next = self.hashtable[url] 
                self.hashtable[url].prev = self.tail 
                self.tail = self.hashtable[url]             
                self.tail.next = None 
                
        # 新拜訪的網站 , 則將其加入hashtable, 並且接到linked list的尾巴
        else : 
            
            self.hashtable[url] = website(url) 
            self.tail.next = self.hashtable[url] 
            self.hashtable[url].prev = self.tail 
            self.tail = self.hashtable[url]
        
        

    # 由tail開始使用prev後退step步 , 如果prev指向None則停止  , 過程中碰到的節點都要從hashtable刪掉
    def back(self, steps: int) -> str:
        
        for i in range(steps): 
            if self.tail.prev : 
                
                del self.hashtable[self.tail.url]
                self.tail = self.tail.prev 

            else : 
                break 
        
        return self.tail.url 
        

    # tail開始使用next前進step步 , 如果next指向None則停止
    def forward(self, steps: int) -> str:
        
        for i in range(steps): 
            if self.tail.next : 
                self.hashtable[self.tail.next.url] = self.tail.next 
                self.tail = self.tail.next 
            else : 
                break  
        
        return self.tail.url 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

""" 
    解法二 . 其實就是釐清題意之後 , 這個解時間空間都很不錯
"""
class website : 
    def __init__(self,url):
        self.url = url 
        self.next = None 
        self.prev = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = website(homepage) 
        self.tail = self.history

    def visit(self, url: str) -> None:
        
        node = website(url) 
        self.tail.next = node 
        node.prev = self.tail 
        self.tail = node 

    def back(self, steps: int) -> str:
        
        for i in range(steps): 
            
            if self.tail.prev : 
                self.tail = self.tail.prev 

            else : break 

        return self.tail.url
            

    def forward(self, steps: int) -> str:
        
        for i in range(steps): 
            
            if self.tail.next : 
                self.tail = self.tail.next 
            else : break 
        
        return self.tail.url 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)