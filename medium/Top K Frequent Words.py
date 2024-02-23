class item : 

    def __init__(self,word): 
        self.word = word 
        self.times = 1  
    
    def __gt__(self,other): 
        if self.times == other.times: 
            # reverse the word compare rule , so when we use reverse sort , 
            # the order will match the problem rule
            return self.word < other.word 
        else : 
            return self.times > other.times 
    
    def __lt__(self,other): 
        if self.times == other.times: 
            # reverse the word compare rule , so when we use reverse sort , 
            # the order will match the problem rule
            return self.word > other.word 
        else : 
            return self.times < other.times  
    
    def __eq__(self,other): 
        if self.times == other.times : 
            return self.word == other.word 
        else : return False 

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        hashmap = dict()
        for word in words : 
            if word in hashmap:
                hashmap[word].times += 1  
            else : 
                hashmap[word] = item(word)
        
        return [   item.word for item in list(sorted(hashmap.values() , reverse=True))[ :k ] ] 
