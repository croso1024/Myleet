/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */

/*
    Makesure the two condiction:
    1. Every level in both tree have same nodes
    2. Every node in both tree have same parents 
    we use a function : equalLevel to verify it ! 
*/

// var flipEquiv = function(root1, root2) {
    
//     if (!root1 || !root2){
//         if (root1 === root2){return true}
//         else {return false}
//     }

//     // must have same key(represent have same nodes , and node parent)
//     const equalLevel = (table1 , table2)=>{

//         if (table1.size !== table2.size){return false} 

//         for (let node of table1.keys()){
//             if (table2.has(node) &&  table1.get(node) == table2.get(node)){}
//             else { return false }
//         }
//         return true 
//     }
//     const parentTable1 = new Map() ; 
//     const parentTable2 = new Map() ; 

//     const queue1 = [root1] ;
//     const queue2 = [root2] ; 
//     parentTable1.set( root1.val , null )
//     parentTable2.set( root2.val , null )

//     while (queue1.length || queue2.length){
        
//         if (!equalLevel( parentTable1 , parentTable2 )){ return false } 

//         const size1 = queue1.length ; 
//         const size2 = queue2.length ; 

//         for (let i = 0 ; i < size1 ; i++){

//             const node = queue1.shift() ; 
//             parentTable1.delete(node.val)
//             if (node.left){
//                 queue1.push(node.left) 
//                 parentTable1.set(node.left.val , node.val) 
//             }
//             if (node.right){
//                 queue1.push(node.right)
//                 parentTable1.set(node.right.val , node.val) 
//             }
//         }

//         for (let i = 0 ; i < size2 ; i++){
//             const node = queue2.shift() ;
//             parentTable2.delete(node.val) 
//             if (node.left){
//                 queue2.push(node.left) 
//                 parentTable2.set(node.left.val , node.val) 
//             }
//             if (node.right){
//                 queue2.push(node.right)
//                 parentTable2.set(node.right.val , node.val) 
//             }
//         }

//     }
//     return true ; 


// };

// Recursion approach 
var flipEquiv = function(root1, root2) {

    if (!root1 && !root2){return true}
    if (!root1 || !root2){return false}
    if (root1.val !== root2.val){return false} 


    return ( flipEquiv(root1.left,root2.left) && flipEquiv(root1.right , root2.right) ) || (flipEquiv(root1.left,root2.right) && flipEquiv  (root1.right , root2.left))
}
    