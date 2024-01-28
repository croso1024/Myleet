/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */


var mergeTwoLists = function(list1, list2) {

    let newHead = new ListNode() ; 
    let ref = newHead ; 


    while ((list1 != null)  && (list2 != null)){

        if (list1.val < list2.val){
            newHead.next = list1 ; 
            list1 = list1.next ; 
            newHead = newHead.next  ;
        }
        else {
            newHead.next = list2 ; 
            list2 = list2.next ; 
            newHead = newHead.next ; 
        }
        
    }

    // list1 or list2 point to the null 

    while (list1 != null){
        newHead.next = list1 ; 
        list1 = list1.next ; 
        newHead = newHead.next ; 
    }

    while (list2 != null){
        newHead.next = list2 ; 
        list2 = list2.next ; 
        newHead = newHead.next ; 
    }
    return ref.next ; 

};