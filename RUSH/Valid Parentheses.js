/**
 * @param {string} s
 * @return {boolean}
 */


// stack solution 
var isValid = function(s) {
    
    let refTable = {
        ")":"(" , "]":"[" , "}":"{"
    };

    const stack = [] ;  

    for (let i = 0 ; i < s.length ; i++){

        if (  ["(","[","{"].includes(s[i]) ){
            stack.push(s[i]);
        }
        else{
            if (stack.length === 0 || refTable[s[i]] !== stack[stack.length -1]){
                return false 
            }
            else{
                stack.pop() ; 
            }
        }
    }

    if (stack.length === 0 ) {return true}
    else {return false}
};