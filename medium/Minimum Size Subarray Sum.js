/*
    
    思路 :
        要求取最短的sub array可以去滿足大於等於target數字;
        如果沒有這樣的sub array再return 0 

        直覺上很容易就能想到sliding window , 而且這一題對於window內的資源還有計算是否有效都很簡單 
        直接使用雙指標框架去解決 , 

*/

/*
    解法一. 
        雙指標框架直接解 , 基本上唯一需要思考的只有要在放大還是縮小的時候更新解 
        對於這一題來說是縮小的時候 , 進入內層while時第一步先更新解
*/ 

var minSubArrayLen = function(target, nums) {
    
    let left = 0 ; 
    let right = 0 ; 
    let window_sum = 0 ; 
    let best = Infinity ; 

    while ( right < nums.length ){

        let add = nums[right] ; 
        window_sum += add ; 
        right += 1 ; 

        let valid = (window_sum>=target)? true : false ;

        while (valid && (left<=right)){

            best = ((right-left)<best)?  (right-left):best 
            let remove = nums[left] ; 
            window_sum -= remove ; 
            valid = (window_sum>=target)? true : false ; 
            left += 1 
        }

    }
    if (best == Infinity) {return 0 }
    else {return best ;}

};