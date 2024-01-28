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
 * @return {boolean}
 */


/*
    這題的玄機在於 , 除了child對節點本身要滿足的大小關係以外 , 他還必須要大於其上源的節點 
    藉著example的圖片可以去觀察 , 我們會在往左右探索的同時去限縮一個區間 ,所有節點必須在區間之內
    用traverse的方式走訪 , maintain這個有效區間
*/
var isValidBST = function(root) {
    
    let valid = true ; 
    // l , r mean the effect value range of the node must be obey 
    const validNode = function(node , l , r){

        if (node == null || !valid){return  ;}

        else if (node.val <= l || node.val >= r){
            valid=false ; 
            return 
        }

        // 往left child走得時候 , 更新right bound 
        // 往right child走的時候 , 更新left bound 
        validNode( node.left  , l  ,  Math.min(r , node.val ));
        validNode(node.right ,  Math.max(l , node.val) , r ) ; 

    }

    validNode(root , Number.MIN_SAFE_INTEGER , Number.MAX_SAFE_INTEGER) ; 

    return valid ; 
};