/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */


/*
    思路 :
        給定了一個Sorted過得Linekd list , 移除這個linked list內重複的元素 ,
        很明顯的使用雙指標來處理 , 當快指標遇到新的元素後才將慢指標連接過去
*/


var deleteDuplicates = function(head) {

    if (head == null) {return head} 

    let slow = head ; 
    let fast = head ; 

    // 只要考慮快指標是否有next 
    while (!fast == null) {

        if (fast.val > slow.val) {

            slow.next = fast  ;  
            slow = fast ; 
        }

        fast = fast.next ; 

    }


    slow = fast ; 
    return head ; 

};

