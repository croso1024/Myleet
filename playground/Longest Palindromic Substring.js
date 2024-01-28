/**
 * @param {string} s
 * @return {string}
 */



// 這一題要用擴散法 , O(N^2)的時間可以找到最佳解

var longestPalindrome = function(s) {
    
    
    let best = Number.MIN_SAFE_INTEGER ; 
    let best_string = null ; 

    for (let i = 0 ; i < s.length ; i++){

        // 處理回文串是奇數的case 
        let left = i ; 
        let right = i ; 

        while ( left-1 >= 0 && right+1 < s.length){
            if (s[left-1] == s[right+1]){
                left -= 1 ; 
                right += 1 ;
            }
            else {break ;}
        }

        if ( (right-left+1) > best ){
            best = right-left + 1 ; 
            best_string = s.slice(left , right+1)
        }

        // 如果回文串是偶數 
        if (i+1 < s.length && s[i]==s[i+1]){

            let left = i ; 
            let right = i+1 ; 

            while ( left-1 >= 0 && right+1 < s.length){
                if (s[left-1] == s[right+1]){
                    left -= 1 ; 
                    right += 1 ;
                }
                else {break ;}
            }
    
            if ( (right-left+1) > best ){
                best = right-left + 1 ; 
                best_string = s.slice(left , right+1)
            }

        }

    }


    return best_string ; 

};