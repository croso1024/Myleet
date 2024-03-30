/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    
    let pathList = path.split('/').filter( (value) =>  value !== "" ) ;
    
    let solutionList = [] ; 

    for (let segment of pathList) {

        if (segment === '.'){} 
        else if (segment === '..'){
            // pop the last element in the canonical form path 
            solutionList.pop() ; 
        }
        else {
            solutionList.push( '/' + segment ) ; 
        }

    } 

    if (solutionList.length === 0){return '/'}
    else {
        return solutionList.join("") ; 
    }

};

console.log(simplifyPath("/../"));
console.log(simplifyPath("/home"));
console.log(simplifyPath("/home//foo/../foo"));