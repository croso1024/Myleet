/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// keep a hashmap to store the mapping relation 
var isIsomorphic = function(s, t) {
    
    let hashMap = new Map() ; 
    let size = s.length ; 

    for (let i = 0 ; i < size ; i++){
        
        if (hashMap.has( s[i] ) && hashMap.get(s[i]) !== t[i]){
            return false ;
        }
        else{
            hashMap.set(s[i] , t[i]) ; 
        }

    }

    let keySetSize = new Set(hashMap.keys()).size 
    let valueSetSize = new Set(hashMap.values()).size 

    return (keySetSize === valueSetSize)? true:false ; 


};