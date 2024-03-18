/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if (!preorder.length > 0){return null}

    const root = new TreeNode( val = preorder[0] ) ;
    const indexOfRoot = inorder.indexOf(root.val) ; 
    // indexOfRoot = how many node in left sub-tree , and the rest is belong to right sub-tree 
    const leftTree = buildTree( preorder.slice( 1 , 1+indexOfRoot ) , inorder.slice(0 ,indexOfRoot)   )

    const rightTree = buildTree( preorder.slice(1+indexOfRoot) , inorder.slice( indexOfRoot+1 ) )

    root.left = leftTree
    root.right = rightTree 

    return root 

};