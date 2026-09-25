"""
    題意 :
    給定單向鏈結串列的頭節點 head,以及正整數 k,
    將節點以每 k 個為一組反轉,並回傳新的頭節點。

    規則:
      - 不足 k 個的最後一組「保持原順序」,不要反轉
      - 只能改節點的 next,不可改 val
      - 只能使用常數額外空間(遞迴的隱性堆疊也不算通過)

    LeetCode 25 · Hard
    URL : https://leetcode.com/problems/reverse-nodes-in-k-group/

    Example :
    head = [1,2,3,4,5], k = 2 -> [2,1,4,3,5]
    head = [1,2,3,4,5], k = 3 -> [3,2,1,4,5]

    Constraint :
    節點數量 n 範圍為 [1, 5000]
    0 <= Node.val <= 1000
    1 <= k <= n

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
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),          # 邊界:k = 1,等於不反轉
        ([1], 1, [1]),                                  # 邊界:單節點
        ([1, 2], 2, [2, 1]),                            # 剛好一組
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),                # 整條剛好一組
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),    # 兩組都剛好滿
        ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),  # 最後一組不足 k
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1]),          # k = n
        ([0, 0, 0, 0], 2, [0, 0, 0, 0]),                # 節點值相同
    ]

    for values, k, expected in test_set:
        head = build_linked_list(values)
        result_head = c.reverseKGroup(head, k)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} k={k} | expected={expected} | got={result}")
