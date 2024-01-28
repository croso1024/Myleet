/**
 * @param {number[]} prices
 * @return {number}
 */


// maintain一個數值代表累計至今的最大值 , 去看該最大值-新的值 來更新利潤 
// 即可完成 O(N)時間 , O(1) 空間的解
var maxProfit = function(prices) {
    
    let best = 0 ; 
    let maximum_price = null ; 

    for (let i = prices.length -1 ; i >=0 ; i-- ){

        let buy_price = prices[i] ; 
        if (maximum_price != null){
            best = Math.max(  maximum_price - buy_price ,   best ) ;
            maximum_price = Math.max(maximum_price , buy_price) ; 
        }
        else {
            maximum_price = buy_price ; 
        } 

    }

    return best ; 

};