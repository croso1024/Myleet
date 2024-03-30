/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */

// sliding-window approach 
var minSubArrayLen = function(target, nums) {
    
    let window = 0 
    let left = 0 
    let right = 0 
    let solution = Number.MAX_VALUE ;

    while (right < nums.length){

        window += nums[right] ; 
        right += 1 

        while ( window >= target && left < right ){

            solution = Math.min( solution , right-left )
            window -= nums[left]
            left += 1 

        }

    }

    return solution === Number.MAX_VALUE?  0 : solution ; 

};