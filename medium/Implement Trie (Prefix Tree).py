"""
    題意:

        此題要求我們實現前綴樹,並完成以下幾個function
        - insert(string word) , 將一個string插入tree
        - search(string word) , 檢查這個string是否存在於樹中
        - startWith(string prefix) , 檢查這個開頭是否存在於樹中
        
    思路:    
    
        由於這一題已經說明所有string的內容都是小寫英文,一此tree中的每個節點最多都有26個分支.
        另外因為在search時我們為了要區分'該字串是否曾經被insert過,還是其實被插入的是前綴完全一樣的字串' , 因為這件事
        我們必須在tree的節點上加入一個flag , 說明是否有被插入過到此為止的節點.
        當遇到這個節點時我們就能夠驗證從tree的root一路走下來的字串是真的有曾經insert過
        由於這一題沒有要求我們實做刪除的功能,所以整體而言不複雜
        
        
        我們先定義一個Tree node class , 在字典樹中的節點都maintain一個hashmap , 用來表示該節點下面還有接什麼字母,
        同時包含該節點代表的字母,以及前述所說的terminal flag.
"""


""" 
    解法一. 按照上述思路實做 , 另外在實做的時候有想到.
        除了使用terminal flag以外,實際上也可以直接把字放在set中,這樣在查詢時可以快速hashset看 , 但MC不佳
    
"""
class TreeNode: 
    
    def __init__(self, letter=None): 
        self.letter = letter 
        self.child = {} 
        self.terminal = False 
        
class Trie:

    def __init__(self):
        
        self.root = TreeNode() 
        
    # insert的時候使用一個probe指向當前導引到的節點
    # probe最終會停止在這個字母的最後一個字, 順便就設定terminal flag
    def insert(self, word: str) -> None:
        
        probe = self.root 
        
        for letter in word: 
            # 如果該字母還不存在於tree , 就建立節點            
            if not letter in probe.child  : 
                probe.child[letter] = TreeNode(letter=letter)  
                
            probe = probe.child[letter] 
        # 在return前把該節點的terminal flag打開        
        probe.terminal = True 
        return 
        
    # 走for loop , 理論上需要每一個節點都存在並且最後一個字母還要是terminal == True 
    def search(self, word: str) -> bool:
        
        probe = self.root 
        
        for letter in word : 
            if not letter in probe.child : return False 
            probe = probe.child[letter]  
        
        if probe.terminal : return True 
        else : return False 

    # 這邊實際上就跟search的邏輯一樣 , 只差別在最後一步是否需要判斷terminal
    def startsWith(self, prefix: str) -> bool:
        
        
        probe = self.root 
        
        for letter in prefix : 
            if not letter in probe.child : return False 
            probe = probe.child[letter]  
        
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)