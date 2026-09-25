"""
    題意 :
    給定一個陣列 lists,其中 lists[i] 是一條已排序(升序)的單向鏈結串列。
    將這 k 條串列合併成一條同樣升序的串列,並回傳合併後的頭節點。

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
    lists[i] 已按升序排列
    所有 lists[i].length 的總和不超過 10^4

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

    # (k 條串列的值, 預期輸出 list)
    test_set = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),                                              # 邊界:k = 0
        ([[]], []),                                            # 邊界:只有一條空串列
        ([[1]], [1]),                                          # 邊界:單節點
        ([[1, 2, 3]], [1, 2, 3]),                              # k = 1,只需原樣回傳
        ([[], [1]], [1]),                                      # 混有空串列
        ([[], [], []], []),                                    # 全部是空串列
        ([[1], [0]], [0, 1]),                                  # 兩條單節點
        ([[1, 1, 1], [1, 1], [1]], [1, 1, 1, 1, 1, 1]),        # 全相同值
        ([[-10000, -1, 0], [-2, 10000]], [-10000, -2, -1, 0, 10000]),  # 邊界:數值上下限
        ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[5], [1, 2, 3, 4]], [1, 2, 3, 4, 5]),                # 長度差距大
    ]

    for lists_values, expected in test_set:
        lists = [build_linked_list(values) for values in lists_values]
        result_head = c.mergeKLists(lists)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={lists_values} | expected={expected} | got={result}")
