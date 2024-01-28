/*
    思路 : 
        買賣股票系列第二題  , 這題需要用到DP的技巧了 
        此題沒有限制交易次數K , 所以對於"狀態"來說 , 我們能夠列舉的有 
        1. 天數 : 即考慮i為目前的天數 , i從0到prices.length -1 
        2. 目前是否持有股票 : 因為我們一次只能拿著一張股票 , 用0 or 1去表示目前的持股狀況 

        dp-table的定義如下: 
            dp[i][j] : 在第i天的情況下 , 我們 持有j==1/沒有持有j==0 , 任何股票時的最大利潤 
        那我們的最終目標就是計算 dp[-1][0] (因為沒有拿股票的利潤一定大於有拿)


        Base case : 
        # 第一天就有買和沒買
        dp[0][0] = 0 
        dp[0][1] = - prices[0]  

        在每一個state我們能做的只有賣掉/持有/買進 , 題目給的賣掉馬上買進一點意義也沒有

        那麼狀態轉移函數就可以寫了

            沒有股票有兩種 : 這一回合賣掉了 / 前一回合就沒有股票 
            dp[i][0] = prices[i] + dp[i-1][1]  / dp[i-1][0]

            持有股票也是兩種 : 這一回合買的 / 上一回合就拿著了 
            dp[i][1] = dp[i-1][0] - prices[i]  / dp[i-1][1]

*/


/**
 * @param {number[]} prices
 * @return {number}
 */

// 解法一. 正規DP 

var maxProfit = function(prices) {
    
    let dp = Array.from(  new Array(prices.length) , (v)=> [0,0]  ); 
    dp[0][1] = - prices[0] ; 

    for (let i = 1 ; i < prices.length ; i++){
        // 這一回合賣掉,或這一回合沒動
        dp[i][0] = Math.max( prices[i] + dp[i-1][1]  , dp[i-1][0] ) ; 
        // 這一回合買入,或這一回合沒動 
        dp[i][1] = Math.max( dp[i-1][0] - prices[i]  , dp[i-1][1]) 
    }

    return dp[prices.length-1][0] ; 

};


// 解法二. 優化空間 , 只保留前一個step , 

var maxProfit = function(prices) {
    
    hold = -prices[0] ; 
    empty = 0 ; 

    for (let i = 1 ; i < prices.length ; i++){
        const last_hold = hold ; 
        const last_empty = empty; 

        empty = Math.max( last_hold + prices[i] , last_empty) ; 
        hold = Math.max( last_empty - prices[i]  , last_hold  );

    }

    return empty ; 
};
