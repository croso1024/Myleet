/*
    思路 : 
    
        使用兩個指標一同從頭開始前進 , 只要遇到0 , 指標1就停止 , 指標2繼續前進
        指標2前進到非0的時候 , 做一個swap , 這樣全部做完就完成了 , 但時間複雜度可能是O(N^2)

        另外這一題在做的時後遇到javascript的奇妙現象 --> 居然可以存取超越陣列的index number ,
        導致我的swap可以無限的做到突破極限.
*/

/*
    解法一. 我依照雙指標的思路去直接手刻 -> 速度很慢 O(N^2) , 空間還可
*/

var moveZeroes = function(nums) {
    
    let left = 0 ; 
    let right = 0 ;  

    while (left < nums.length) {
        if ( nums[left] == 0 ) {

            // 經過while , right就會落在一個非0的位置
            while ((right < nums.length-1) && (nums[right] == 0)) {
                right += 1 ; 
            }
            // 如果走到底 , right還是指向0,那就可以跳出迴去了
            if (nums[right] == 0 ) {return} 

            // swap 
            [nums[left] , nums[right] ] = [nums[right] , nums[left]] ; 

        }
        left += 1 ; 
        right = left ; 
    }

};

/*
    解法二. 
        東哥的思路這一題實際上就是先做移除所有的0 , 然後再補零補到原始長度 
        去除所有0的方式很簡單 , 快慢指標 , 當快指標遇到0就跳過不賦值
*/ 

var moveZeroes = function(nums) {

    let slow = 0 ; 
    let fast = 0 ; 

    // phrase.1 remove all zero elements . 
    while (fast < nums.length) {
        // 如果fast指標指到不是0 , 在slow指標賦值並前進
        if (!nums[fast] == 0) {
            nums[slow] = nums[fast] ; 
            slow += 1 ; 
        }
        fast += 1 ; 
    }

    // 走完這個迴圈 , nums[ 0 ~ slow-1 ]的位置就全都是非0 , 並按照原始順序排列 , 接下來要在slow到nums.length-1的部份補上0
    for (let index = slow ; index < nums.length ; index++ ) {
        nums[index] = 0 ;
    }

}
