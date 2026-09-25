"""
    題意 :
    給定單向鏈結串列的頭節點 head,以及整數 n,
    刪除「倒數第 n 個」節點,並回傳刪除後的頭節點。

    LeetCode 19 · Medium
    URL : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Example :
    head = [1,2,3,4,5], n = 2 -> [1,2,3,5]
    head = [1],         n = 1 -> []
    head = [1,2],       n = 1 -> [1]

    Constraint :
    節點數量 sz 範圍為 [1, 30]
    0 <= Node.val <= 100
    1 <= n <= sz

    思路 :
    這一題要處理 Linked list 的操作 , "倒數第n" 這件事應該可以透過先讓一個指標提前走n步來達成. 
    已知  n <= sz . 
    假設 
    : sz = 3 , n = 3 , 則走三步後到一個 None , 
    : sz = 3 , n = 1 , 則fast先走一步, 之後一起走到 fast為None時 , 慢標就指向要被砍的節點. 
    為了移除要被砍的節點,我們額外維護一個 prev , 用來橋接

    複雜度 :  Time O(N) , 只要快慢標走一次 , 加上一些橋接工作 / 空間 O(1) , 僅存指標和橋接過程的暫存

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = head 
        fast = head 
        prev = None # Keep a hook 
        
        # Give n <= length( linked_list ) 
        for i in range(n): fast = fast.next 
        
        # 只要 fast 還指向存在的節點 , 就繼續走. 
        while fast : 
            prev = slow 
            slow = slow.next 
            fast = fast.next 
        
        # 跳出後 , 開始橋接整個節點. 

        # prev is not None : 代表要移除的不是第一個節點 , prev 有值. 後續回傳 head 即可
        if prev is not None : 
            prev.next = slow.next 
            return head 
        
        # 若 prev is None , 則表示移除的就是倒數第 sz 個 , 也就是第一個節點. 直接回 head.next 
        else : 
            return head.next 


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

    # (values, n, 預期輸出 list)
    test_set = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),                                # 邊界:刪掉唯一節點
        ([1, 2], 1, [1]),                            # 刪尾巴
        ([1, 2], 2, [2]),                            # 刪頭
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),          # 刪頭,較長串列
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),          # 刪尾巴,較長串列
        ([0, 0, 0], 2, [0, 0]),                      # 節點值相同
    ]

    for values, n, expected in test_set:
        head = build_linked_list(values)
        result_head = c.removeNthFromEnd(head, n)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | input={values} n={n} | expected={expected} | got={result}")
