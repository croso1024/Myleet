/**
 * @param {number[]} nums
 * @return {number}
 */


// dp[i] : maximum profit we can get when we steal the i-th house. 
var rob = function(nums) {

    if (nums.length === 1){return nums[0]} 

    let dp = new Array(nums.length).fill(0) ; 
    dp[0] = nums[0] ; 
    dp[1] = nums[1] ; 

    for (let i = 2 ; i < nums.length ; i++){

        let prevMax = Number.MIN_SAFE_INTEGER ; 

        for (let j = 0 ; j < i - 1  ; j++){
            prevMax = Math.max(prevMax , dp[j]) 
        }

        dp[i] = prevMax + nums[i] ; 

    }

    return Math.max(...dp) ; 
    
};


var rob = function(nums) {

    if (nums.length === 1){return nums[0]} 
    
    let bestPrev1 = nums[0] ;
    let bestPrev2 = Math.max(nums[0] , nums[1]) ;

    for (let i = 2 ; i < nums.length ; i++){

        if ( i % 2 === 0){

            bestPrev1 = Math.max( bestPrev1 + nums[i] , bestPrev2 )

        }
        else{

            bestPrev2 = Math.max( bestPrev2 + nums[i] , bestPrev1 ) ; 

        }

    }

    return Math.max(bestPrev1 , bestPrev2)

}