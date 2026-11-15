"""
    題意 :
    給定一個包含 n 個節點的無向圖（節點編號 0 到 n - 1），以及邊列表 edges，
    其中 edges[i] = [ai, bi] 表示節點 ai 與 bi 之間有一條無向邊。

    回傳這張圖中連通分量（connected components）的總數。

    LeetCode 323 · Medium
    URL : https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

    Example :
    n = 5, edges = [[0,1],[1,2],[3,4]]          -> 2
    n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]    -> 1

    Constraint :
    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    沒有重複的邊

    思路 :
    標準 Union-Find 模板題,建構 Union-Find 本體需要 O(N) 時間與空間. 
    後續的 union / is_connected 操作都是 O(1)

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List


class UnionFind : 

    def __init__(self , n : int): 
        # 初始的連通分量數等同節點數 
        self.count = n 
        # 每個節點初始的 union 塊 root 
        self.union_root = [i for i in range(n)] 
        # 每個節點所在的 union 塊的節點總數
        self.union_size = [1 for i in range(n)] 

    # 連接 p / q 所在的 union
    def union(self, p : int , q : int): 

        root_p : int = self.find_root(p) 
        root_q : int = self.find_root(q) 

        if root_p == root_q : return 

        # 如果兩個所在連通分量 Union 不同才做合併.把 size 小的合併到 size 大的
        if self.union_size[root_p] > self.union_size[root_q] :
            self.union_root[root_q] = root_p 
            # 只要更新 root_p , 因為 root_q 已經被吞了,後面也只用得到 root_p 的 size 
            self.union_size[root_p] += self.union_size[root_q] 
        else : 
            self.union_root[root_p] = root_q 
            self.union_size[root_q] += self.union_size[root_p] 
        
        self.count -= 1 
        
        return 
    
    # 判斷 p / q 是否相連 : 
    def is_connected(self , p : int , q : int) : 
        root_p : int = self.find_root(p) 
        root_q : int = self.find_root(q) 
        return root_p == root_q 

    # 核心操作 , 查詢某個節點的 root , 順手作路徑壓縮 
    # def find_root(self, p : int): 
    #     parent = p 
    #     # 當目標節點的 parent 不是自己, 就要往上找 
    #     while parent != self.union_root[parent]  : 
    #         self.union_root[parent] = self.union_root[self.union_root[parent]]
    #         parent = self.union_root[parent] 
    #     return self.union_root[parent]
    def find_root(self,p:int): 

        path = [] 
        cur = p 
        while  cur != self.union_root[cur] : 
            path.append(cur) 
            cur = self.union_root[cur] 
        
        # 完成後 cur 停在 root 
        for i in path : 
            self.union_root[i] = cur 
        return cur

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        union_find = UnionFind(n) 
        for edge in edges : 
            union_find.union(edge[0],edge[1])
        return union_find.count



if __name__ == "__main__":
    c = Solution()

    # (n, edges, 預期, 說明)
    # 每次呼叫都複製 edges,實作改到測資本身不會留到下一題
    test_set = [
        (5, [[0, 1], [1, 2], [3, 4]], 2, "官方範例:{0,1,2} 與 {3,4} 共 2 個分量"),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1, "官方範例:全部串成 1 個分量"),
        (1, [], 1, "單一節點無邊,共 1 個分量"),
        (4, [], 4, "完全無邊,每個節點各自為獨立分量"),
        (
            6,
            [[0, 1], [1, 2], [3, 4]],
            3,
            "包含孤立節點 5,共有 {0,1,2}, {3,4}, {5}",
        ),
        (
            4,
            [[0, 1], [1, 2], [2, 0]],
            2,
            "分量內有環:多餘的邊不應重複減少分量數,答案應為 {0,1,2} 與 {3}",
        ),
        (
            4,
            [[0, 1], [2, 3], [1, 2]],
            1,
            "先各自連通後再由橋邊 [1,2] 合併為單一分量",
        ),
        (5, [[0, 4]], 4, "只有一條邊連接頭尾,其餘 3 點各自獨立"),
    ]

    for n, edges, expected, note in test_set:
        result = c.countComponents(n, [edge[:] for edge in edges])
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result}")
