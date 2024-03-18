/**
 * @param {string} s
 * @return {boolean}
 */


var isPalindrome = function(s) {
    const lc = s.toLowerCase().replace(/[^a-zA-Z0-9]/g , "")    
    let left = 0 
    let right = lc.length - 1 

    while (left <= right){

        if (lc[left] !== lc[right]){return false}
        left += 1 
        right -= 1 
    }
    return true 
};
