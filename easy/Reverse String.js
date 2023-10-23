/*
    給定一個字元陣列 , 要求in-place的反轉這個array ,
    看起來就是雙指標一左一右的連續swap就可以結束  , 

    中止條件就是雙指標相遇
*/


var reverseString = function(s) {
    
    let left = 0 ; 
    let right = s.length - 1  ; 

    // 中止條件是 left >= right ,重疊或超越 
    while ( left < right ){
        // swap  element 
        [ s[left] , s[right] ] =  [s[right] , s[left] ] ; 

        // shrink pointer 
        left += 1 ; 
        right -= 1 ; 
    }

};