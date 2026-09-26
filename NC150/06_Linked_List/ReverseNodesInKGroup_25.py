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
    這一題以K個一組，做反轉 , 在紙上繪個圖.
    我的想法是用快慢標 , 快飆先走個 K 步. 
    接著快慢標就會分別停在一段要被反轉的區間 ( 若快標走到 None則跳出 )

    接著需要一個helper , 反轉快慢標中間的部分LinkedList, 
    反轉完成繼續走K步.




    複雜度 : Time O(?) / Space O(?)

    Trade-off :

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def show_testing_data(head): 

    node_list = []

    while head : 
        node_list.append(head.val)
        head = head.next 
    print(node_list)
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # print(f"Question : {show_testing_data(head) } , k = {k}") 
        # 反轉給定的兩個節點中的節點
        def _reverse_partial_linked_list( partial_head : ListNode , partial_tail : ListNode): 
            prev = None 
            cur = partial_head 
            while cur : 

                next = cur.next 

                if prev is not None : 
                    cur.next = prev 
                else : 
                    cur.next = None 

                if cur == partial_tail : 
                    break 
                
                prev = cur 
                cur = next
            
            # 反轉完成後 , tail 現在才是頭 , head 則視尾
            return partial_tail , partial_head
            
        
        dummy = ListNode() 
        


        # Given K <= len(LinkedList) 
        slow = head 
        fast = head 

        # 先將範圍定在第一組前K節點. 
        for i in range(k-1 ) : fast = fast.next 

        # 反轉完成後 , 第一輪的fast會是新的Head 
        dummy.next = fast 

        group_tail : ListNode|None = None 
        terminate = False 

        # 當快標還在的時候 , 就還可以部分反轉
        while fast and not terminate : 

            next_group_start = fast.next 

            # 反轉當前所在的 slow / fast 段
            # 出來的 partial_head.next 指向 Null, 而且相當於
            # , partial_tail.next 也已經指向反轉的內部了
            partial_head , partial_tail = _reverse_partial_linked_list(slow , fast)  

            if group_tail is not None : 
                group_tail.next = partial_head 
            group_tail = partial_tail

            # 反轉完一段 ,則繼續對 slow / fast 標走k步 : 
            # 這裡一個陷阱 , 那就是 slow / fast 已經在部分反轉的時候 , 被修改了next的參考.
            # 因此在這邊 for i in range(k) , 實際上就會返著走. 
            # 故在每一段反轉開始前,需要先儲存下一段的開頭. 
            if next_group_start :
                slow = next_group_start
                fast = next_group_start 
                for i in range(k-1) : 
                    fast = fast.next 
                    # fast is None , 表示剩餘節點數不足夠反轉 , 直接把剩下的接起來
                    if fast is None : 

                        probe = next_group_start
                        
                        while probe : 
                            group_tail.next = probe 
                            group_tail = probe
                            probe = probe.next 

                        terminate = True 
                        break 
            else : 
                break 
        
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

    # (values, k, 預期輸出 list)
    test_set = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5,6], 3, [3, 2, 1, 6, 5, 4]),
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
