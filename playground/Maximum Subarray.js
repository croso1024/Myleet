/**
 * @param {number[]} nums
 * @return {number}
 */




// 1D-Dp table : dp[i] : 以index=i結尾的array內 , 最大sub-array值
// base case : dp[0] = nums[0]
// state transition :  dp[i] = Math.max( nums[i] , nums[i] + dp[i-1] )

var maxSubArray = function(nums) {
    
    let dp = new Array(nums.length).fill(null) ; 
    dp[0] = nums[0] ; 

    for (let i = 1 ; i < nums.length ; i++){

        dp[i] = Math.max( nums[i] , nums[i] + dp[i-1] );
    }

    return Math.max(...dp)
};