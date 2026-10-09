"""
    題意 :
    給定一張連通無向圖裡某個節點的參考。
    回傳這張圖的 deep copy。

    每個節點有一個整數 val,以及 neighbors(相鄰節點的 list)。
    圖裡沒有自環、沒有重複邊。每個節點的 val 都不一樣,而且等於它的編號(從 1 開始)。
    傳進來的 node 一定是 val == 1 的那個節點。圖是空的時,node 為 null。

    複製後要有同樣數量的新節點。
    val 與鄰居關係都要對上,而且任何指標都不得指回原圖的節點。

    測試用 adjacency list 表示整張圖。
    adjList[i] 是 val == i + 1 這個節點的鄰居編號。
    鄰居在 list 裡的順序不影響對錯。

    LeetCode 133 · Medium
    URL : https://leetcode.com/problems/clone-graph/

    Example :
    adjList = [[2,4],[1,3],[2,4],[1,3]] -> [[2,4],[1,3],[2,4],[1,3]]
    adjList = [[]]                      -> [[]]
    adjList = []                        -> []

    Constraint :
    節點數在 [0, 100]
    1 <= Node.val <= 100
    Node.val 互不相同
    沒有重複邊,也沒有自環
    圖是連通的,從給定節點可以走到每一個節點

    思路 :
    這一題實際上給的輸入為 node , 而不是 adjacency list , 
    而直覺上這題和 Copy Linked List 很像 , 
    需要走訪一次所有節點 , 複製一個節點Copy , 
    
    Given all nodes in the graph are unique. 
    這一題的細節就剩下對使用的節點的把控 , 要正確的用複製品/正品


    複雜度 : 
    時間複雜度 / 空間複雜度為 O(N)

    


    Trade-off :

"""

from typing import List, Optional , Dict 


class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[List[Node]]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Optional[Node]") -> "Optional[Node]":
        if node is None : return None

        # Store the clone node 
        clone_node_map : Dict[int , Node] = {}
        def copy(node : Node) -> Node : return Node(val = node.val)

        # DFS / BFS , use DFS here . 
        # Given at lease one node.
        # Use copy map as visited set 
        stack = [node] 
        head = copy(node) 
        clone_node_map[node.val] = head 

        while stack : 

            cur = stack.pop() 

            for neighbor in cur.neighbors : 
                # 已經出現在複製Map當中的 , 就不再尋訪.且不用複製
                if neighbor.val in clone_node_map : 
                    pass 
                
                # 第一次看到的節點就要複製一顆 ,　然後丟回 DFS ,
                else : 
                    clone = copy(neighbor) 
                    clone_node_map[neighbor.val] = clone 

                    # stack 內部是放原始節點, 原始節點才有 Edge 
                    stack.append(neighbor)  

                # 無論是否是第一次看到的 , 都需要將複製品接回去
                # cur 必然已經出現在 clone map , 需要將 clone map 裡對應 cur 的那顆節點也串接上複製好的 neighbor
                clone_node_map[cur.val].neighbors.append(clone_node_map[neighbor.val]) 
        
        return head 


def build(adj: List[List[int]]) -> Optional[Node]:
    """adjacency list 的第 i 列是 val == i + 1 的鄰居。空 list 代表空圖。"""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbor_vals in enumerate(adj):
        nodes[i].neighbors = [nodes[val - 1] for val in neighbor_vals]
    return nodes[0]


def to_adj(node: Optional[Node]) -> List[List[int]]:
    """走訪整張圖,依 val 排成 adjacency list。鄰居編號排序後再比。"""
    if node is None:
        return []
    found = {}
    stack = [node]
    found[node.val] = node
    while stack:
        cur = stack.pop()
        for neighbor in cur.neighbors:
            if neighbor.val not in found:
                found[neighbor.val] = neighbor
                stack.append(neighbor)
    return [
        sorted(neighbor.val for neighbor in found[val].neighbors)
        for val in range(1, len(found) + 1)
    ]


def shares_node(original: Optional[Node], copied: Optional[Node]) -> bool:
    """複製圖裡只要出現原圖的節點,就不是 deep copy。"""
    if original is None or copied is None:
        return False
    return bool(set(collect_ids(original)) & set(collect_ids(copied)))


def collect_ids(node: Node) -> List[int]:
    seen = set()
    stack = [node]
    seen.add(id(node))
    while stack:
        cur = stack.pop()
        for neighbor in cur.neighbors:
            if id(neighbor) not in seen:
                seen.add(id(neighbor))
                stack.append(neighbor)
    return list(seen)


if __name__ == "__main__":
    c = Solution()

    # (adjList, 預期, 說明)
    # 另檢查:原圖沒有被改掉,而且複製後的節點沒有與原圖共用
    test_set = [
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            "官方範例:四個節點的環,每個點連兩個鄰居",
        ),
        ([[]], [[]], "官方範例:只有一個節點,沒有鄰居"),
        ([], [], "官方範例:空圖"),
        ([[2], [1]], [[2], [1]], "兩個節點互相連接"),
        ([[2], [1, 3], [2]], [[2], [1, 3], [2]], "三個節點排成一條線"),
        (
            [[2, 3], [1, 3], [1, 2]],
            [[2, 3], [1, 3], [1, 2]],
            "三角形,每個點都連另外兩個",
        ),
        (
            [[2, 3, 4], [1], [1], [1]],
            [[2, 3, 4], [1], [1], [1]],
            "星形:1 連到 2、3、4,其餘都只連回 1",
        ),
        (
            [[2], [1, 3], [2, 4], [3]],
            [[2], [1, 3], [2, 4], [3]],
            "四個節點排成一條線",
        ),
        (
            [[2, 3], [1, 3], [1, 2, 4], [3]],
            [[2, 3], [1, 3], [1, 2, 4], [3]],
            "三角形再從 3 拉出一條到 4",
        ),
    ]

    for adj, expected, note in test_set:
        root = build(adj)
        cloned = c.cloneGraph(root)
        result = to_adj(cloned)
        original_after = to_adj(root)
        shared = shares_node(root, cloned)
        passed = result == expected and original_after == expected and not shared
        status = "Pass" if passed else "Failed"
        print(f"{status} | {note}")
        print(f"       expected={expected}")
        print(f"       got     ={result} | shared={shared}")
