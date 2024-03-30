/**
 * @param {string[]} strs
 * @return {string}
 */


var longestCommonPrefix = function(strs) {

    let minSize = strs[0].length ; 
    let minString = strs[0] ; 
    for (let str of strs){
        if (str.length < minSize) {
            minSize = str.length ; 
            minString = str ; 
        }
    }

    for (let i = 0 ; i < minSize ; i++){
        for (let j = 0 ; j < strs.length-1 ; j++){
            if (strs[j][i] !== strs[j+1][i]){
                return strs[0].slice(0 , i)
            }
        }
    }
    return minString ;     
};

var longestCommonPrefix = function(strs) {

    let prefix = "" ; 

    for (let i = 0 ; i < strs[0].length ; i++){
        
        let compareChar = strs[0][i] ;
        for (let str of strs){
            if (i >= str.length){
                return prefix ; 
            }
            else if( str[i] !== compareChar ){
                return prefix ; 
            }
        }
        prefix += compareChar
    }
    return prefix ; 
};