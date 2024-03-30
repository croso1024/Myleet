/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */


var combine = function(n, k) {

    let answer = [] ; 

    const backtrack = ( startNum , track ) =>{

        if (track.length === k){
            answer.push( Array.from(track)  ) ; 
            return 
        }

        for (let i = startNum ; i < n+1 ; i++){
            track.push(i) ;
            backtrack( i+1 , track )
            track.pop() ; 
        }
    }
    backtrack( 1 , [] ) ; 
    return answer ; 
};