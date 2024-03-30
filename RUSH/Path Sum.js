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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    
    let solution = false ; 

    const traverse = (node,acc)=>{

        if (solution){return}
        if (node === null){return null}

        if (node.left === null && node.right === null){
            if (acc + node.val === targetSum){
                solution = true ; 
            }
            return ; 
        }

        if (node.left !== null){
            traverse(node.left , acc + node.val) 
        }
        if (node.right !== null){
            traverse(node.right , acc + node.val) 
        }

    }
    traverse(root , 0 )
    return solution ; 
};