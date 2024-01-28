/*
    思路 :
        基本上就是2sum的解法走一個O(n)的迴圈 
        總時間複雜度是O(n^2) ; 

        即把3Sum分解為 :2Sum找特定target , 
        題目要求return所有滿足條件的triplets , 並且不能用duplicate , 所以最外層的迴圈我就用遞減式

*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {

    // sort to increasing order 
    nums.sort( (a,b)=> a-b ) ; 
    let solution_ref = new Set(); 
    let solution = [] ; 


    for (let index=0 ; index < nums.length-2 ; index++){

        // find two sum equal to nums[index] ; 
        let left = index + 1 ; 
        let right = nums.length - 1 ; 
        
        const base = nums[index] ; 

        while (left < right) {
            console.log(left , right)
            const sum = base + nums[left] + nums[right] ; 
            // check the hashset to avoid duplicate ; 
            // then add the triplet to solution array ; 
            if (sum == 0){
                // [base , nums[left] , nums[right]] must be increaseing order cause the sort . 
                if (  !solution_ref.has([base , nums[left] , nums[right]].toString())  ){
                    solution_ref.add([base , nums[left] , nums[right]].toString());
                    solution.push( [base , nums[left] , nums[right]] ) ; 
                }

                left += 1 ; 
                right -= 1 ;

            }
            else if (sum > 0){
                right -= 1 ;
            }
            else if (sum < 0){
                left += 1 ; 
            }
        }
    }

    return solution ; 
};




/*
    優化空間 , 在sum==0時走while loop跳過相同值, 這樣就可以閃掉duplicate 
    比較需要注意的細節包含 : 
        1. 在跳過元素的while loop的index 
        2. 外層loop也需要能夠跳過元素 , 這蠻容易忽略的
*/

var threeSum = function(nums) {

    // sort to increasing order 
    nums.sort( (a,b)=> a-b ) ; 
    let solution = [] ; 
    let prev = null ; 

    for (let index=0 ; index < nums.length-2 ; index++){

        if (prev != null  && nums[index] == prev){continue}

        // find two sum equal to nums[index] ; 
        let left = index + 1 ; 
        let right = nums.length - 1 ; 
        
        const base = nums[index] ; 

        while (left < right) {
            const sum = base + nums[left] + nums[right] ; 
            // check the hashset to avoid duplicate ; 
            // then add the triplet to solution array ; 
            if (sum == 0){
                solution.push([base , nums[left] , nums[right]])

                while ( left < nums.length-2  && nums[left] == nums[left+1]){  
                    left += 1  
                } 
                left += 1 ;
                
                while ( right > 2 && nums[right] == nums[right-1]){
                    right -=1 ; 
                }
                right -= 1 ; 

            }
            else if (sum > 0){
                right -= 1 ;
            }
            else if (sum < 0){
                left += 1 ; 
            }
        }

        prev = nums[index] ; 
    }

    return solution ; 
};

test = [-1,0,1,2,-1,-4] ; 

console.log(threeSum(test)) ; 