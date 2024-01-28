/**
 * @param {number[]} nums
 * @return {number}
 */


/* 
    類似 maximum array sum ,  但這一題是連乘 
    令dp[i]代表在以i結尾的subarray的最大值    

    這一題比較tricky的地方在於 , 我們要maintain的是1D的最大和最小數組
    
    即
    dp1[i] 為i結尾的最大乘積
    dp2[i] 為i結尾的最小乘積 

    這樣在計算上 

    dp1[i] = ( dp1[i-1] * nums[i] if nums[i] > 0 ) or (dp2[i-1] * nums[i] if nums[i] <0) or nums[i]
    
    
*/




var maxProduct = function(nums) {
    

    let dp1 = new Array(nums.length).fill(null) ; 
    let dp2 = new Array(nums.length).fill(null) ; 

    // base case dp1[0] = dp2[0] = nums[0]
    dp1[0] = nums[0] ; 
    dp2[0] = nums[0] ; 


    for (let i = 1 ; i < nums.length ; i++){

        if (nums[i] >0){

            dp1[i] =  Math.max(dp1[i-1] * nums[i] , nums[i] ) ; 
            dp2[i] =  Math.min(dp2[i-1] * nums[i] , nums[i] ) ;

        }
        else {

            dp1[i] = Math.max(dp2[i-1] * nums[i] , nums[i]) ; 
            dp2[i] = Math.min(dp1[i-1] * nums[i] , nums[i]) ;

        }
    }

    return Math.max(...dp1)
};