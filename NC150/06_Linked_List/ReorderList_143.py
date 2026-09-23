"""
    題意 :
    給定單向鏈結串列的頭節點 head,將節點依「頭、尾、次頭、次尾 …」交錯重排。
    必須原地修改,不可回傳新串列。

    以 n 個節點 L0 → L1 → … → Ln-1 為例,重排後應為:
    L0 → Ln-1 → L1 → Ln-2 → L2 → …

    LeetCode 143 · Medium
    URL : https://leetcode.com/problems/reorder-list/

    Example :
    head = [1,2,3,4]   -> [1,4,2,3]
    head = [1,2,3,4,5] -> [1,5,2,4,3]

    Constraint :
    節點數量範圍為 [1, 5 * 10^4]
    1 <= Node.val <= 1000

    思路 :

    要頭/尾交替排 , 最直覺想法是一個 Array 儲存這些 node , 這樣就有順序.
    然後雙指標左右向內縮 , 串起全部. 
    這個方案時間複雜度 O(N) , 空間O(N).
    
    複雜度 : Time O(N) / Space O(N)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        container : List[ListNode] = [] 
        probe = head 
        while probe : 
            container.append(probe)
            probe = probe.next 
        
        left , right = 0 , len(container) - 1 
        if len(container) <= 1 : return 

        # 串接的起點 
        cur = "left"

        while left < right : 

            left_node = container[left]
            right_node = container[right] 

            if cur == "left" : 
                left_node.next = right_node 
                right_node.next = None 
                left += 1 
                cur = "right"

            elif cur == "right" : 
                right_node.next = left_node 
                left_node.next = None 
                right -= 1 
                cur = "left"
        
        return 


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

    # (輸入 list, 預期輸出 list)
    test_set = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1], [1]),                                  # 邊界:單一節點
        ([1, 2], [1, 2]),                            # 邊界:兩個節點,順序不變
        ([1, 2, 3], [1, 3, 2]),                      # 奇數長度
        ([7, 7, 7, 7], [7, 7, 7, 7]),                # 全部節點值相同
        (list(range(1, 11)), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),
    ]

    for values, expected in test_set:
        head = build_linked_list(values)
        c.reorderList(head)
        result = linked_list_to_list(head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} | expected={expected} | got={result}")
