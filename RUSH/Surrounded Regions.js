/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */

// perform dfs on every cell in the matrix , 
// and dfs(i,j) will return wheather (i,j) cell connect to the bound or not , if it connect to the bound ,
// we store the pos for those cell , and flip it value in the last step .
var solve = function(board) {

    const direction = [[1,0],[-1,0],[0,1],[0,-1]];
    const flipTable = [];

    const dfs = (i,j , path) =>{

        let connectToBound = null ; 
        if (i===0 || i===board.length-1 || j ===0 || j === board[0].length-1){
            connectToBound = true ;
        } 
        else{
            connectToBound = false ; 
        }

        for (let dir of direction){

            const next_i = i + dir[0] ; 
            const next_j = j + dir[1] ; 
            // console.log(`Now at ${i},${j} , next:${next_i},${next_j}`)
            if (next_i >= 0 && next_i < board.length && next_j >=0 && next_j < board[0].length){
                if (board[next_i][next_j] === "O"){
                    board[next_i][next_j] = "X" ; 
                    path.push(  [next_i,next_j] ) ; 
                    connectToBound = dfs(next_i,next_j , path) || connectToBound ; 
                }
            }
        }
        return connectToBound ; 
    }


    for (let i = 0 ; i < board.length ;i++){

        for (let j = 0 ; j < board[0].length ; j++ ){
            // console.log(board); 
            if (board[i][j] === "O"){
                board[i][j] = "X" ; 
                path = [[i,j]] 
                connectToBound = dfs(i , j , path) ; 

                if (connectToBound){
                    for ( let [a,b] of path){
                        flipTable.push([a,b]) ; 
                    }
                }
            }
        }
    }
    console.log(flipTable)
    for (let [i,j] of flipTable){
        board[i][j] = "O" ; 
    }
    return board ; 
};



var solve = function(board) {

    const direction = [[1,0],[-1,0],[0,1],[0,-1]]; 
    const flipSet = [] ; 
    const dfs = (i,j)=>{
        
        for (let dir of direction){

            let next_i = i + dir[0] ;
            let next_j = j + dir[1] ;

            if (next_i >= 0 && next_i < board.length && next_j>=0 && next_j < board[0].length){

                if (board[next_i][next_j] === "O"){
                    board[next_i][next_j] = 'X' ;
                    flipSet.push([next_i,next_j])
                    dfs(next_i,next_j) ; 
                }
            }
        }
    }

    for (let i = 0 ; i < board.length ; i++){

        if ( board[i][0] === "O" ){
            board[i][0] = 'X' ; 
            flipSet.push([i,0])
            dfs(i,0) ; 
        }
        
        if ( board[i][board[0].length-1] === "O" ){
            board[i][board[0].length-1] = 'X' ; 
            flipSet.push([i , board[0].length-1]) 
            dfs(i,board[0].length-1) ; 
        }

    }
    for (let j = 0 ; j < board[0].length ; j++){

        if ( board[0][j] === "O"){
            board[0][j] = 'X' ; 
            flipSet.push( [0 ,j] )
            dfs(0,j) ;
        }
        
        if (board[board.length-1][j]==="O" ){
            board[board.length-1][j] = 'X';
            flipSet.push([board.length-1,j])
            dfs(board.length-1,j) ;
        }
    }

    for (let i = 0 ; i <board.length ; i++){
        for (let j=0 ; j < board[0].length ;j++){
            board[i][j] = 'X' ;
        }
    }
    for (let [a,b] of flipSet){
        board[a][b] = "O" 
    }
    return board ; 
}