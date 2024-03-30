/**
 * @param {number[]} citations
 * @return {number}
 */
 
// sort soluion
var hIndex = function(citations) {
    
    citations.sort( (a,b) => b-a ) ; 
    let sol = 0

    for (let i = 0 ; i < citations.length ; i++){

        // sol = Math.max(  sol , Math.min( citations[i] , citations.length-i ) )
        if ( citations[i] >= i+1 ){
            sol = i+1 
        }


    }
    return sol ; 
};