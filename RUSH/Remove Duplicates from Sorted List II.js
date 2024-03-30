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
var deleteDuplicates = function(head) {
    
    let solution = new ListNode()
    let solProbe = solution ; 
    let probe = head ; 

    while (probe && probe.next){

        // detect duplicate
        if (probe.val === probe.next.val){
            let refVal = probe.val ; 
            while(probe.next && probe.next.val === refVal){
                probe = probe.next 
            }
            probe = probe.next ;
        }
        else{
            solProbe.next = probe ; 
            solProbe = solProbe.next ;
            
            probe = probe.next ; 
            solProbe.next = null ; 
        }

    }
    if (probe){
        solProbe.next = probe ; 
    }

    return solution.next     
};