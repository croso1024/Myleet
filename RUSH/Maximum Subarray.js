/**
 * @param {number[]} nums
 * @return {number}
 */


// dp solution ,dp[i] represent the maximum subarray end at i  
// dp[i]  = Math.max( nums[i] , nums[i] + dp[i-1] ) 
var maxSubArray = function(nums) {
    
    let dp = new Array(nums.length).fill(null) ; 
    dp[0] = nums[0] ; 
    let solution = dp[0] ; 

    for (let i = 1 ; i < nums.length ; i++){

        dp[i] = Math.max( nums[i] , nums[i] + dp[i-1] ) ; 
        solution = Math.max(solution , dp[i ]) ; 
    }

    return solution ; 
};


var maxSubArray = function(nums) {
    
    prev = nums[0]
    let solution = dp[0] ; 

    for (let i = 1 ; i < nums.length ; i++){

        prev = Math.max( nums[i] , nums[i] + prev ) ; 
        solution = Math.max(solution , prev) ; 
    }

    return solution ; 
};






console.log(maxSubArray([5,4,-1,7,8]))
