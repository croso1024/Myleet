/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */

/*
    題意:
        給定一個陣列和整數k , 求是否可以將所有數字分成彼此相等的k組

    思路:
        最暴力的解法就是每個數字都有 k 個筒子可以放, 因此暴力破解的時間複雜度是 nums.length ^ k 
        最高就是16^16 = 2^64 , 這鐵定是不可行的, 稍微去思考該如何剪枝,
        每個筒子最多只能放 sum(nums)//k的數值 , 因此選筒子的時候就是看目前的累積數值,一旦放進去筒子數值會超過就不放了
        只放那些還能放的筒子,這樣應該可以有效地砍掉許多分支

        -----------------------
        這一題最大的疑惑在於如何使用memo去加速,為什麼solution使用 nums編碼作為hash值來用可以判斷,

        --> 因為一旦知道哪些數字是已經用過, 其實就是填滿多少筒並以及當前的筒子填了多少就都已經知道了 !!!!!

*/

/*
    這個解法可行,但速度不夠快, 我這邊是用'數字去選bucket'
*/ 
var canPartitionKSubsets = function(nums, k) {
    
    const size = nums.length ; 
    let sum = 0 
    nums.forEach( item => sum+=item )
    nums.sort( (a,b) => b-a )
    const bucketVolume = sum/k 
    console.log(bucketVolume)
    if ( !Number.isInteger(bucketVolume)) {return false}

    let solution = false ; 
    const memo = new Map() ; 


    // state : index of nums use , buckets 
    const backtrack = ( index , buckets) => {

        if (index == size) {

            // const result = buckets.every( item => item === bucketVolume )            
            // if (result) { 
            solution = true ;
            // }
            return true
        }

        const key = String(index) + "," + buckets.join();
        if (memo.has(key)){return false} 

        // 用當前數字選擇一個bucket放進去
        for (let b_id = 0 ; b_id < k ; b_id++ ){
            
            if ( nums[index] + buckets[b_id] <= bucketVolume ){
                buckets[b_id] += nums[index] 
                backtrack(index+1 , buckets)
                buckets[b_id] -= nums[index] 
            }
            // else {break}
        }
    }; 

    backtrack(0 , Array.from( new Array(k).fill(0)  ) )

    return solution
};


// console.log( canPartitionKSubsets( [10,1,10,9,6,1,9,5,9,10,7,8,5,2,10,8], k =11 ) ) 


var canPartitionKSubsets = function(nums, k) {
    
    const size = nums.length ; 
    let sum = 0 
    nums.forEach( item => sum+=item )
    const bucketVolume = sum/k 
    if ( !Number.isInteger(bucketVolume)) {return false}

    const memo = new Set() ; 
    const available = new Array(size).fill(1) ; 

    // state : index of nums use , buckets 
    const backtrack = ( index , curSum , bucket) => {

        if (bucket === k){
            return true
        }


        if (curSum === bucketVolume){
            return backtrack(0, 0 , bucket+1)
        } 

        const key = available.join()
        if (memo.has(key)){return false }

        for (let i = index ; i < size ; i++){

            if (available[i] && curSum + nums[i] <= bucketVolume){
                available[i] = 0 
                if (backtrack(index+1 , curSum+nums[i] , bucket)){return true}
                available[i] = 1 
            }
        } 

        memo.add(key);
        return false ; 

    }

    return backtrack(0 , 0  , 0  )

};

console.log( canPartitionKSubsets( [10,1,10,9,6,1,9,5,9,10,7,8,5,2,10,8], k =11 ) ) 