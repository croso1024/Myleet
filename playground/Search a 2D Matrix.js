/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */



var searchMatrix = function(matrix, target) {
    
    // 先針對row做binary search , 再針對column做
    let m = matrix.length ; 
    let n = matrix[0].length ; 

    let left = 0 ; 
    let right = m - 1 ; 

    // 做封閉區間binary search 


    while (left <= right){

        let mid = Math.floor((left+right) / 2) ; 

        if (target < matrix[mid][0]){
            right = mid - 1 ; 
        }
        else if ( target > matrix[mid][n-1]){
            left = mid + 1 ; 
        }
        // 找到指定row了 , 內部再做一個binary search看看
        else if( target >= matrix[mid][0]  && target <= matrix[mid][n-1]) {

            let row = mid ; 
            left = 0 ; 
            right = n - 1 ; 

            while (left <= right){

                mid = Math.floor((left+right)/2); 

                if (target > matrix[row][mid]){
                    left = mid + 1 ; 
                }
                else if ( target < matrix[row][mid]){
                    right = mid - 1 ; 
                }
                else if (target == matrix[row][mid]){
                    return true ; 
                }

            }

            return false ; 
        }
    }
    return false ; 

};