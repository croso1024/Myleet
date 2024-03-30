/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    
    k = k % nums.length ; 
    if ( k===0 ){return nums}
    
    // reverse entire array first 
    for (let i = 0 ; i < Math.floor(nums.length/2) ; i++){
        [nums[i],nums[nums.length-1-i]] = [nums[nums.length-1-i],nums[i]] 
    }
    // reverse the first k element 
    for (let i = 0 ; i < Math.floor(k/2); i++){
        [nums[i] , nums[k-1-i]] = [nums[k-1-i] , nums[i]] 
    }
    // reverse the rest part 
    for (let i = 0 ; i < Math.floor((nums.length-k)/2) ; i++){
        [nums[i+k] , nums[nums.length-i-1] ] = [nums[nums.length-i-1] , nums[i+k]]
    }
    return nums 
};

console.log(rotate([1,2,3,4,5,6,7] , k = 3))
console.log(rotate([1,2,3,4,5,6,7] , k = 2))
console.log(rotate([1,2,3,4,5,6,7] , k=5))