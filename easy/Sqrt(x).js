/*
    思路 :  
        給定一個非負整數x, 要求在不使用任何build-in的情況下返回
        他的square root floor . 

*/

/*
    解法一. 我一開始直觀的解法 O(x) 
        直接初始化 left , right = 0 , 1 
        去檢查  left*left <= target < right*right
*/


var mySqrt = function(x) {
    
    let left = 0 ; 
    let right = 1 ;
    while (  !((left*left <= x) && (x < right*right)) ) {
        left +=1  ; 
        right +=1   ; 
    }
    return left ; 

};

console.log(mySqrt(5)) ; 
console.log(mySqrt(8)) ; 
console.log(mySqrt(9)) ; 
console.log(mySqrt(25)) ; 

/*
    解法二. Binary Search
        這題乍看之下沒有馬上看出其能夠用Binary search來解 ,
        但實際上我們增加left邊界的速度並不需要線性 , 同時right的值就相當於右邊的界
        令right = x  , left = 0 來初始化 
        x的平方根必然在這段區間的某個位置 
        
        而那個位置的平方會是小於等於目標值 , 但有許多數字都符合此條件,
        所以我們要找的是符合此條件的右側邊界, 
        換句話說這一題就是 " 二分搜索找右邊界 " 的任務  
*/


var mySqrt = function(x) {

    let left = 0 ; 
    let right = x ; 

    while (left <= right ) {

        const mid = Math.floor( (left+right)/2 ) ; 

        // 對於此題來說,沒有剛好的單一目標值 , 
        // 所有mid*mid 小於等於目標值的都有可能是解 ,我們是要找這群解的右側邊界
        if ( mid*mid <= x ) {
            left = mid+1 ;  // 最後一次找到後 , 這個解就會跨越right 
        }

        else {
            right = mid - 1 
        }

    }

    // 因為是搜索右側邊界 , 當left指針超越right的時候 , left-1或right指向的就是答案
    return right ; 

}