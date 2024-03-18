/*
    題意:

        給定一個整數n,代表一個有向圖中的節點數量,節點從0,1,2--> n-1. 
        並且有向圖中所有的edge都是藍色或紅色(同時有指向自己的edge以及平行的edge)  
        這些edge會在題目給定的redEdges與blueEdges中給定。

        這一題要求返回一個長度為n的array:answer , answer[x]代表從節點0出發到x的最短顏色交替路徑,或著-1代表該路徑不存在

    思路:
        我們要從0展開BFS,但看起來得分別展開紅色edge與藍色edge為開頭,同時在展開過程中去交替使用的graph,
        最直接的作法就是分別從0開始以紅/藍為先展開一次,並更新相應的答案

*/

/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */

// 這個解法在速度上算是很不錯, 大致上的步驟就是兩次build graph take O(edge.length) , 走BFS,以'兩個graph total edges數量'作為visited,
// 走兩次BFS就可以了, 速度很不錯,空間普通
var shortestAlternatingPaths = function(n, redEdges, blueEdges) {

    const buildGraph = (edges) =>{
        
        const graph = {} ; 
        for ( let [src , dst] of edges ){
            if (!graph.hasOwnProperty(src)){graph[src] = new Set();} 
            graph[src].add(dst) ; 
        }
        return graph ; 
    }

    const redGraph = buildGraph(redEdges) ; 
    const blueGraph = buildGraph(blueEdges) ; 


    const AlternativeBFS = ( graphs )=>{
        const answer = new Array(n).fill(-1) ; 
        answer[0] = 0 ; 
        queue = [0] ; 
        step = 1
        visited = new Set() ; 

        while (queue.length >0) {

            const size = queue.length ; 

            for (let i = 0 ; i < size ; i++){

                let node = queue.shift() ; 
                if (!graphs[step%2].hasOwnProperty(node)){continue}

                for (let neighbor of graphs[ step % 2 ][node]){

                    if ( !visited.has( [step%2 , node,neighbor].toString() ) ){

                        queue.push(neighbor) ; 
                        visited.add([step%2 , node,neighbor].toString())
                        if (answer[neighbor] === -1){
                            answer[neighbor] = step ;
                        }

                    }

                }

            }
            step += 1 
        }
        return answer ; 
    }

    const answer1 = AlternativeBFS([redGraph , blueGraph])
    const answer2 = AlternativeBFS([blueGraph , redGraph]) 
    for (let i = 0 ; i < n ; i++){
        if (answer1[i]!==-1 &&  answer2[i]!== -1) {
            answer1[i] = answer1[i] < answer2[i]? answer1[i] : answer2[i] ; 
        }
        else {
            if (answer1[i] === -1){answer1[i] = answer2[i]}
        }
    }

    return answer1 ; 

};

shortestAlternatingPaths(n=5 , [[0,1],[1,2],[2,3],[3,4]] , [[1,2],[2,3],[3,1]])