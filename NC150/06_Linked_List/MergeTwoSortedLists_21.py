"""
    題意 :
    給定兩個已排序(升序)的單向鏈結串列 list1、list2,將兩者合併成一個新的、
    同樣升序排列的鏈結串列並回傳其頭節點。新串列須由原本兩個串列的節點「拼接」而成,
    不可另外建立新節點來儲存數值。

    LeetCode 21 · Easy
    URL : https://leetcode.com/problems/merge-two-sorted-lists/

    Example :
    list1 = [1,2,4], list2 = [1,3,4] -> [1,1,2,3,4]
    list1 = [],      list2 = []      -> []
    list1 = [],      list2 = [0]     -> [0]

    Constraint :
    兩個串列的節點總數範圍為 [0, 50]
    -100 <= Node.val <= 100
    list1 與 list2 皆已按非遞減順序排列

    思路 : 
    維護兩條 List 的頭 , 還有一個當前用來縫合它們的Head.
    逐步走訪 / 比較後串接起整條.

    時間複雜度為 O( N1 + N2 ) , 兩條Linked List的長度

    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 is None and list2 is None : return None 
        elif list1 is None : return list2 
        elif list2 is None : return list1 

        head = None 
        cur = None 

        while list1 and list2 : 

            if head is None : 
                
                if list1.val < list2.val : 
                    
                    head = list1 
                    cur = list1 
                    list1 = list1.next 
                else : 
                    head = list2 
                    cur = list2 
                    list2 = list2.next 
                continue
            
            if list1.val < list2.val : 

                cur.next = list1  
                cur = cur.next 
                list1 = list1.next 
            
            else : 
                cur.next = list2 
                cur = cur.next 
                list2 = list2.next 
        
        # 走完後 , 可能剩下 list1 / list2 
        if list1 : 
            cur.next = list1 
        elif list2 : 
            cur.next = list2 
        
        return head 


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 is None and list2 is None : return None 
        elif list1 is None : return list2 
        elif list2 is None : return list1 

        dummy = ListNode() 
        cur = dummy 

        while list1 and list2 : 

            val_1 = list1.val 
            val_2 = list2.val

            if val_1 < val_2 : 
                
                cur.next = list1 
                cur = list1 
                list1 = list1.next 
            
            else : 

                cur.next = list2 
                cur = list2 
                list2 = list2.next 

        if list1 : 
            cur.next = list1 
        if list2 : 
            cur.next = list2 
        
        return dummy.next 



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

    # (list1, list2, 預期輸出 list)
    test_set = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4]),
        ([], [], []),                                     # 邊界:兩者皆空
        ([], [0], [0]),                                   # 邊界:其中一個為空
        ([0], [], [0]),
        ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),              # 全相同值
        ([-100, -50, 0], [-100, 0, 100], [-100, -100, -50, 0, 0, 100]),  # 邊界:數值上下限
        ([1, 3, 5, 7], [2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8]),          # 交錯合併
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),        # 兩串列數值範圍不重疊
    ]

    for l1, l2, expected in test_set:
        head1 = build_linked_list(l1)
        head2 = build_linked_list(l2)
        result_head = c.mergeTwoLists(head1, head2)
        result = linked_list_to_list(result_head)
        passed = result == expected
        status = "Pass" if passed else "Failed"
        print(f"{status} | list1={l1} | list2={l2} | expected={expected} | got={result}")
