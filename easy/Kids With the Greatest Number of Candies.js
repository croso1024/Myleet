/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */


/*
    思路 : 
        這一題有點過於簡單 , 基本上先走O(N)取得最大值 , 
        接著在走一個O(N)去看每一個元素+上extra後能否大於最大值就結束 
*/

var kidsWithCandies = function(candies, extraCandies) {

    let maximum = Math.max(...candies) ; 

};