/*
    題意:

        給定一個array nums , 以及整數target , 要求返回有幾個non-empty subsequence,滿足
        seq內最小值與最大值的和 <= target , 
        因為這個解的數量太多, 解要 mod pow(10,9)+7 

    思路:
        sort後雙指標,
        - 若 nums[left]+nums[right] > target , 縮小right指標
        - 若 nums[left]+nums[right] <= target ,計算當前區間 ,如果left包含在sub_seq內有多少個解 
          接著移動left指標

          left包含在當前sub_seq內有多少個解 => 選定left後,剩下 n 個element有幾種組合
          n個element任意挑選的組合數 = Cn取1 + Cn取2 直到Cn取n

          n! / (1 + (n-1)!) + n! / (2! + (n-2)!)

          但可以從另外一個角度來看這件事, 10個element可以組成的序列總數為 2^10,
          即每個element都有出現or不出現可以選. 我反而認為這個idea是這一題最關鍵的部份
        
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var numSubseq = function(nums, target) {

    // first step : sorting the array 
    nums = nums.sort( (a,b) => a-b ) ; 
    let left = 0 , right = nums.length - 1 ; 
    const mod = Math.pow(10 , 9) + 7 ; 

    const powerTable = [1] ; 

    for (let i = 1 ; i <= nums.length ; i++){
        let base = powerTable[i-1] ; 
        powerTable.push( ( base * 2 ) % mod ) ;
    }
    console.log(powerTable)
    let solution = 0 ; 

    while (left <= right) {

        if (nums[left] + nums[right] <= target){
            // calculate how much sequence can be form in this interval 
            // but must choose the minimum number , so in actually ,
            // we just pick up number from  (right-left) number
            // solution +=  ( Math.pow(2 , right-left) ) % mod ; 
            solution += powerTable[right-left] ; 
            left += 1 ; 
        }
        else {
            right -= 1 ;
        }
    }
    return solution % mod ; 

};
