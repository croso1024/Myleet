/**
 * @param {string} s
 * @return {string}
 */


// DP solution 
var longestPalindrome = function(s) {
    
    let dp = Array.from( new Array(s.length) , (v)=> new Array(s.length).fill(null) ) ; 
    let solution = 1 ; 
    let bestInterval = [0,0];

    for ( let i = 0 ; i < s.length ; i++){dp[i][i] = 1}

    for (let i = 1  ; i < s.length ; i++){

        for (let j = 0 ; j < s.length - i ; j++){

            let x = j 
            let y = i + j 

            if (s[x] === s[y]){
                
                if ( Math.abs(x-y) === 1 ){
                    dp[x][y] = 2 ; 
                }
                else{
                    dp[x][y] = (dp[x+1][y-1] !== false)?  2 + dp[x+1][y-1] : false
                }
                if (dp[x][y] && dp[x][y] > solution){
                    solution = dp[x][y] 
                    bestInterval = [x,y] ; 
                }

            } 
            else{
                dp[x][y] = false 
            }
            

        }

    }
    return s.slice( bestInterval[0] , bestInterval[1] + 1  ) ; 

};

console.log(longestPalindrome('cbbd'))


