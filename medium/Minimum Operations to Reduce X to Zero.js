/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */

// sliding window solution 
var minOperations = function(nums, x) {

    let sum = 0 
    for (let num of nums){sum += num} 
    let target = sum - x 
    console.log(sum , target)
    if ( target < 0 ) {return -1} 

    let left = 0 , right = 0 
    let maximumWindow = -1 
    let window = 0 
    while (right  < nums.length ){
        window += nums[right]
        right += 1 
        while ( window > target ){
            window -= nums[left]
            left += 1 
        }
        if (window === target){
            maximumWindow = Math.max( maximumWindow , right - left )
        }
    }

    return (maximumWindow !== -1)?  nums.length - maximumWindow : -1 

};

console.log(
minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309] ,  134365)
)