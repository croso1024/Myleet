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
 * @return {TreeNode}
 */

// post-order traverse 
var invertTree = function(root) {
    

    const invert = (node)=>{

        if (node === null) {return node}

        let leftChild = invert(node.left) ; 
        let rightChild = invert(node.right) ; 

        // invert the child 
        node.right = leftChild ; 
        node.left = rightChild ; 
        return node 
    }   

    return invert(root) ; 

};