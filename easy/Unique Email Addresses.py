from typing import List 
""" 
    題意 : 
        此題提供了一個有效的email規則 , 一組email透過@符號分為local name與domain name, 
        而local name中可能會存在"."與"+" 兩個符號 , 這兩個符號在local name中有特殊的運算規則如下 
        - 在local name遇到 "." 會自動忽略 
        - 在local name遇到 "+" 後 , local name剩餘部份就會自動忽略
        ex. " m.y+name@email.com " -> " my@email.com " . 
        
        題目給定一個email address list , 要我們計算當中總共有幾個不同的email信箱 
    
    思路 : 
        這一題只是個easy , 我會覺得只是用"@"符號去切分 local name與domain name ,
        接下來用一個hashmap去存處理完成的local name , 每一格hashmap對應到一個domain set , 
        
        如此一來我們只要維護一個counter , 遇到一個不在hashmap key以及domain set的內容就去增加counter並更新map即可
"""



""" 
    解法一.  將這個問題拆解為兩個部份 , 分割local/domain name以及使用hashmap檢查唯一的email address 
    
        拆解的function需要 O(email address長度) 
        而後檢查的迴圈則需要O(N) ,
        space則是O(N) , 因為最多n個獨立address
        
        實際結果的速度偏差 , 空間還不錯
"""
class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:

        sol = 0 
        hashmap = dict() 
        
        # 將一個地址拆分為有效的local name 與 domain name  , 基本上要take O(N) 
        # 這邊實做第一種解法 , 使用index of去拿"@" , 在將分割出來的local name做額外處理
        def addressParser(email:str):

            sep = email.index("@")  
            
            domain_name = email[sep+1:]
            local_name = "" 
            
            for i in range(sep): 
                if email[i] == "." : pass 
                elif email[i] == "+" : break 
                else : 
                    local_name += email[i] 
                
            return local_name , domain_name 

        # 拆分出local , domain 
        for email in emails : 
            
            local , domain = addressParser(email) 
            
            if local in hashmap :
                
                if domain in hashmap[local] : pass 
                else : 
                    hashmap[local].add(domain) 
                    sol += 1 
                
            else : 
                sol += 1 
                hashmap[local] = {domain} 
        
        return sol 


