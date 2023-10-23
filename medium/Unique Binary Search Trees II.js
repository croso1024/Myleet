/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */


/*
    思路 : 
        這一題就用BackTrack去展開 , 為了構建一棵Tree , 
        左分支的節點只能使用小於自身當前節點的 , 右分支則是使用大於的

        結束條件則是當前沒有可以用來建構的節點 , 這一題的關鍵基本上就是控制動作清單 , 以及傳遞可用節點
*/

var generateTrees = function(n) {

    let actions = Array.from( new Array(n) , (x,idx)=>1+idx ); 

    // 回傳一個多組左子樹 , 右子樹 , 透過雙迴圈與root合體 , 
    // 最終回傳的是以res_node可以組成的所有BST !  
    let buildTree = function( res_node ){ 

        if (res_node.length==0) {return [null]}
        let SubTreeSet = [] ; 
        // 窮舉所有可能的左右子樹種類加入陣列中
        for (let [index,node] of res_node.entries()) {

            let left_subTree =  buildTree( res_node.slice(0,index) )  ;  
            let right_subTree =  buildTree ( res_node.slice(index+1) )  ; 

              // 以這些左右子樹建立許多以當前node為root的子樹
            for (let left of left_subTree) {
                for (let right of right_subTree) {
                    SubTreeSet.push(
                        new TreeNode(node , left , right) 
                    )
                }
            }

        }

        return SubTreeSet
    }


    return buildTree( actions  ); 

};


/*
    解法二 . 不是透過res_node ,而是透過剩餘可用的index來做 , 目的是加速,大體框架相同
*/ 

var generateTrees = function(n) {

    let actions = Array.from( new Array(n) , (x,idx)=>1+idx ); 

    // 回傳一個多組左子樹 , 右子樹 , 透過雙迴圈與root合體 , 
    // 最終回傳的是以res_node可以組成的所有BST !  
    let buildTree = function( left_probe , right_probe ){ 

        if ( left_probe > right_probe ) {return [null]}
        let SubTreeSet = [] ; 
        // 窮舉所有可能的左右子樹種類加入陣列中
        for (let start = left_probe ; start < right_probe+1 ; start++ ){

            let left_subTree =  buildTree( left_probe ,  start-1  )  ;  
            let right_subTree =  buildTree ( start+1 , right_probe )  ; 

            // 以這些左右子樹建立許多以當前node為root的子樹
            for (let left of left_subTree) {
                for (let right of right_subTree) {
                    SubTreeSet.push(
                        new TreeNode( start , left , right) 
                    )
                }
            }

        }

        return SubTreeSet
    }


    return buildTree( 1,n ); 

};