""" 
    思路: 
        這一題要找到指定兩個節的最低共同祖先 , 在這一題裡面允許自己作為自己的祖先 
        
        稍微想一下的思路如下 : 這一題透過traverse的方式來做 , 
        
        往下展開遞迴tree , 一旦遇到目標節點 , 就將至今累積的track先保存下來 
        這樣走完兩顆tree , 我們就有兩條從root到目標的軌跡 
        
        這個軌跡第一個分叉(不同值)的前一個數值就是Lowest  common ancestor 
        
        
        not . 
            1.這兩條軌跡至少有一個節點(root)會是一樣        
            2. 這一題有給說每一個節點的值都是unique
            
        
        
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

""" 
    解法一. 
        基本上就是透過保存Trajectory , 然後對照後求解 , 沒有任何優化

"""
class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        trajectory_p = [] 
        trajectory_q = [] 
        
        # 這一題保存軌跡的時間點基本上在pre-order / in-order / post-order 都可以
        def traverse(node , track): 
            nonlocal trajectory_p , trajectory_q
            if node is None : return 
            
            
            track.append(node.left)
            traverse(node.left , track) 
            track.pop() 
            
            
            # 我在in-order位置對軌跡進行操作 
            if node.val == p.val and not trajectory_p : 
                trajectory_p = list(track)
            if node.val == q.val and not trajectory_q : 
                trajectory_q = list(track)
            
            
            track.append(node.right)
            traverse(node.right , track)
            track.pop()    
        
        traverse(root , [root]) 
        
        # 我們取得兩條軌跡後 , 就看在哪一個值分叉  , 其前一個值就是解
        # 另外兩天軌跡至少root會一樣 , 且至少count >= 1 
        count = min(len(trajectory_p) , len(trajectory_q))
        sol = None 
        
        for i in range(count): 
            if trajectory_q[i].val == trajectory_p[i].val : pass 
            else : 
                sol =  trajectory_p[i-1] 
                break 
        
        # 可能走完loop都一直pass , 代表LCA是較短的軌跡的最後一個元素 
        return sol if not sol is None else trajectory_p[count-1]
                
            
        
""" 
    解法二. 
        嘗試去優化解法一的時間 , 提早剪枝 , 前一個解法透過遞迴去走了所有節點 ,並在節點執行常數操作
        因此Time為O(N) , 但實際上這邊應該可以直接Binary search來找到目標節點 
        兩次Binary search為 2 * O(log n) , 就算存軌跡方式一樣也可以加速不少
        
        -> 改用Binary search比較針對性的去找 , 
        
        雖然可以加速 , 但空間仍然不是非常好 , 我應該是存了兩條完整的路徑 , 也許可以同步search兩個值
"""


class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        # Binary search尋找目標節點的軌跡
        def BS_trajectory( node ,  target ) : 
            
            trajectory = [] 
            while node : 
                
                if node.val > target : 
                    trajectory.append(node) 
                    node = node.left 
                
                elif node.val < target : 
                    trajectory.append(node) 
                    node = node.right
                
                else : 
                    
                    trajectory.append(node) 
                    return trajectory
            
            
            return trajectory
        
        trajectory_p = BS_trajectory(root , p.val)
        trajectory_q = BS_trajectory(root , q.val)
        
        # 我們取得兩條軌跡後 , 就看在哪一個值分叉  , 其前一個值就是解
        # 另外兩天軌跡至少root會一樣 , 且至少count >= 1 
        count = min(len(trajectory_p) , len(trajectory_q))
        sol = None 
        
        for i in range(count): 
            if trajectory_q[i].val == trajectory_p[i].val : pass 
            else : 
                sol =  trajectory_p[i-1] 
                break 
        
        # 可能走完loop都一直pass , 代表LCA是較短的軌跡的最後一個元素 
        return sol if not sol is None else trajectory_p[count-1]
                
            