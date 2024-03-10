/*
    題意:

        給定一個字串s,我們要將字串分解成多個sub-string , 每個substring中不能有任何重複的charater, 
        要求至少要分成幾個sub-string才可以達到這個條件.

    思路:
        依據題目的example case , 看起來直覺會想到sliding window ,或著說是Greedy approach ,
        用一個set去maintain目前範圍的字串,一旦遇到重複就把目前累積的加入solution , 重新初始化set
*/


/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    
    let solution = 0 ;
    let refSet = new Set() ; 

    for (let i = 0 ; i<s.length ; i++){

        if (refSet.has(s[i])) {
            solution+=1; 
            refSet.clear() ; 
            refSet.add(s[i]) ; 
        }
        else{
            refSet.add(s[i]) ;
        }
    }



    return solution + 1 ; 

};