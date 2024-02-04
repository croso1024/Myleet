""" 
    題意 : 
        給定一個有n個節點的tree ,並使用parent array來表示並以index=0作為root. ( so parent[0] = -1 ) 
        我們要設計一個資料結構允許用戶去鎖定,解鎖與更新這棵tree內的node 
        這個資料結構要支援以下:
        1. Locks : 為特定user鎖定特定的node , 並且使得其他user不能也lock這個node , 這個function只能使用在一個還沒有被lock的node上
        2. Unlocks : 為特定的user去解鎖node , 只有這個function可以去解鎖節點 (要user有對上才能解鎖)
        3. Upgrade : 為特定user去lock給定節點 ,同時unlock這個節點之下的所有節點(無論是誰lock上的) , upgrade只有在以下三個條件滿足時可用
            - 該節點為unlock
            - 其節點的descendant至少要有一個被lock 
            - 其節點沒有任何被lock的ancestors
        
        
    思路 : 
        這一題在例子中只有使用一些簡單的lock ,unlock , 而這些操作基本上都可以透過一個簡單的dict去處理. 
        比較需要去思考實做的是upgrade , 整個upgrade的步驟我認為可以拆分為: 
            - 檢查指定node是否為unlock  -> by hashtable
            - 檢查ancestor都是unlocked   -> trace the parent array & use hashtable 
            - 檢查decestor至少有一個locked  -> 我認為一個較好的方式就是maintain 一個 decestor lookup-table
            
        我的核心思路就是去maintain一個table用來紀錄每一個節點他的decestor有多少個被lock , 或著是儲存被lock的descentor
        在lock和unlock操作中去修改這個table (因為給了parent array , 所以lock,unlock操作後比較容易去操作其ancestor )
            
    
"""

""" 
    解法一. follow我的解題思路去走 ,
        lock,unlock function都簡單明瞭 , 就是在處理上鎖的過程中更新descendant table 
        而upgrade比較特殊 , 除了幾個條件去判斷是否可以upgrade以外 , 一旦可以upgrade , 
        就需要去把要upgrade的目標的 descendant table移除要upgrade目標的descendant ,接著加上目標節點 
        之後要將 upgrade目標之下所有節點解鎖並清空desendant-table , 我使用了一個visted set去加速這一part , 避免重複砍
        
        
        時間複雜度 O(logN) , 空間比較難計算 , 因為我有N個節點 , 每個節點在table上最多都會保存其子樹大小的節點數

"""
from typing import List 
class LockingTree:

    def __init__(self, parent: List[int]):
        
        self.parent = parent
        # 建立locked表,用來保存每個節點是被誰lock住 , None 代表該節點沒有被lock
        self.locked = { i : None for i in range(len(self.parent))  }
        # 建立descentor locked table , 表示每個節點的descendant有哪些是locked的
        self.descendant_table = {i : set() for i in range(len(self.parent))}


    # 檢查節點是否被誰lock住了 , 如果沒有的話就開放lock , 同時修改descendant table
    def lock(self, num: int, user: int) -> bool:
        
        if  self.locked[num] is None : 

            self.locked[num] = user 
            
            # 在回溯到root之前
            parent = self.parent[num]

            while parent != -1 :  
                
                self.descendant_table[parent].add(num) 
                
                parent = self.parent[parent]
                            
            return True
        
        else : 
        
            return False 
        

    def unlock(self, num: int, user: int) -> bool:
        
        # 如果locked array告訴我們該節點有被鎖住 , 並且鎖定者也為相同user時才可以解 , 其餘無法
        if not self.locked[num] is None and self.locked[num] == user : 
            
            self.locked[num] = None 
            
            parent = self.parent[num] 
            
            while parent != -1 : 
                
                self.descendant_table[parent].remove(num) 
                
                parent = self.parent[parent]
            
            return True 
            
        else : 
            return False 
            
        

    def upgrade(self, num: int, user: int) -> bool:
        
        # 觸動upgrade需要滿足三個條件 , 該node為unlocked , 其descendant至少有一個lock , 其ancestor都是 unlock
        
        # 條件1,2
        if self.locked[num] is None and len(self.descendant_table[num]) > 0 : 
            # 檢查條件3 
            parent = self.parent[num] 
            while parent != -1 :  
                if self.locked[parent] is None : 
                    parent = self.parent[parent]
                else : return False 
            
            # 到這邊就是可以進行upgrade , upgrade操作 , 需要locked該節點 , 同時解鎖所有descendants .
            # 我的操作就是趁著還拿著該節點的descendants table , 我先將所有ascentor的descendants table做更新 , 再將所有descendant解鎖

            locked_descendant : set 
            locked_descendant = self.descendant_table[num] 
            
            # 將upgrade的節點鎖定
            self.locked[num] = user 

            # 幫所有ascentors移除待會要解鎖定的那些            
            parent = self.parent[num] 
            while parent != -1 : 
                self.descendant_table[parent].difference_update(locked_descendant) 
                self.descendant_table[parent].add(num) 
                parent = self.parent[parent] 
            
                
            # 清除完了之後可以開始解鎖descendant 
            for node in locked_descendant : 
                self.locked[node] = None 

            # 還有一個很重要的一步 , 把descendant到num中間的這些節點 , 清除掉descendant table, 可以想成在num底下沒有任何locked node了
            # 而這一步除了將所有locked_descendant的節點一個個拿出來做tree往上的更新 , 我自己是加上一個visited table來加速
            deleted = set() 
            for node in locked_descendant :  
                
                self.descendant_table[node] = set()
                deleted.add(node) 
                
                parent = self.parent[node]
                # 在descendant到num之間的節點要清空 descendant_table
                while parent != num : 
                    
                    if parent in deleted : break  
                    self.descendant_table[parent] = set()
                    deleted.add(parent)
                    parent = self.parent[parent] 
                    
            
            return True 
                        
        else : return False 
            

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)