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

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


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
