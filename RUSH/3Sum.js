/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    let sortedArray = nums.sort( (a,b) => a-b )
    let solution = []  ;
    for (let i = 0 ; i < nums.length ; i++){

        if (i>0 && sortedArray[i] == sortedArray[i-1]){continue} 
        let target = sortedArray[i] ; 
        twoSum(target , i+1)

    }

    function twoSum(target , start_index) {

        let left = start_index 
        let right = nums.length - 1 

        while (left < right){

            let sum = target + sortedArray[left] + sortedArray[right]

            if (sum === 0){
                solution.push([target , sortedArray[left] ,  sortedArray[right] ])
                left += 1 
                while (left < right && sortedArray[left] === sortedArray[left-1]){left+=1}
                right -= 1 
                while (left < right && sortedArray[right] === sortedArray[right+1]){right -= 1}

            }
            else if (sum >0){
                right -= 1 
            }
            else {
                left += 1 
            }
        }
    }
    return solution ; 
};

console.log(threeSum([-1,0,1,2,-1,-4]))
console.log(threeSum([0,1,1]))
console.log(threeSum([0,0,0]))