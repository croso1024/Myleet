/**
 * @param {TreeNode} root
 * @return {number}
 */

/*
    思路 : 
        recursion traverse結束 , 我寫了遞迴,BFS/DFS , 前兩個效果差不多,DFS則是在空間上較優一點
*/

/*
    recursion
*/

var countNodes = function(root) {
    
    let result = 0 ;  

    let traverse = node => {
        if (node == null) {return} 
        else {
            result += 1 
            traverse(node.left) ; 
            traverse(node.right) ; 
            return 
        }

    };

    traverse(root) ; 

    return result ; 

};


/*
    BFS :  
*/

var countNodes = function(root) {

    if (root == null) {return 0 }
    let result = 0 ; 
    let queue = [] ; 
    
    queue.push(root) ; 

    while (queue.length >0) {

        let node = queue.shift() ; 
        result += 1 ; 
        if (node.left !=null) {queue.push(node.left)}
        if (node.right !=null) {queue.push(node.right)}

    }
    return result ; 
};

/*
    DFS :  
*/

var countNodes = function(root) {

    if (root == null) {return 0 }
    let result = 0 ; 
    let stack = [] ; 
    
    stack.push(root) ; 

    while (stack.length >0) {

        let node = stack.pop() ; 
        result += 1 ; 
        if (node.left !=null) {stack.push(node.left)}
        if (node.right !=null) {stack.push(node.right)}

    }
    return result ; 
};
