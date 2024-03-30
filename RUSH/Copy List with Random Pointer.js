/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */



// naive solution , 走一次linked list , 並且建立新的複製節點做串接 ,之後再走第二次,透過已經建立的hashmap去對照random指向的節點
// 單趟的走法 , 就是正常走, 不論走next或是random都先檢查是否已經在hashmap內
var copyRandomList = function(head) {
    
    if (head === null){return null}
    let hashMap = new Map(); 

    let originProbe = head  ; 
    hashMap.set( originProbe , new Node(val = head.val))
    let copyProbe = hashMap.get(originProbe) ; 
    let sol = copyProbe ; 
    while (originProbe !== null){


        if (originProbe.next  !== null){
            if (!hashMap.has(originProbe.next )){
                    hashMap.set(originProbe.next , new Node( val = originProbe.next.val  ) )
            }
                copyProbe.next = hashMap.get(originProbe.next) ;
        }

        if (originProbe.random !==null){
            if (!hashMap.has(originProbe.random)){
                hashMap.set(originProbe.random , new Node(val = originProbe.random.val)) 
            }
            copyProbe.random = hashMap.get(originProbe.random) ; 
        }

        originProbe = originProbe.next ; 
        copyProbe = copyProbe.next ; 
    }
    return sol 
};