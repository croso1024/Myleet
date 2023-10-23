
/*
    給定一個array , 找到peak element 並返回他的index ,
    可能array中有多個peak element , 只要返回任意一個就好
    peak element的定義是他的數值大於左右兩個neighbor,另外arr兩端的元素只需要比一個鄰居
    題目要求用O(logN)的算法來答

    使用binary search的方式不太直觀 , 但可以畫一條曲線 , 想像我們使用binary search去切分 
    當切分的地方不是一個peak的時候 , 
    - 切分點mid左邊高於mid -> 左方有peak 
    - 切分點mid右邊高於mid -> 右邊有peak 
    以上的思路不太明顯 , 也是這一題的難度所在 , 知曉這一點之後這一題就信手捻來 , 只要處理兩個邊界的special case 

*/

// 解法一 . 先不管O(logN) , 就直接linear找  -> 速度就贏50%了

var findPeakElement = function(nums) {
    
    if ( nums.length == 1 ) {return 0}
    if (nums.length ==2 && nums[0]!= nums[1]) {
        return (nums[0]>nums[1])? 0 : 1 
    }   


    for (let index=1 ; index<nums.length-1 ; index++) {

        if ((nums[index] > nums[index-1]) && (nums[index] > nums[index+1]) ){
            return index ;
        }
    }
    return null
};


// 解法二. 真正使用binary search的作法 , 這一題的玄機在於如何將題目給定的情境應用binary search.
// 注意我們實際上並沒有去特別操作mid和周圍鄰居數值一樣的狀況 , 如果一樣就是照樣減小搜索空間 , 因為題目給定
// peak就是要strictly greater than . 

var findPeakElement = function(nums) {

    if (nums.length == 1 ){return 0}

    let left = 0 ; 
    let right = nums.length - 1 ; 
    // 封閉區間binary search 
    while (left <= right ) {

        let mid = Math.floor(  (right+left)/2  ); 

        // special case , mid落在邊界 
        if (mid == 0){
            if (nums[0]>nums[1]) {return 0}
            // 如果不是解 , 代表mid右邊比較高  , 繼續切割搜索空間 
            else {
                left = mid + 1 ; 
            }
        }   
        else if (mid == nums.length-1) {
            if (nums[nums.length-1] > nums[nums.length-2]) {return nums.length - 1} 
            else {
                right = mid - 1 ; 
            } 
        }
        else {
            // mid大於周圍 -> 答案
            if ((nums[mid] > nums[mid-1]) && (nums[mid] > nums[mid+1])) {return mid}
            // mid小於等於左邊
            else if (nums[mid] <= nums[mid-1]) {
                right = mid - 1 ; 
            }
            else {
                left = mid + 1 ; 
            }
        }
    }
    return null ; 
}