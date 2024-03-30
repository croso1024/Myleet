/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */


// divide & conquer 
var sortedArrayToBST = function(nums) {
    
    const buildTree = (array) => {

        if (array.length ===0) {return null}
        
        let rootIndex = Math.floor( array.length /2 ) ; 
        let rootNode = new TreeNode(val = array[rootIndex])

        let leftSubTree = buildTree(array.slice(0 , rootIndex))
        let rightSubTree = buildTree(array.slice(rootIndex+1))  

        rootNode.left = leftSubTree;
        rootNode.right = rightSubTree ;
        return rootNode ; 
    }
    return buildTree(nums) ; 
};