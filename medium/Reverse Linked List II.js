/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */


/*
    思路 : 
        這題的敘述很簡單 , 就是給一個單向linked list , 要求我們將第left到第right的部份反轉 ,
        其餘保持不變 . 

        就用雙指標去定位要交換的範圍 , 針對該範圍去做反轉 , 接合
        假如要交換 i->j的節點 , 我們要拿著 i-1和j+1 , 之後對i->j做反轉再做接合 

        我覺得寫的有點差 , 邏輯搞的有點過於複雜 .
        
        寫這題的當下狀態不太好 , 需要重複練習 , 另外使用recursion還是有O(N)的複雜度
        因此這一題必須要練習使用for-loop的版本
    
*/

var reverseBetween = function(head, left, right) {

    if (left == right) {return head} 
    let fast = head ; 
    let slow = head ; 
    let node_before_reverse = null ; 
    let node_after_reverse = null ; 

    for (let step=1 ; step < right ; step++){
        fast = fast.next ; 
    } 
    node_after_reverse = fast.next ; 

    for (let step=1 ; step < left ; step++){
        if (step == left-1) {node_before_reverse = slow}
        slow = slow.next ; 
    }

    // 到此 slow,fast , node_before_reverse , node_after_reverse都拿到了 
    // 遞迴的反轉slow -> fast  , 遞迴內的base case直接用right,left , 因為題目考量不會讓我們爆掉

    const reverse = (node , step) => {
        if ((step == right-left) || (node == null) ) {
            return node ; 
        }

        // post-order的位置做反轉
        next_node = reverse(node.next , step+1) ; 
        if (next_node != null){next_node.next = node ; }
        node.next = null 
        return node ;
    }

    last_node = reverse(slow , 0) ; 
    if (node_before_reverse != null) {node_before_reverse.next = fast}
    else {head = fast;}
    if (last_node != null) {last_node.next = node_after_reverse }

    return head ; 
}
