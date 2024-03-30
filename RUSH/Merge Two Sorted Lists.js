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
    
    let solution = new ListNode() ;  
    let probe = solution ;  

    let l1 = list1 ; 
    let l2 = list2 ; 

    // l1 & l2 pointer to a effect linked list 
    while (l1 && l2){

        if (l1.val <= l2.val){
            probe.next = l1 ; 
            probe = probe.next 
            l1 = l1.next 
        }
        else{
            probe.next = l2 ; 
            probe = probe.next  ; 
            l2 = l2.next ; 
        }
    }

    // l1 === null or l2 === null 
    if (l1 !== null){

        probe.next = l1 ; 

    }
    else{

        probe.next = l2 ; 
        
    }

    return solution.next ; 


};