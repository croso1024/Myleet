/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * 
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */


// flag approach , cost O(1) space + O(N) time for recursion traverse 
var lowestCommonAncestor = function(root, p, q) {
    
    let solution = null ; 
    // return wheather or not , the P and Q node in this subtree 
    const traverse = (node) =>{
        if (node === null){return [false , false]} 
        
        let [haveP1 , haveQ1] = traverse(node.left) ; 
        let [haveP2 , haveQ2] = traverse(node.right) ; 

        let haveP = (node.val === p.val)? true : haveP1 || haveP2 ; 
        let haveQ = (node.val === q.val)? true : haveQ1 || haveQ2 ; 

        if (haveP && haveQ && solution === null){
            solution = node ; 
            return [true , true]
        }

        return [haveP , haveQ]
    }

    traverse(root) ;
    return solution ; 

};