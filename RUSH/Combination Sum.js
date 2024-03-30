/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    
    candidates.sort((a,b)=>a-b) ; 
    let solution = [] ; 

    const backtrack = ( startIndex , track , acc )=>{

        if (acc === target){
            solution.push(Array.from(track)) ; 
            return 
        }

        for (let i = startIndex ; i < candidates.length ; i++){

            if (candidates[i] + acc > target){break ;}
            track.push(candidates[i]) ; 
            acc += candidates[i] ;
            backtrack( startIndex = i  , track , acc  ) ;
            acc -= candidates[i] ; 
            track.pop() ; 

        }
    }

    backtrack(0 , [] , 0 ) ; 
    return solution ; 

};