/**
 * @param {number[][]} matrix
 * @return {number[]}
 */



var spiralOrder = function(matrix) {
    

    const answer = [] ; 
    let size = matrix.length * matrix[0].length ; 
    let up = 0 , down = matrix.length , left = 0 , right = matrix[0].length

    let x = 0 , y = 0 ; 

    // 走到了bound後 , 就要切方向繼續走
    while (answer.length < size){

        while (y < right && answer.length < size){
            answer.push(matrix[x][y])
            y += 1 
        }
        y -= 1 
        x += 1 
        up += 1 

        while (x < down && answer.length < size ){
            
            answer.push(matrix[x][y]) 
            x += 1 
        }
        x -= 1 
        y -= 1 
        right -= 1 

        while ( y >= left && answer.length < size){
            answer.push(matrix[x][y]) 
            y -= 1 
        }
        y += 1 
        x -= 1 
        down -= 1

        while ( x >= up && answer.length < size){
            answer.push(matrix[x][y]) 
            x -= 1 
        }
        x+=1 
        y+=1 
        left += 1 

    }

    return answer ; 

};

// console.log(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
console.log(spiralOrder(matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))