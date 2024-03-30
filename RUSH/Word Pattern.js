/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */



var wordPattern = function(pattern, s) {
    
    let wordArray = [] ; 
    let temp = "" ; 
    for (let i = 0 ; i < s.length ; i++){
        
        if (s[i] !== " "){
            temp += s[i] ; 
        }
        else{
            wordArray.push(temp) ; 
            temp = "" ; 
        }
    }
    wordArray.push(temp) ; 
    console.log(wordArray) ; 

    if (wordArray.length !== pattern.length){return false}
    let hashMap  = new Map() ; 

    for (let i = 0 ; i < pattern.length ; i++){
        
        let key = pattern[i] ;
        let word = wordArray[i] ; 

        if (hashMap.has(key)){
            if (hashMap.get(key) !== word){return false}
        }
        else{
            hashMap.set(key , word) ; 
        }

    }


    if (hashMap.size !== new Set(hashMap.values()).size){return false}
    return true ; 

};

wordPattern(pattern = "abba", s = "dog dog dog dog")