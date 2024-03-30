/**
 * @param {number[]} nums
 * @return {number[]}
 */


// bi-direction prefix solution 
// prefix1[i] : accumultate multiply from left to i-1  , for i==0 is None 
// prefix2[i] : accumultate multiply from right to i+1 , for i==nums.length-1 , is None 
var productExceptSelf = function(nums) {

    const prefix1 = new Array(nums.length) ; 
    const prefix2 = new Array(nums.length) ; 

    // fill out the prefix1 
    let accMultiply = nums[0] ; 
    for (let i = 1  ; i < nums.length ; i++){
        prefix1[i] = accMultiply ; 
        accMultiply *= nums[i] ; 
    }
    accMultiply  = nums[nums.length-1] ; 
    for (let i = nums.length-2 ; i >= 0 ; i--){
        prefix2[i] = accMultiply ; 
        accMultiply *= nums[i] ; 
    }

    let answer = new Array(nums.length) ; 
    answer[0] = prefix2[0] ; 
    answer[nums.length-1] = prefix1[nums.length-1] ; 
    for (let i = 1 ; i<nums.length-1 ; i++){
        answer[i] = prefix1[i] * prefix2[i] ; 
    }
    return answer ; 
};

// 來回,使用answer矩陣
var productExceptSelf = function(nums) {

    let answer = new Array(nums.length).fill(1) ; 
    let temp = nums[0] ; 
    for (let i = 1 ; i < nums.length ; i++){
        answer[i] *= temp ; 
        temp *= nums[i] ; 
    }
    temp = nums[nums.length-1] ; 
    for (let i = nums.length -2  ; i >=0 ; i--){
        answer[i] *= temp ; 
        temp *= nums[i] ; 
    }

    return answer ; 
};