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


/*
    Invert the tree in post-order position 
*/
var invertTree = function(root) {

    if (root == null){return root} 


    let left_child = invertTree(root.left) ; 
    let right_child = invertTree(root.right) ; 

    root.left = right_child ; 
    root.right = left_child ; 
    
    return root ; 

};