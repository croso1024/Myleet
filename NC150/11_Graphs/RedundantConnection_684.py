"""
    題意 :
    一棵樹是連通、而且沒有環的無向圖。
    這張圖一開始是 n 個節點(編號 1 到 n)的樹,之後多加了一條原本不存在的邊。
    edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條邊。edges 的長度就是 n。

    回傳一條可以刪掉的邊,刪掉之後剩下的圖仍是一棵 n 個節點的樹。
    若有多條邊都可以刪,回傳在 edges 裡出現得最晚的那一條。

    LeetCode 684 · Medium
    URL : https://leetcode.com/problems/redundant-connection/

    Example :
    edges = [[1,2],[1,3],[2,3]]                 -> [2,3]
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]     -> [1,4]

    Constraint :
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= n
    沒有重複的邊
    給定的圖是連通的

    思路 :
    這一題是找出那條 , 要加上之前,要連接的兩塊就已經互相連通的情況. 
    題目給定的範例1, 就符合多條可刪,但要刪掉最後一條要加的.
    而題目也給定 , 這張圖本來就是所有節點都相連,因此只有一條是多餘的 ( N個節點至少 N-1 條邊才能全連接 , 不可能發生 2 條都是多餘的 , 只會發生多餘的1條可以有不同選擇)

    這一題走 Union-Find 標準模板,即可解 時間 O(N) , 空間 O(N)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class UnionFind : 

    # 配合節點是由編號 1 ~ n , index-0 就不使用
    def __init__(self,n : int): 

        self.union_root = [ i for i in range( n + 1  )] 
        self.union_size = [1 for i in range(n+1)]

    # 做路徑壓縮 
    def find(self,x : int): 

        parent = self.union_root[x] 
        while parent != self.union_root[parent] : 

            self.union_root[parent] = self.union_root[ self.union_root[parent] ]
            parent = self.union_root[parent]
        
        return parent
    
    def union(self,p : int , q : int):
        
        root_p = self.find(p)
        root_q = self.find(q) 

        if root_p == root_q : return 

        if self.union_size[root_p] > self.union_size[root_q] : 
            self.union_root[root_q] = root_p 
            self.union_size[root_p] += self.union_size[root_q]
        
        else : 
            self.union_root[root_p] = root_q 
            self.union_size[root_q] += self.union_size[root_p] 


    def is_connected(self , p: int , q:int) : 
        
        return self.find(p) == self.find(q)



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # 這一題要的 , 就是找出第一組 , 在加入 edges 發現兩個目標早已經連通的狀況 : 
        # Given N = len(edges) 
        union_find = UnionFind(n = len(edges))  
        for ai , bi in edges : 
            if union_find.is_connected(ai,bi) : 
                return [ai,bi] 
            union_find.union(ai,bi) 
        return -1 


if __name__ == "__main__":
    c = Solution()

    # (edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        ([[1, 2], [1, 3], [2, 3]], [2, 3], "官方範例:三角形,最後一條邊成環"),
        (
            [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
            [1, 4],
            "官方範例:環在前四條,5 是掛在外面的葉子",
        ),
        ([[1, 2], [2, 3], [1, 3]], [1, 3], "三個節點,多餘的邊剛好是最後一條"),
        (
            [[1, 2], [2, 3], [1, 3], [3, 4]],
            [1, 3],
            "多餘的邊不是陣列最後一條,後面還有一條必須留的樹邊",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]],
            [4, 1],
            "四節點的環,答案是環上最晚出現的邊,不是整份輸入的最後一條",
        ),
        (
            [[1, 2], [1, 3], [1, 4], [2, 3]],
            [2, 3],
            "1 分岔到 2、3、4,只有 2 和 3 之間多了一條邊",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [2, 4], [4, 5]],
            [2, 4],
            "環在中段,左右各有一條必須留的邊",
        ),
        (
            [[2, 3], [1, 2], [1, 3], [1, 4], [4, 5]],
            [1, 3],
            "環上的三條邊不是依編號排,要回傳輸入裡最晚的那條",
        ),
        (
            [[1, 2], [2, 3], [3, 4], [1, 4]],
            [1, 4],
            "四個節點剛好四條邊,整圈都在環上,答案是最後一條",
        ),
    ]

    for edges, expected, note in test_set:
        result = c.findRedundantConnection([edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
