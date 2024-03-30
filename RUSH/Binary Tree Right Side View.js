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
 * @return {number[]}
 */

// level order traverse , record the last apppear node in every level 
// Perform BFS 
var rightSideView = function(root) {
    
    if (root === null){return []}
    let answer = [] ; 
    let queue = [root] ; 
    
    while (queue.length>0){

        let size = queue.length ; 
        let lastNode = null ; 
        for (let i = 0 ; i < size ; i++){
            lastNode = queue.shift() ;
            if (lastNode.left){queue.push(lastNode.left)}
            if (lastNode.right){queue.push(lastNode.right)}
        }

        answer.push(lastNode.val) ; 
    }
    return answer ; 
};