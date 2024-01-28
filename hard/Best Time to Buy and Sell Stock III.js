/*
    思路 : 
        買賣股票的第三題 , 這一題增加的限制為我們總共只能進行2次交易 , 
        更加general來說就是得要計算總計k次交易可以得到的最大金錢 


        根據股票問題一貫思路的DP定義 : 
        可以設定狀態包含了 :
        1. 天數 
        2. 可以交易的最大次數 k 
        3. 是否持有股票 

        dp[i][k][j]  : 在第i天 , 最多可以交易K次的情況下 , 是否持有股票可得的最大收益 
        我們要求的就是在最後一天手上沒有股票時的最大收益(必定大於等於拿著股票) 

        此題的狀態比較多且狀態轉移複雜 , 從base case先看 

        # 第一天 ,利益只會是0或你買進了一次
        dp[0][:][0] = 0 
        dp[0][:][1] = -price[0] 

        # 最大可以交易次數為0 , 那收益也會是0 
        dp[:][0][:] = 0 

        -- 狀態轉移  : 

        這一題的狀態轉移 , 我們在每一個狀態下都有幾個動作 : 賣出 , 買入 , 不動 

        # 如果我們手上沒有股票 : 那代表我們這一回合賣掉了 , 或著上回合就沒有
        dp[i][K][0] = max (  price[i] + dp[i-1][K][1]  , dp[i-1][K][0]   )
        
        # 如果手上有股票 : 則代表應該是這一回合買入 , 或著上回合就有

        # --- !!! 特別要注意針對交易次數的限制 , 因為一次完整的買入賣出才算交易 , 我們在買入的時候才更新K 
        交易是從buy開始的 , 因此不能在sell的時候更新K , 

        dp[i][K][1] = max ( dp[i-1][K-1][0] - price[i] , dp[i-1][K][1]     )

        // !! 我在實做的時候犯了一個錯 
        就是把K值設置為2 (這一題限制交易兩次 , 但實際上狀態為 交易0次,1次,2次) 
    
*/


/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    let K = 2+1 ; 
    let dp = Array.from( new Array(prices.length) , (v)=> Array.from(
        new Array(K) , (v)=> new Array(2).fill(0)  
        ) );

    // 更新base case : 
    for (let k = 0 ; k < K ; k++){
        dp[0][k][0] = 0 ; 
        dp[0][k][1] = -prices[0]
    }
    for (let i = 0 ; i<prices.length ; i++){
        dp[i][0][0] = 0;
        dp[i][0][1] = 0 ;
    }

    // 在我們的狀態轉移過程 , 計算dp[i][k][j] , 會需要前一天的i-1, k-1計算完成
    // 而在已知Base case的情況下 , 我們的這兩個狀態從1開始推進就好


    // 推進天數狀態
    for (let i = 1 ; i < prices.length ; i++){
        // 推進K 狀態
        for (let k = 1 ; k < K ; k++){

            // 沒有持股 : 賣出 or 本就沒有 
            dp[i][k][0] = Math.max( prices[i] + dp[i-1][k][1] , dp[i-1][k][0] )

            // 有持股 : 買入 or 本就有 
            dp[i][k][1] = Math.max( dp[i-1][k-1][0] - prices[i] , dp[i-1][k][1] )

        }
    }

    // 最終解在 dp[price.length-1][K-1][0]
    // 代表在到達最後一天時 , 在題目給定的K數下可以得到的最大利潤

    console.log(dp[prices.length-1]);

    return dp[prices.length-1][K-1][0] ; 

};
