/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

/*
    [1,2]   -> [3,1]
    [3,4]      [4,2] 
    clockwise rotation 90 degree -> swap by diagoal then reverse for every row 
*/

var rotate = function(matrix) {

    // step.1 swap the element diagonal 
    let size = matrix.length ; 

    for (let i = 0 ; i<size ; i++){
        for (let j = i ; j < size ; j++){
            // swap element 
            [matrix[i][j] , matrix[j][i]] = [matrix[j][i]  , matrix[i][j]] ; 
        }
    }

    for (let i = 0 ; i < size ; i++){
        let left = 0 , right = size-1 ; 
        while ( left < right){
            [matrix[i][left] , matrix[i][right]] = [matrix[i][right] , matrix[i][left]]
            left += 1  ;
            right -= 1 ; 
        }
    }
    return matrix 

};