"""
    題意 :
    給定 n 個節點（編號 0 到 n - 1）以及無向邊列表 edges，
    其中 edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條無向邊。

    判斷這些邊所構成的圖是否為一棵「有效的樹 (valid tree)」。
    有效的樹必須同時滿足：
    1. 所有節點連通（只有 1 個連通分量）
    2. 圖中沒有環（acyclic）

    LeetCode 261 · Medium
    URL : https://leetcode.com/problems/graph-valid-tree/

    Example :
    n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]            -> True
    n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]      -> False

    Constraint :
    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    沒有重複的邊

    思路 :

    直接的 Union-Find 題目, 確保在所有 Edge 連接的過程,要相連的兩塊原本都互不相連 ( 否則連接後成為環 )
    同時最後走完 , 連通分量剩下 1 
     

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class UnionFind : 

    def __init__(self,n:int): 

        self.count = n 
        self.union_parent = [i for i in range(n)]
        self.union_size = [1 for i in range(n)] 

    # 找出當前連通分量的 root 
    def find(self,x : int):
        path = [x] 
        parent = self.union_parent[x] 
        while parent != self.union_parent[parent]:
            path.append(parent)
            parent = self.union_parent[parent]
        # 把看到的所有節點 , 都連接回 root
        for node in path  : self.union_parent[node] = parent 
        return parent

    # 連接兩塊分量 , 回傳 boolean 表示是否執行合併 , 沒執行表示原本已經連接
    def union(self, p : int , q : int) -> bool : 

        root_p = self.find(p) 
        root_q = self.find(q) 

        if root_p == root_q : return False 

        if self.union_size[root_p] > self.union_size[root_q] : 
            self.union_parent[root_q] = root_p
            self.union_size[root_p] += self.union_size[root_q] 
        
        else : 
            self.union_parent[root_p] = root_q 
            self.union_size[root_q] += self.union_size[root_p]
        
        self.count -= 1 

        return True 

    def is_connected(self, p : int , q : int): 
        return self.find(p) == self.find(q)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Given N , init union find 
        union_find = UnionFind(n=n) 

        # 開始走edges , 美一條邊加入時 , 都應該要是 union 回傳 True ( 正確連接,而不是已經有連接過 )
        for ai  , bi in edges : 

            if union_find.union(ai,bi) :
                pass 
            # 一旦已經連接過了 , 那就表示有環 , 直接算錯
            else : 
                return False 
        
        # 完成之後,驗證是否所有節點都包含在內

        return union_find.count == 1 

if __name__ == "__main__":
    c = Solution()

    # (n, edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True, "官方範例:連通且無環的樹"),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            False,
            "官方範例:有環 (1-2-3),不是樹",
        ),
        (1, [], True, "單一節點且無邊,本身就是一棵樹"),
        (2, [], False, "兩個節點但無邊,不連通"),
        (4, [[0, 1], [2, 3]], False, "邊數不足且分成兩個連通分量"),
        (
            4,
            [[0, 1], [1, 2], [0, 2]],
            False,
            "陷阱:邊數剛好 n-1,但 0-1-2 成環且節點 3 孤立",
        ),
        (5, [[0, 1], [0, 2], [0, 3], [0, 4]], True, "星狀圖,連通無環"),
        (4, [[0, 1], [1, 2], [2, 3]], True, "鏈狀圖,連通無環"),
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False, "四節點四條邊構成環"),
    ]

    for n, edges, expected, note in test_set:
        result = c.validTree(n, [edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
