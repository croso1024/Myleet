"""
    題意 :
    給定單向鏈結串列的頭節點 head,以及正整數 k。
    每 k 個節點為一組,將每一組內部的節點反轉,回傳反轉後的頭節點。
    若最後剩下的節點不足 k 個,則保持原樣。

    不得修改節點的值,只能調整節點之間的連結。

    LeetCode 25 · Hard
    URL : https://leetcode.com/problems/reverse-nodes-in-k-group/

    Example :
    head = [1,2,3,4,5], k = 2 -> [2,1,4,3,5]
    head = [1,2,3,4,5], k = 3 -> [3,2,1,4,5]

    Constraint :
    節點數量 n 的範圍為 1 <= k <= n <= 5000
    0 <= Node.val <= 1000

    思路 :
    這一題以K個一組，做反轉




    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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

    # (values, k, 預期輸出 list)
    test_set = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1], 1, [1]),                               # 邊界:單節點,k = 1
        ([1, 2, 3], 1, [1, 2, 3]),                   # k = 1,整條不變
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),             # k = n,整條反轉
        ([1, 2, 3, 4], 2, [2, 1, 4, 3]),             # 長度剛好是 k 的倍數
        ([1, 2, 3, 4, 5, 6], 4, [4, 3, 2, 1, 5, 6]), # 尾端不足一組
        ([0, 1000, 0, 1000], 2, [1000, 0, 1000, 0]), # 邊界:節點值上下限
    ]

    for values, k, expected in test_set:
        head = build_linked_list(values)
        result_head = c.reverseKGroup(head, k)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} k={k} | expected={expected} | got={result}")
