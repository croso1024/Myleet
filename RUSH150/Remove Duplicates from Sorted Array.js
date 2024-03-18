/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    let insert_probe = 1 ;
    
    for (let check_probe = 1  ; check_probe<nums.length ; check_probe++){

        if (nums[check_probe] !== nums[check_probe-1] ){
            nums[insert_probe] = nums[check_probe] 
            insert_probe += 1 
        }
    }
    return insert_probe ;
};