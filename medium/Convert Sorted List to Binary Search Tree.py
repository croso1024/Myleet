""" 
    Covert the sorted linked list to binary tree : 
    1. Simple approach : 
        - a. transform the all node val in linked list in a list 
        - b. build the subtree by the list , recursively 
    2. Only linked list approach : 
        i think it need a subfunction to find the middle in linked list ,
        so basically is use the time to get more memory efficiency than approch 1 

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:


        # define a helper function to find the middle of linked list 
        # return the middle node , and the first node of left/right subtree 
        def findMiddle(linkedlist) :
            
            slow = fast = linkedlist 
            # prev is a pointer , use to delete the prev node.next before the middle
            prev = None 
            while fast and fast.next : 
                prev = slow 
                slow = slow.next 
                fast = fast.next.next 
            
            # We only have 3 case ,
            # 1. Just one node in list , so fast == slow 
            # 2. Just two node in list , so prev point to first node , fast is None 
            # 3. other 
            if slow == fast : 
                return linkedlist , None , None 
            else : 
                prev.next = None 
                return slow , linkedlist , slow.next 


        # given a sorted linked list , build the tree recursively
        def buildTree(node):
            if node is None : return None 

            # step.1 find out the center/left/right of tree
            centerNode , leftList , rightList = findMiddle(node) 
            subTreeRoot = TreeNode(val = centerNode.val)
            subTreeRoot.left = buildTree(leftList)
            subTreeRoot.right = buildTree(rightList) 

            return subTreeRoot 

        return buildTree(head)  

























