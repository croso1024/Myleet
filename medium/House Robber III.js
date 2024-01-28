/*

    思路 : 
        House Robber的第三版本 , 從array改成給tree
        除了root以外,所有節點都只有且只有一個parent, 不能連續地偷竊相連階層的節點值,求可以拿到的最大金額 

        這一題很炫 , 就是結合了Tree的情況,我們不能連續地偷竊相鄰的兩層 , 
        那這樣看起來,在每一個節點上能做的事情就兩個 
        偷竊該節點並往下走 , 不偷該節點就往下走 

        回想普通House robber的遞推 , 到達該節點時可以偷的最大值等於 該點的值+走到前兩層時的最大值 或 不偷這一點的值 ,等於到前一層的值
        用top-down遞迴+memo來做


*/


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
    解法一. Top-down DP + memo
*/

var rob = function(root) {
    
    let memo = new Map() ; 

    // dp函數的定義為以該節點為root,
    // 分別在有選與不選的情況下可以得到的最大收益

    const dp = function(node){

        if (node == null){return [0 , 0]}
        else if ( memo.has(node)  ){return memo.get(node)}   

        // 在post-order位置做操作 , 可以選的只有兩種 
        const [left_profit_have , left_profit_not] = dp(node.left)  ; 
        const [right_profit_have , right_profit_not] = dp(node.right) ; 

        // 如果有選自己 
        const profit_have = node.val + left_profit_not + right_profit_not ; 
        // 如果沒選自己
        const profit_not = Math.max(
            left_profit_have + right_profit_have ,
            left_profit_have + right_profit_not , 
            left_profit_not + right_profit_have ,
            left_profit_not + right_profit_not , 
            ) ; 

        memo.set(node , [profit_have,profit_not]) ; 

        return [profit_have , profit_not] ; 
    }

    return Math.max(...dp(root)) ; 

};


// 解法二. 修改DP函數定義

var rob = function(root) {
    
    let memo = new Map() ; 

    // dp函數的定義為以該節點為root,
    // 可以得到的最大收益

    const dp = function(node){

        if (node == null){return 0 }
        else if ( memo.has(node)  ){return memo.get(node)}   

        // 如果有選自己 
        const profit_have = node.val + ((node.left == null)?  0 : dp(node.left.left) + dp(node.left.right))   + ((node.right == null)? 0 : dp(node.right.left) + dp(node.right.right)) ; 

        // 沒選自己 
        const profit_not = dp(node.left) + dp(node.right) ; 


        console.log(node.val , profit_have , profit_not)


        const res = Math.max(profit_have , profit_not) ; 


        memo.set(node , res) ; 
        return res 
    }

    return dp(root) ; 

};