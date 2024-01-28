/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */


// Bottom up solution 

/*
    dp-table dp[i] : solution for change the "i" coin

    state transition function : 

        dp[i] = 1 + dp[i-j] for j in coins and i-j >= 0 

*/
var coinChange = function(coins, amount) {
    

    // create dp-table  , for 0 to amount coin 
    let dp = new Array( amount + 1  ).fill(  Number.MAX_SAFE_INTEGER ) ; 

    // base case ; 
    dp[0] = 0 ; 

    // outer-loop for state transition 
    for (let i = 1 ; i < amount+1 ; i++){

        for (let coin of coins){
            if (i-coin < 0){continue; } 
            dp[i] = Math.min( dp[i] , 1 + dp[i-coin] ) ; 
        }
    }

    return ( dp[amount] == Number.MAX_SAFE_INTEGER )?   -1 : dp[amount]; 
    
};



// Top-down solution with memo
var coinChange = function(coins, amount) {

    let hashmap = new Map() ; 

    let dp = ( amount ) => {
        
        // basecase : amount == 0 ; 
        if (amount ==0 ){return 0 ;}
        else if ( hashmap.has(amount)) {return hashmap.get(amount) ; }

        // temp to represent the solution of this dp func 
        let temp = Number.MAX_SAFE_INTEGER ; 

        for (let coin of coins ){
            if (amount-coin >=0){
                temp = Math.min(  1 + dp(amount - coin) , temp ) ; 
            }
        }
        hashmap.set(amount , temp) ; 
        return temp ; 
    }

    const solution = dp(amount) ; 


    return (solution==Number.MAX_SAFE_INTEGER)?   -1 : solution ;  
}