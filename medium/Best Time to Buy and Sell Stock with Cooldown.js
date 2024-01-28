/*
    思路 : 
        買股票系列問題 , 但我覺得這一題比較有創意 , 
        不限制交易次數 k , 但只要我們每次賣出就要至少休息一回合,所以整題而言更動的是狀態轉移函數 

        在普通情況 , 這一題的解為 
        令DP-table 為 dp[i][j] , 代表到達第i天時 , 是否持有股票對應的最大收益  

        // 沒有持股 
        dp[i][0] = Math.max( dp[i-1][0]  , dp[i-1][1] + price[i] )

        // 有持股 
        dp[i][1] = Math.max( dp[i-1][1] ,  dp[i-1][0] - price[i] )

        而現在強迫我們只要有賣出 , 那就一定要休息一回合 , 因此現在來說持股的情況會改變
        如果有持股 -> 代表前一回合就有持股 , 或著是是在兩回合以前買的股 
        dp[i][1] = Math.max( dp[i-1][1] , dp[i-2][0] - price[i] )

*/


/**
 * @param {number[]} prices
 * @return {number}
 */



/*
    解法一. 按照上面的狀態轉移框架 , 

    看起來可能會覺得在i==1的時候是特殊情況有點特別 , 但實際上可以想成 i==1也是base case , 因為實際的狀態轉移牽扯到
    dp[i-1] , dp[i-2] , 只是我把這部份放在迴圈中而已

    這個解的時間空間就不錯了 , 空間還有進一步優化的空間 
*/
var maxProfit = function(prices) {
    
    let dp = Array.from(  new Array(prices.length) , (v)=> new Array(2).fill(0) ); 

    // base case : 
    dp[0][0] = 0 ; 
    dp[0][1] = -prices[0] ; 

    for (let i=1 ; i< prices.length ; i ++){

        // i==1的情況是特殊情況 
        if (i==1){
            // 沒持股
            dp[i][0] = Math.max(dp[i-1][0] , dp[i-1][1]+prices[i]) ; 
            // 有持股
            dp[i][1] = Math.max( dp[i-1][1] , dp[i-1][0] - prices[i]) ; 
        }

        // i > 1後就是上面的正常case,如果有持股 , 那一定是上一回合就拿著 , 或著前兩回合的最大收益去買(代表上回合在休息)
        else {

            dp[i][0] = Math.max(dp[i-1][0] , dp[i-1][1]+prices[i]) ; 
            dp[i][1] = Math.max(dp[i-1][1] , dp[i-2][0]-prices[i]) ; 
        }

    }
    
    return dp[prices.length-1][0]
};