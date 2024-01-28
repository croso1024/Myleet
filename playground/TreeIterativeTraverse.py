""" 
    紀錄一下使用迭代的方法處理三種traverse
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Root = TreeNode(val=1) 
Root.left = TreeNode(val=2)
Root.right = TreeNode(val=3)
Root.left.left = TreeNode(val=4) 
Root.left.left.left = TreeNode(val=5)  
Root.right.left = TreeNode(val=6) 
Root.right.right = TreeNode(val=7) 
Root.right.right.left = TreeNode(val=8) 



def preorder(root): 
    
    stack = [] 
    stack.append(root) 
    pre_order = [] 
    
    while stack : 
        
        node = stack.pop() 
        pre_order.append(node.val) 
        
        if node.right : stack.append(node.right)     
        if node.left : stack.append(node.left) 
        
    return pre_order

print(f"Preorder : {preorder(Root)}") 


def inorder(root): 
    
    stack = [] 
    cur = root 
    inorder = [] 
    
    while cur or stack : 
        
        if cur : 
            stack.append(cur) 
            cur = cur.left 
        else : 
            if not stack : break 
            else : 
                cur = stack.pop() 
                inorder.append(cur.val) 
                cur = cur.right 
                
    return inorder

print(f"Inorder: {inorder(Root)}") 


def postorder(root): 
    
    stack = [] 
    stack.append(root) 
    post_order = [] 
    
    while stack: 
        
        node = stack[-1]  
        if not node.left and not node.right : 
            stack.pop()
            post_order.append(node.val)

        if node.right : stack.append(node.right) 
        if node.left : stack.append(node.left) 
        
        node.left = None 
        node.right = None 
    
    return post_order

# print(f"Postorder: {postorder(Root)}") 

def postorder_with_memo(root): 
    
    stack = [] 
    stack.append(root) 
    post_order = [] 
    memo = set() 
    
    while stack: 
        
        node = stack[-1]  
        if node in memo : 
            stack.pop()
            post_order.append(node.val)
            continue

        if node.right : stack.append(node.right) 
        if node.left : stack.append(node.left) 
        
        memo.add(node) 
        
    
    return post_order

print(f"Postorder with memo: {postorder_with_memo(Root)}") 