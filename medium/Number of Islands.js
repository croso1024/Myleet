/**
 * @param {character[][]} grid
 * @return {number}
 */

/*
    思路: 
        此題為廣度優先搜索可以解 , 直觀的想可能是Traverse這個array , 
        遇到1 (島嶼的一部分)就開始執行BFS , 並把看過的i,j都放進set ,然後島嶼數+1 
        接下來再次看到1 , 先檢查他是不是在某一座島內的 , 如果不是再次執行廣度優先 ,島嶼數再加1 
        因為js不能用tuple作為key , 這邊直接用數字key , dp[i][j] = Number(ij)
*/

// 解法一. 我直接實做基於BFS的版本 , 但有些測資過不去 , 推測原因是當m,n到達10個以上 
// 就有可能 m=1 n=10 和m=11 n=0變成重複的key在hashset內  
// 為了要讓Javascript能夠保存成對的值作為key , 用array.toString()轉為字串

var numIslands = function(grid) {
    
    let islands = 0 ; 
    let hashset = new Set() ; // 我們使用數字來作為島嶼編號 , 保存已經接觸過得島嶼 

    for (let i = 0 ; i < grid.length ; i++ ){

        for (let j  = 0 ; j < grid[0].length ; j++){

            // 當我們發現島嶼 , 且是我們還沒有踏過得 -> BFS 
            // 括張完整座島嶼 , 並增加已知島嶼數1
            if ( (grid[i][j] == "1") && ( !hashset.has( [i,j].toString() ) ) ) {
                
                // coding BFS algorithms , use index i & j as the state 
                let queue = [] ; 
                queue.push([i,j])
                hashset.add([i,j].toString()) ; 

                while ( queue.length > 0 ) {
                    [cur_i , cur_j] = queue.shift() ;  

                    // 不超出邊界 && 往下是一個島 && 還沒加入hashset
                    if ( ( cur_i+1  < grid.length  ) && (grid[cur_i+1][cur_j] == "1" ) &&
                        (!hashset.has( [cur_i+1,cur_j].toString()) )) 
                    {
                        queue.push([cur_i+1 , cur_j])  ;
                        hashset.add([cur_i+1,cur_j].toString()) ; 
                    }

                    // 不超出邊界 && 往右是一個島 && 還沒加入hashset
                    if ( ( cur_j+1  < grid[0].length  ) && (grid[cur_i][cur_j+1] == "1") && 
                        (!hashset.has( [cur_i,cur_j+1].toString()) )) 
                    {
                        queue.push([cur_i, cur_j+1 ])  ;
                        hashset.add([cur_i,cur_j+1].toString()) ; 
                    } 

                    // 不超出邊界 && 往左是一個島 && 還沒加入hashset
                    if ( ( cur_j-1 >= 0  ) && (grid[cur_i][cur_j-1] == "1") && 
                        (!hashset.has( [cur_i,cur_j-1].toString()) )) 
                    {
                        queue.push([cur_i, cur_j-1 ])  ;
                        hashset.add([cur_i,cur_j-1].toString()) ; 
                    } 

                    // 不超出邊界 && 往上是一個島 && 還沒加入hashset
                    if ( ( cur_i-1 >= 0  ) && (grid[cur_i-1][cur_j] == "1" ) &&
                        (!hashset.has( [cur_i-1,cur_j].toString()) )) 
                    {
                        queue.push([cur_i-1 , cur_j ])  ;
                        hashset.add([cur_i-1,cur_j].toString()) ; 
                    }


                }

                islands += 1 ; 
            }

        }
    }
    return  islands;

};


// 解法二 , 根本不必要用hash set去保存走過的島 , 可以直接把走過得島嶼改成"0"

var numIslands = function(grid) {

    let queue = [] ; 
    let island = 0 ; 

    for (let i = 0 ; i < grid.length ; i++ ) {
        for (let j = 0 ; j < grid[0].length ; j++) {
            if (grid[i][j] == "1") {

                queue.push([i,j]) ;  
                grid[i][j] = "0" ; 
                // BFS Traverse 
                while (queue.length > 0 ) {
                    let [cur_i , cur_j] = queue.shift() ; 
                    // 檢查上面
                    if ( (cur_i-1 >= 0) && ( grid[cur_i-1][cur_j] == "1") ) { 
                        queue.push([cur_i-1 , cur_j]) ; 
                        grid[cur_i-1][cur_j] = "0";
                    } 
                    // 檢查下面  
                    if ( (cur_i+1 < grid.length) && ( grid[cur_i+1][cur_j] == "1") ) { 
                        queue.push([cur_i+1 , cur_j]) ; 
                        grid[cur_i+1][cur_j] = "0";
                    } 
                    // 檢查左邊 
                    if ( (cur_j-1 >= 0) && (grid[cur_i][cur_j-1] == "1") ) {
                        queue.push([cur_i , cur_j-1]) ; 
                        grid[cur_i][cur_j-1] = "0";
                } 
                    // 檢查右邊 
                    if ( (cur_j+1 < grid[0].length) && (grid[cur_i][cur_j+1] =="1" ) ) {
                        queue.push([cur_i,cur_j+1]) ; 
                        grid[cur_i][cur_j+1] ="0";
                    }  
                }
                
                island += 1 ; 
            } 
        }

    }

    return island ; 

}