from typing import Optional , List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

""" 
    給定一個不包含重複元素的int list : nums , 
    從中選擇一個最大的元素作為root ,並且root在nums中的id為 id_root 
        -root的left child是以相同方式使用nums[:id_root]作為新的nums建立
        -root的right child則是nums[id_root+1:]來建立 
    
    這一題看起來就是一個遞迴下去做 , Base case是nums為空 , 
    並且recursion function返回建立完的Sub-Tree , 在post-order的位置做接合
        
    釐清這些看起來這題蠻簡單的    
"""


class Solution:
    
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        

        # 給定nums進行遞迴 , base case為nums為空 , 返回一個以nums建立的tree 
        def recursion(nums) : 
            
            if not nums : return None
            elif len(nums) == 1: return TreeNode(val=nums[0]) 
            
            # 用一個線性探測來找到maximum value以及index 
            maximum ,max_id = nums[0] , 0 
            for i in range(1,len(nums)) :  
                if nums[i] > maximum : maximum , max_id = nums[i] , i
            # 取得用來當作root的最大值和他的index 
            
            # 取得maximum_id後就可以順利拆分左右array            
            left_subTree = recursion(nums[:max_id])
            right_subTree = recursion(nums[max_id+1:])
            
            sub_root = TreeNode(val = maximum) 
            sub_root.left = left_subTree 
            sub_root.right = right_subTree 
            
            return sub_root 

        return recursion(nums)
            