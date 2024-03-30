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
var reverseBetween = function(head, left, right) {
    
    let nextHook = null ; 

    const partialReverse = (node , index) =>{
        // given right <= n , so index === right must have a node ;  
        if (index === right){
            // we don't care about nexthook point to null or not ; 
            nextHook = node.next ; 
            return node ; 
        }
        
        let lastNode = partialReverse( node.next , index+1 ) ; 
        node.next.next = node ; 
        node.next = null ; 
        return lastNode ; 
    }

    let probe = head ; 
    let prev = null ; 
    for (let i = 1 ; i < left ; i++){
        prev = probe ; 
        probe = probe.next ;
    }
    let lastNode = partialReverse(probe , left) ; 
    probe.next = nextHook ; 

    if (prev !== null){
        prev.next = lastNode ; 
        return head ; 
    } 
    else {
        return lastNode 
    }

};