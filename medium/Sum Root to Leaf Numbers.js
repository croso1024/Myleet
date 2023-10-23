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


/*
    這一題的思路基本上就在pre-order, post-order位置操作累積值 ,
    在leaf時對外部變數做修正即可 . 非常接近於BackTrack結構 
    
    主要的差異點在於因為是要處理JS的字串轉數字 , 比較生疏
*/

var sumNumbers = function(root) {

    let result = 0 ; 

    let traverse = function(node , temp) {

        if (node == null) {return} 

        // react the leaf
        if (node.left == null && node.right == null) {
            path_sum = "" ;
            for (let element of temp) {
                path_sum += String(element) ; 
            }
            result += Number(path_sum) ; 
            return 
        }

        if (node.left != null) {
            
            temp.push(node.left.val);
            traverse(node.left , temp ) ;
            temp.pop();

        }

        if (node.right != null) {

            temp.push(node.right.val);
            traverse(node.right, temp);
            temp.pop();
        }

    }

    traverse(root , [root.val]) ; 

    return result ; 

};