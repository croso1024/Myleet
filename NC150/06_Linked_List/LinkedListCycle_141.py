"""
    題意 :
    給定單向鏈結串列的頭節點 head,判斷串列中是否存在環(cycle)。
    若某個節點可經由持續跟隨 next 指標再次回到自己,則視為有環。

    LeetCode 141 · Easy
    URL : https://leetcode.com/problems/linked-list-cycle/

    Example :
    head = [3,2,0,-4], pos = 1  -> True
    head = [1,2],      pos = 0  -> True
    head = [1],        pos = -1 -> False

    Constraint :
    節點數量範圍為 [0, 10^4]
    -10^5 <= Node.val <= 10^5
    pos 為 -1,或是串列中某個合法 index(0-based)
    題目保證 pos 若不是 -1,則 tail.next 會指回該 index 的節點

    思路 :
    這一題是經典的快慢標題目 , 檢查Linked list內是否有環這件事. 
    可以用一快一慢,如果快慢會交會,那表示一定有環出現. 
    如果快的走到通 (斷掉), 則表示沒有環. 
    走到通或著交會,時間複雜度都是 O(N)

    複雜度 : Time O(N) / Space O(1)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head 
        fast = head 

        while fast and fast.next : 
            
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast : return True 

        # 走通了,表示無環
        return False 


def build_linked_list(values: List[int], pos: int = -1) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    nodes: List[ListNode] = []
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
        nodes.append(curr)
    if pos >= 0 and nodes:
        curr.next = nodes[pos]
    return dummy.next


if __name__ == "__main__":
    c = Solution()

    # (values, pos, 預期輸出)
    test_set = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),                             # 邊界:空串列
        ([1], 0, True),                              # 邊界:單節點自環
        ([1, 2, 3, 4, 5], -1, False),                # 無環的較長串列
        ([1, 2, 3, 4, 5], 4, True),                  # tail 指回自己
        ([-100000, 0, 100000], 1, True),             # 邊界:數值上下限
    ]

    for values, pos, expected in test_set:
        head = build_linked_list(values, pos)
        result = c.hasCycle(head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} pos={pos} | expected={expected} | got={result}")
