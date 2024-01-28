/*
    思路 :  
        這一題要我們依據不同level , 交替的走 LDR , RDL traverse
        直接用一個global變量保存現在的階層數 , 來決定要走哪樣子的尋訪就好 

        --> 實際上用global變量來保存的不是應該走LDR或RDL , 而是要push或unshift進入array
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
 * @return {number[][]}
 */


/*
    解法一. 
        按照上面的思路 , 雖然可以做到依照深度交換尋訪順序 , 但會有出現被添加的順序錯亂的問題 , 
        依據題目的示意 , 我發現可以直接做level-order的traverse , 然後把奇數深度的level反轉就好
*/

var zigzagLevelOrder = function(root) {
    
    // hashmap 用來保存每一個階層的節點值 , 這邊直接用obj , 比較方便做修改
    const hashmap = {};
    let level = 0 ; 

    const traverse = (node )=>{

        if (node == null){return}

        // 這邊做階層的加入節點
        if (hashmap.hasOwnProperty(level)){
            hashmap[level].push(node.val) 
        }
        else {
            hashmap[level] = [node.val]
        }

        // 接下來做修改深度 , 往下遞迴 
        level += 1 ; 
        traverse(node.left ) ; 
        traverse(node.right) ; 
        level -= 1 ; 

    }

    traverse(root ) ; 

    let count = 0 ; 
    let sol = [] ; 
    while ( hashmap.hasOwnProperty(count) ){

        if ( count % 2 == 0 ) {
            sol.push(hashmap[count]) ; 
        }
        else {
            hashmap[count].reverse() 
            sol.push(hashmap[count])
        }
        count +=1 
    }

    return sol ; 

};


/*
    解法二. 
        與上面的概念類似 , 但這邊改為在尋訪的過程中用unshift , push並用來增加解
        這個解法在速度上有大幅的提昇
*/
var zigzagLevelOrder = function(root) {
    
    // hashmap 用來保存每一個階層的節點值 , 這邊直接用obj , 比較方便做修改
    const hashmap = {};
    let level = 0 ; 

    const traverse = (node )=>{

        if (node == null){return}

        // 這邊做階層的加入節點
        if (hashmap.hasOwnProperty(level)){
            if (level % 2 == 0 ) {
                hashmap[level].push(node.val)     
            }
            else {
                hashmap[level].unshift(node.val)
            }
        }
        else {
            hashmap[level] = [node.val]
        }

        // 接下來做修改深度 , 往下遞迴 
        level += 1 ; 
        traverse(node.left ) ; 
        traverse(node.right) ; 
        level -= 1 ; 

    }

    traverse(root ) ; 
    let count = 0 ; 
    let sol = [] ; 
    while ( hashmap.hasOwnProperty(count) ){

        sol.push(hashmap[count]) ; 
        count +=1 
    }

    return sol ; 

};

/*
    解法三. BFS做階層尋訪 , 透過外部的level變數來決定被加入的方向 
    這個解法在速度與空間都完勝上面解一解二 , 應該是最佳解了
*/

var zigzagLevelOrder = function(root) {

    const sol = [] ; 
    const queue = [] ; 

    if (root == null){return [];}
    queue.push(root) ; 

    let level = 0 ; 

    while ( queue.length > 0 ) {

        const size = queue.length ; 
        // temp , 用來暫存這一層的內容
        const temp = [] ; 
        for (let idx = 0 ; idx < size ; idx++){

            const cur_node = queue.shift() ; 
            if (level %2 == 0){
                temp.push(cur_node.val);
            }
            else {
                temp.unshift(cur_node.val)
            }

            if (cur_node.left != null) {queue.push(cur_node.left)}
            if (cur_node.right != null) {queue.push(cur_node.right)}
        }
        // 走訪完了一個層級 
        level += 1 ;
        sol.push(temp); 

    }

    return sol ; 

}