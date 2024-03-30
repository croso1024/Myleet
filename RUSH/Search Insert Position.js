/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */


// Binary search approach 
var searchInsert = function(nums, target) {
    
    let left = 0 , right = nums.length - 1 ; 


    while (left <= right){

        let mid = left + Math.floor((right-left)/2) ;  

        let probeNumber =  nums[mid] ; 

        if (probeNumber === target){return mid;}
        else if (probeNumber < target){
            left = mid + 1 
        }
        else{
            right = mid - 1 ; 
        }
    }

    return left 

};