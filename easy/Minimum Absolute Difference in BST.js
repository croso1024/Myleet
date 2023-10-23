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
    思路 :
        這題要我們求取BST樹中任意兩個節點的最小差值 ,直覺上就能想到post-order
        最小差值會發生在 min( 當前節點-左子最大 , 右子最小-當前節點  ) 
        利用post-order去走整棵樹計算上面那個式就結束

        解法一. post-order 去track左右子樹的極值並更新 -> 慢,複雜 ,操作多
        解法二. inOrder加入arr , 之後linear的走array計算min diff -> O(N)時間和空間 ,還不夠好 
        解法三. inOrder順序本質上就是sorted , 直接比較尋訪過程的前後節點計算min diff -> 最好

        可能今天狀態不好或是太久沒有寫tree , 居然直接忘了這一點
*/

/*
    解法一. 就是上述的Recursion + post-order思路 , 
        實際做起來發現說我一開始忽略了要maintain子樹的最小值與最大值這件事 , 
        這會讓操作變得更多一點導致time,space都不是很優
*/


var getMinimumDifference = function(root) {
    
    let best = Infinity ; 
    // 函數回傳該節點之下的最大&最小值用來計算 
    let computeDifference = node => {
        if (node == null) {return [node , null , null]}

        // 要在post-order位置操作 
        let [left_child , l_min , l_max] = computeDifference(node.left) ; 
        let [right_child , r_min , r_max] = computeDifference(node.right) ;

        // 如果left_child 不是null 
        if (left_child != null) {
            best = Math.min( best ,  node.val-l_max );
            l_min = Math.min(node.val , l_min) ;
            l_max = Math.max(node.val , l_max) ; 
        }
        else {
            l_min = node.val  ;
        }

        if (right_child != null){
            best = Math.min( best , r_max - node.val  );
            r_min = Math.min(node.val ,r_min) ; 
            r_max = Math.max(node.val ,r_max) ; 
        }
        else {
            r_max = node.val
        }
        // 回傳以該節點為子樹的最大與最小
        return [node , l_min , r_max]
    }

    computeDifference(root) ; 
    return best ; 

};



/*
    解法二 . in-order traverse + array計算diff
    這個作法在速度上應該可以很快,只是空間不佳
*/

var getMinimumDifference = function(root) {

    let arr = [] ; 
    let inOrder = function(node) {
        if (node == null) {return node} 
        inOrder(node.left) ; 
        arr.push(node.val); 
        inOrder(node.right) ; 
    }
    inOrder(root) ; 

    // 已知至少會有兩個節點 
    let bestDiff = Infinity ; 
    for(let index=0 ; index<arr.length-1 ; index++){
        bestDiff = Math.min(bestDiff , Math.abs(   arr[index] - arr[index+1] )  ) ;
    }
    return bestDiff ; 

}


/*
    解法三. 
        使用in-order的順序尋訪 , 本來就可以得到節點之間的sorted順序 , 
        直接比較前一個inorder探訪的節點和當前就可以了 ,
*/

var getMinimumDifference = function(root) {

    let bestDiff = Infinity ; 
    let prev = null 

    let inOrder = function(node) {
        if (node == null) {return node} 
        inOrder(node.left) ; 
        if (prev != null) {
            bestDiff = Math.min( bestDiff , node.val - prev.val ) ; 
        }
        prev = node ; 
        inOrder(node.right) ; 
    }
    inOrder(root) ; 

    return bestDiff ; 

}