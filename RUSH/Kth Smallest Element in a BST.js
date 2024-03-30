/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    
    let number = 1
    let solution = null ; 
    const inorder = node =>{
        if (node === null || solution !== null){return null}

        inorder(node.left)

        if (number === k){solution = node.val}
        number += 1 ; 

        inorder(node.right) 
    }
    inorder(root)
    return solution ; 

};


var kthSmallest = function(root, k) {
    
    let stack = [] ; 
    let cur = root ; 
    number = 0 ; 

    while (cur !== null || stack.length >0){

        if (cur !== null){
            stack.push(cur) ; 
            cur = cur.left ; 
        }
        else{

            cur = stack.pop() ;
            number += 1 
            if (number === k){return cur.val}
            cur = cur.right 

        }
    }

};
