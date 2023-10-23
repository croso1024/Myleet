/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */


/*
    思路 :  
        這一題蠻單純的 , 就是一個固定size的視窗去滑動找尋最大值 
        直觀來說可以透過一個長度為k的array去存著這些值,但這樣會有O(N)的space complexity 

        所以可以改用兩個指標去保存左右兩端的值 ,

        step1. 先計算 nums[0] ~ nums[k-1] 的總和 做一個初始結果 
        step2. 雙指標移動 , left指標移除windows中的元素 , right指標則做增加 
        step3. 每次調整完視窗 , 更新當下的最佳解  
        
        repeat step2 & step3

        一般的解法就如上先做window內的初始值 , 然後開始移動指標 
        但我想也可以套用sliding windows的框架 , left , right都從0開始 ,
         一直到 (right - left + 1) = k 開始才會進入到內層while去更新best也可. 


*/ 

// 解法一 . 比較直觀的先做window內的初始值 , 然後再開始掃蕩  
// 速度和空間都ok了

var findMaxAverage = function(nums, k) {
    
    // step.1 計算0到k的total value  , 做solution的初始值 
    let sum_of_window = 0 ; 
    for (let i = 0 ; i<k ; i++) {
        sum_of_window += nums[i] ; 
    }
    let best = sum_of_window / k ; 


    let left = 0 ; 
    let right = k-1 ; 

    while (right < nums.length-1) {

        // 移動兩個指標後更新一次best 
        sum_of_window -= nums[left] ; 
        left += 1 ; 

        right += 1 ;
        sum_of_window += nums[right] ; 

        best = Math.max(best , sum_of_window/k);

    }

    return best ; 
};


// 解法二 . 標準sliding windows框架 
// 基本上要思考的東西是我們要在哪個部份去更新解 , 但實際上這一部份依照實做去決定 

// 這個解的速度與空間都比上一個略好
var findMaxAverage = function(nums, k) {

    let left = 0 ; 
    let right = 0 ; 
    let window = 0 ; 
    let best = -Infinity ; 

    // 注意區間是左閉右開 , 初始狀態下window是沒有值的 
    while (right < nums.length){  

        window += nums[right] 
        right += 1   

        // 內迴圈 , 也就是left指標要開始進的條件, 是因為要保持right與left構成的區間大小為k 
        // 注意我們使用的規則是[left,right) , 因此right=2時只有 0,1兩個元素
        // right-left為左右指標內囊括的元素數量  , 當其大於k才要開始調整 

        while ( (right-left) > k ){

            window -= nums[left] ; 
            left += 1 ; 

        }


        // 我們在當right前進達到區間內有k個元素後做解答的更新 
        // 在這個部份 , 要馬就是區間內剛好到達k個元素 , 要馬就是right+1後先大於了 ,然後left+1縮進到剛好 
        if ( (right-left) == k ){
            best = Math.max(best , window/k)
        }

    }

    return best ; 

}