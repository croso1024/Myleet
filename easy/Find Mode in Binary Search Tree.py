from typing import Optional , List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
""" 
    這一題要我們找出在Binary tree裡面出現過最多次的節點 , 
    常規思路就是 Traverse+一個dict保存所有節點的出現次數 , 最後列出出現過最多次的
    但這一題的follow up 希望我們可以使用常數空間複雜度來做 
    ( 只接受recursion stack 的space ) 
    
    常數空間複雜度的關鍵可能是 in-order traverse , 
"""
        
""" 
    解法一. 
        先做一個常規思路 , traverse加上dict的紀錄 , 比較關鍵的是取得table後的處理 
        因為我們要做的是"取出多個同為最大的值" , 因此不需要sorted 或是max完再max 
        可以一次的線性尋訪完成
"""        

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.table = dict()
        
        def traverse(node): 
            if node is None : return 
            
            # 加入對照表在pre/in/post order都沒差 , 這邊加在pre-order 
            
            if not node.val in self.table : 
                self.table[node.val] = 1 
            else : 
                self.table[node.val] += 1 
            
            traverse(node.left)
            traverse(node.right) 
        
        traverse(root) 
        
        # 至此已經統計了所有節點出現的次數 , 但題目給定可能同時有多個mode,思路包含
        
        # -> Sorted & pick  take O(N log N) 
        # -> find max then iterate  modes * O(N)
        # -> 手動線性走訪一次 , 遇到最大值就更新值以及返回mode,遇到相同值就append 
        #    如此一來就是線性時間完成
        
        maximum = float('-inf')

        for key,value in self.table.items() : 
            if value > maximum : 
                maximum = value 
                mode = [key]     
                
            elif value == maximum : 
                mode.append(key) 
            
        return mode 
            

""" 
    解法二. 
        來思考如何完成follow-up要求的O(1) space complexity , 
        透過in-order我們可以依照值的大小來尋訪 , 應該就可以再那個時候累積該數值出現的次數 , 並再下一次出現新的數值時做更新 
        
        這個解法的細節也就在於處理in-order內容的順序 , 是否有前一個節點 , 紀錄節點初次數 , 
        prev , prev_freq , mode , mode_freq的操作 , 另外一開始寫的時候我出現一個細節錯誤在於我在prev is None時 
        初始化看到的第一個節點同時也將該節點加入mode , 因為我原本想著之後出現更大的節點時能夠覆蓋掉 , 
        但反而會造成這個初始節點(如果他也確實是出現多次)那就會被加入mode第二次 , 
        
        換句話說加入的功能我本來就已經寫在新節點不等於prev , 因此不需要加在prev初始化時
"""

class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        mode = list() 
        mode_freq = 0 
        prev = None
        prev_freq = 0 
        
        # 為了要完成O(1)空間複雜度 , 所有的操作在in-order位置進行 , 利用in-order的sorted property
        # 因為這相當於線性尋訪一個sorted完成的array , 我們實際在做的就是紀錄每一個元素出現的個數 , 
        # 當切換元素的時候去比較是否大於 , 等於目前的最佳並做更新
        
        def  traverse(node): 
            nonlocal prev , prev_freq , mode , mode_freq
            if node is None : return  
            
            traverse(node.left) 
    
            # 如果prev存在 , 
            # -> 且prev不等於目前尋訪的節點,則要看情況更新mode , mode_freq 
            # -> prev等於目前尋訪的節點 , 則prev_freq += 1
            if not prev is None : 
                # 尋訪到與上個節點相同的數值
                if prev == node.val : 
                    prev_freq += 1 

                # 當找到一個不一樣的數值之後 ,進行更新                
                else : 
                    if prev_freq > mode_freq :  
                        mode = [prev]
                        mode_freq = prev_freq 
                        
                    elif prev_freq == mode_freq : 
                        mode.append(prev)
                    # 找到一個不同的數值 , 那prev的出現次數要變回 1  , 並且更新prev
                    prev = node.val
                    prev_freq = 1 
                    
            # 如果prev不存在 : 
            # 那代表我們進入第一個節點的內容 , 更新prev , prev_freq , mode , mode_freq 
            else : 
                prev = node.val 
                prev_freq += 1 
                # 加入mode我已經寫在切換節點內容的時候 , 因此實際上初始化不需要加入mode , 這可能會造成重複加入
                #mode.append(node.val)
                #mode_freq = 1

            traverse(node.right) 
        
        # traverse完成後 , 會拿到Tree中最大數值節點的出現次數 , 和mode做個最後比較 
        traverse(root) 
        
        if prev_freq > mode_freq : 
            mode = [prev] 
        elif prev_freq == mode_freq :
            mode.append(prev) 
            
        return mode
        
            
            