/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */



var searchMatrix = function(matrix, target) {
    
    // outer binary search  + inner binary search 
    let Oleft = 0 , Oright = matrix.length - 1 

    while ( Oleft <= Oright ){

        let Omid = Oleft + Math.floor( (Oright-Oleft)/2 ) ;
        let row = matrix[Omid] ;

        // find out the row contain the target value ; 
        if (row[0] <= target && row[ row.length-1 ] >= target){
            
            let Ileft = 0 , Iright = matrix[0].length - 1 
            while (Ileft <= Iright){
                let Imid = Ileft + Math.floor((Iright-Ileft)/2) ; 
                let val = matrix[Omid][Imid] ; 

                if (val === target){return true}
                else if (val > target){
                    Iright = Imid - 1 
                }
                else {
                    Ileft = Imid + 1  
                }
            }
            return false ;
        }
        else if (row[0] > target){
            Oright = Omid - 1 ; 
        }
        else{
            Oleft = Omid + 1 
        }

    }
    return false ; 

};