/**
 * @param {character[][]} board
 * @return {boolean}
 */


var isValidSudoku = function(board) {
    

    const checkRow = row =>{
        let ref = new Set() ; 
        for (let i = 0 ; i < 9 ; i++){
            if (board[row][i] === "."){continue}
            if (ref.has(board[row][i])){return false}
            else{ref.add(board[row][i])}
        }
        return true ;
    }

    const checkColumn = column =>{
        let ref = new Set() ; 
        for (let i = 0 ; i < 9 ; i++){
            if (board[i][column] === "."){continue}
            if (ref.has(board[i][column])){return false}
            else{ref.add(board[i][column])}
        }
        return true ;
    }

    const checkBox = (row, column) =>{

        let ref = new Set() ; 
        for ( let i = row ; i < row+3 ; i++){
            for (let j = column ; j < column+3 ; j++){
                if (board[i][j] === "."){continue}
                if (ref.has(board[i][j])){return false}
                else{ref.add(board[i][j])}
            }
        }
        return true 
    }

    for (let i = 0 ; i < 9 ; i++){if (!checkRow(i)){return false}}
    for (let i = 0 ; i < 9 ; i++){if (!checkColumn(i)){return false}}

    for (let i = 0 ; i < 9 ; i +=3 ){
        for (let j = 0 ; j < 9 ; j+=3 ){
            if(!checkBox(i,j)){return false} 
        }
    }
    return true 

};