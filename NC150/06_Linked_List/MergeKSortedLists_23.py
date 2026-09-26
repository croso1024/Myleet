"""
    題意 :
    給定 k 條已排序(升序)的單向鏈結串列,組成一個陣列 lists。
    將它們合併成一條升序鏈結串列,並回傳合併後的頭節點。

    LeetCode 23 · Hard
    URL : https://leetcode.com/problems/merge-k-sorted-lists/

    Example :
    lists = [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
    lists = []                      -> []
    lists = [[]]                    -> []

    Constraint :
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] 為升序
    所有 lists[i].length 的總和不會超過 10^4

    思路 :

    覺得這一題和 Merged 2 Sorted List 類似,
    只是這一次要改為合併更多條,直覺的想法是改用某個容器儲存還能比較的Linked List即可.
    需要有個機制去剔除已經不可比較的 Linked List 才行. 

    已知 lists[i].length 總和不會超過 10^4 , 
    如果每一次比較 , 都要比較K次. ,單條最多又500個節點.
    可能要考量一下時間複雜度會不會爆炸.

    # 此處有在思考, 題目是不是有打算要求我們用 Binary Search 快速定位要用哪條 Linked List , 但我們不能保證某條　Linked List 的頭被接上後,下一個的數值.
    # 因此如果要走 Binary Search , 勢必還要得處理重新Sorting的機制 

    # 已知總節點數在 10^4 量級 , K條數就是在 10^4 量級. 而每條最多500節點.
    # 因此最壞的情況就是比較 10^4 條後才能選擇一個節點. 這樣思考感覺時間複雜度必定爆炸. 

    思考後再想有沒有辦法用 Heap , 維護一個min_heap , 每次從 heap 頂端拿一個最小值得 Linked List 出來用.
    用完之後更新值 , 重新丟回 Heap. 

    因此實際的時間複雜度 : 
    設 N = LinkedList數量,也是總節點數量量級
    1. 建立 Heap , 共 10^4條 O(NlogN) 
    2. 每一次找最小值 O(logN) ,串接O(1)
    3. 串接完成更新回去 O(logN)  
    看起來此方案比較合理 , 總時間複雜度應該在  O(NlogN) 

    複雜度 : Time O(NlogN) / O(LlogL) , N為總節點數量,Linked List數量 / Space : O(L)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next

from typing import List  , Dict  , Tuple 
from heapq import heappop , heappush

class Item : 

    def __init__(self, val : int , linked_list : ListNode ):
        self.val = val 
        self.linked_list = linked_list 
    
    def __eq__(self,other : ListNode):
        return self.val == other.val
    def __gt__(self,other: ListNode):
        return self.val > other.val 
    def __lt__(self,other:ListNode) : 
        return self.val < other.val 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        # 使用 heap 來管理所有 Linked List 
        heap : List[Item] = []

        # 結構體使用 [ node_val , node ] : 
        for list_head in lists : 
            if list_head is None : continue
            heappush(
                heap , Item(val=list_head.val , linked_list=list_head)
            )

        dummy_node = ListNode() 
        cur = dummy_node

        # 只要任何一個Linked List 還有值 ( heap 存在 ) 
        while heap : 

            list_item : Item = heappop(heap)  
            list_head = list_item.linked_list

            cur.next = list_head
            cur = cur.next 
            list_head = list_head.next 

            if list_head is not None :
                heappush(heap , Item(val=list_head.val , linked_list=list_head))
        
        return dummy_node.next 



def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    c = Solution()

    # (lists 的各條串列, 預期輸出 list)
    test_set = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),                                            # 邊界:沒有任何串列
        ([[]], []),                                          # 邊界:只有一條空串列
        ([[1, 2, 3]], [1, 2, 3]),                            # 只有一條串列
        ([[], [1]], [1]),                                    # 空串列與非空串列混在一起
        ([[1], [1], [1]], [1, 1, 1]),                        # 全部相同值
        ([[-10, -1], [-5, 0], [2]], [-10, -5, -1, 0, 2]),    # 含負數
        ([[1, 3], [2, 4], [], [5]], [1, 2, 3, 4, 5]),        # 中間夾一條空串列
        ([[-10000], [10000]], [-10000, 10000]),              # 邊界:數值上下限
    ]

    for groups, expected in test_set:
        lists = [build_linked_list(g) for g in groups]
        result_head = c.mergeKLists(lists)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | lists={groups} | expected={expected} | got={result}")
