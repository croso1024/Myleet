/**
 * @param {number[]} nums
 * @return {number}
 */


/*
    建立DP-table , dp[i]代表以index = i 的字為結尾的subsequence可以連續的最大次數
    basecase 為 1  
    state transition : 
        dp[i] = 1 or max(dp[0~(i-1)]  for nums[i-1] <  nums[i] )
*/

var lengthOfLIS = function(nums) {
    
    // 設置 dp-table , basecase 
    let dp = new Array(nums.length).fill(1)  ; 

    // 外層迴圈推進狀態 
    for (let i = 1 ; i < nums.length ; i ++){

        // 內層迴圈計算該狀態的值 
        for (let j = 0 ; j < i ; j++) {

            if (nums[i] > nums[j]){
                dp[i] = Math.max( 1+dp[j]  , dp[i] ) ; 
            }
        }
    }
    return Math.max(...dp) ; 
};