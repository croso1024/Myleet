/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {

    let insert_probe = 1 ; 

    let flag = 1 

    for (let i = 1 ; i < nums.length ; i++){

        if ( nums[i] === nums[i-1] ){

            if (flag){
                flag = 0 
                nums[insert_probe] = nums[i] 
                insert_probe += 1    
            }

        }
        else{
            nums[insert_probe] = nums[i]
            insert_probe += 1 
            flag = 1 
        }
    }
    return insert_probe ; 
};