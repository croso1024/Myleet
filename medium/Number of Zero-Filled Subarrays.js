/**
 * @param {number[]} nums
 * @return {number}
 */

/*
    題意:

        給定一個Array nums, 要求返回內部的全0 subarray個數 , 
        p.s sub-array是指連續的array
    思路:
        Sliding window , right指標掃到0後開始展開 , 分解動作如下:
        將left移動到right , right開始擴張直到下一個是非0
        計算left <-> right有幾個0 假設有n個 , 一共可以組 n+(n-1)+(n-2) ... 即 n(n+1)/2個sub-array

*/


var zeroFilledSubarray = function(nums) {
    
    const size = nums.length ; 
    let left = 0 , right = 0; 
    let sol = 0 ; 

    while (right < size){

        if (nums[right] === 0){

            left = right ; 
            while (right < size-1 && nums[right+1] === 0 ){
                right += 1 
            }
            const n = right - left + 1
            sol +=  (n*(n+1)) / 2 

        }
        right += 1 
    }
    return sol 
};