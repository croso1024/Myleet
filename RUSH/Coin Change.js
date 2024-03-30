/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */



// dp[i] : the minimum coins require for assemble i 
// var coinChange = function(coins, amount) {
    
//     let dp = new Array(amount+1) ;
//     dp[0] = 0 
//     // calculate the minium coins require for assemble i coin 
//     const exchange = i =>{
//         console.log(i)
//         if (dp[i] !== undefined){return dp[i]}

//         let temp = Number.MAX_VALUE ; 

//         for (let j = 0 ; j < coins.length ; j++){
//             if (coins[j] > i){continue} 
//             let change = exchange(i-coins[j]) ; 
//             if (change !== -1){ temp = Math.min(temp , 1 + change ) }

//         }

//         if (temp === Number.MAX_VALUE){
//             dp[i] = -1 ; 
//             return -1 
//         }
//         else{
//             dp[i] = temp ; 
//             return temp ; 
//         }
//     }

//     let result = exchange(amount);
//     return result
// };


var coinChange = function(coins, amount) {

    let dp = new Array(amount+1);  
    dp[0] = 0 
    coins.sort((a,b)=>a-b) ; 

    for (let i = 1 ; i < amount+1 ; i++){
        let temp = Number.MAX_VALUE ; 
        for (let coin of coins){
            if ( i - coin >= 0 && dp[i-coin] !== -1 ){temp = Math.min(temp , 1 + dp[i-coin])}
            else if (i-coin < 0){break ;}
        }
        dp[i] = (temp===Number.MAX_VALUE)? -1 : temp ;
    }
    return dp[amount]; 

}

console.log(coinChange(coins=[186,419,83,408] , amount=6249))