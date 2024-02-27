"""
    Given a binary tree. 
    We want to find out that most frequent subtree sum in this tree . 

    if more than one subtree sum is most frequent and equals . 
    return all those value in any order 

    intution solution : 
        post-order traverse , and use a global list to collection all value 
"""
# Definition for a binary tree node.
from typing import Optional , List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        hashmap = dict() 

        def traverse(node): 

            if node is None : return 0 

            left_sum = traverse(node.left)
            right_sum = traverse(node.right)

            sub_tree_sum = left_sum + right_sum  + node.val 

            if sub_tree_sum in hashmap : 
                hashmap[sub_tree_sum] += 1 
            else :
                hashmap[sub_tree_sum] = 1 

            return sub_tree_sum

        traverse(root)  

        most_freq = 0  
        sol = []

        for val , freq in hashmap.items(): 

            if freq > most_freq : 
                most_freq = freq 
                sol = [val] 
            elif freq == most_freq : 
                sol.append(val)
        
        return sol





