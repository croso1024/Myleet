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
 * @return {number}
 */
var maxDepth = function(root) {
    
    let solution = 0 ;

    const traverse = (node ,depth)=>{

        if (node === null){return}

        solution = Math.max(solution , depth) 

        traverse(node.left , depth+1)
        traverse(node.right , depth + 1 ) 
    }
    traverse(root,  1); 
    return solution ; 

};


var maxDepth = function(root) {
    if (root === null){return 0}

    return 1 + Math.max( maxDepth(root.left) , maxDepth(root.right))
}