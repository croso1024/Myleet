/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */


// backtrack approach -> time limited exceed 
var wordBreak = function(s, wordDict) {
    
    let solution = false 

    const backtrack = ( rest )=>{
        if (rest.length === 0){solution = true}
        if (solution){return} 

        for (let word of wordDict){
            if (word.length > rest.length ){continue}
            if ( word === rest.slice(0 , word.length ) ){
                backtrack( rest.slice(word.length)) 
            }
        }
    }
    backtrack(s) ; 
    return solution ; 
};

// dp : memo solution 
var wordBreak = function(s, wordDict) {

    let memo = new Map() ; 

    const dp = (rest) =>{
        if (rest.length === 0){return true}
        else if( memo.has(rest) ){return memo.get(rest)} 

        let temp = false ; 
        for (let word of wordDict){
            if (temp) {break}
            if (word.length > rest.length){continue} 
            if (word === rest.slice(0 , word.length)){
                temp = temp || dp(rest.slice(word.length)) ; 
            }
        }
        memo.set(rest , temp); 
        return temp ; 
    }
    return dp(s) ; 

}