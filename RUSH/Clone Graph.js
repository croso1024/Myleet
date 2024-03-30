/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */


// DFS or BFS with copy-table 
var cloneGraph = function(node) {
    
    if (node===null) {return null}

    // record the node that already be copy ,
    let copyTable = new Map() ; 
    // perform BFS, store the 'true' node in the graph
    let queue = [node] ; 
    // record the node that already be visited . 
    let visited = new Set();  
    visited.add(node.val)
    
    while (queue.length) {

        let curNode = queue.shift() ; 
        if (!copyTable.has(curNode.val)){
            copyTable.set( curNode.val , new Node(val = curNode.val) ) 
        }
        for (let neighbor of curNode.neighbors){

            if (!copyTable.has(neighbor.val)){copyTable.set(neighbor.val , new Node(val = neighbor.val))}
            copyTable.get(curNode.val).neighbors.push( copyTable.get(neighbor.val) ) 

            if (!visited.has(neighbor.val)){
                visited.add(neighbor.val) ; 
                queue.push(neighbor) ; 
            }

        }

    }
    return copyTable.get(1) ; 

};