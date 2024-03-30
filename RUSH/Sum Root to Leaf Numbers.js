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
var sumNumbers = function(root) {
    
    let solution = 0 ; 

    const traverse = (node ,acc)=> {
        if (node === null){return}

        //leaf
        if (node.left === null && node.right === null){
            solution += Number(   acc + node.val.toString()  )
            return
        }

        traverse(node.left , acc + node.val.toString()  )
        traverse(node.right , acc + node.val.toString()  )
    }

    traverse(root ,"");


    return solution

};