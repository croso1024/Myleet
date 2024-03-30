/**
 * @param {number[]} nums
 * @return {string[]}
 */

var summaryRanges = function(nums) {
    
    if (nums.length === 0){return []}
    let curStart = nums[0]
    let curContinue = 0
    let answer = [] ; 
    for (let i = 1 ; i <= nums.length ; i++){

        if ( nums[i] === curStart + curContinue + 1 ){
            curContinue += 1 
        }
        else{

            if (curContinue === 0){
                answer.push(String(curStart))
            }
            else{
                answer.push( String(curStart) + "->" + String(curStart + curContinue))
            }
            curStart = nums[i] ; 
            curContinue = 0 ; 
        }
    }
    return answer; 
};

console.log(summaryRanges([0,1,2,4,5,7]))
console.log(summaryRanges([0,2,3,4,6,8,9]))
console.log(summaryRanges([0]))
console.log(summaryRanges([0,1]))
console.log(summaryRanges([0,1,5]))
console.log(summaryRanges([]))