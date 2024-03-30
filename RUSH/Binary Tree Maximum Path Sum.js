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



// recursion - traverse approach 
var maxPathSum = function(root) {
    
    let solution = Number.MIN_SAFE_INTEGER ; 

    // 回傳經過該節點的path的最大值
    const updateMaximum = node =>{

        if (node === null){return 0}

        let leftMaximum = updateMaximum(node.left) ; 
        let rightMaximum = updateMaximum(node.right) ; 

        let maximum = Math.max(leftMaximum +node.val , rightMaximum + node.val , node.val ) 

        solution = Math.max(solution , maximum , leftMaximum+rightMaximum+node.val) ; 

        return maximum ; 

    }

    updateMaximum(root) ; 
    return solution ; 

};