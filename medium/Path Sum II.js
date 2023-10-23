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
 * @param {number} targetSum
 * @return {number[][]}
 */


/*
    思路 :  
        這一題乍看是非常類似做Back Tracking , 使用DFS在下探的過程中紀錄軌跡以及當前的和 
        一旦找到了leaf就比較目前累積的和 , 並視情況將軌跡加入最終解 
*/ 
var pathSum = function(root, targetSum) {
    
    let Solution = new Array();


    function Traverse(node , accumulative , track) {
        if (node == null) { return  }
        // 到達leaf做檢查
        if (node.left == null && node.right == null) {
            
            if (accumulative + node.val == targetSum) {
                console.log("Trigger")
                track.push(node.val);
                Solution.push( Array.from(track));
                track.pop();
            }
            return 
        }

        // 當有child , 更新accumulative , track並傳下去 
        if (node.left) {
            track.push(node.val);
            accumulative = accumulative + node.val;
            Traverse(node.left ,accumulative , track );
            accumulative = accumulative - node.val ;
            track.pop();
        }
        
        if (node.right) {
            track.push(node.val);
            accumulative = accumulative + node.val;
            Traverse(node.right ,accumulative , track );
            accumulative = accumulative - node.val ;
            track.pop();
        }
    }

    Traverse(root , 0 , []);
    return Solution ; 
};