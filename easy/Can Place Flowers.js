/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */


/*
    思路 : 給定一個只有0,1 element的array , 求我們是否能將n個花插入其中 , 
    花代表數字1 , 每一朵花的左右兩邊不能有鄰接的花 
    即 [1,0,0,0,1] 只能將花插在正中央 

    --> 因為這一題問的是 "是否可以" 而不是要我們求出有多少種插花方式可以滿足之類的 
    所以直觀上來說 , 就是遇到可以插花的部份就插 , 走訪一次O(N) 走到底看是不是所有花都已經插完或著還有剩就好 
*/



// 解法一 . 我一開始寫的版本 , 就是檢查probe是否在邊界 , 然後一直插花 , 但這麼寫有些複雜
// 而且沒有處理到如 [0] 這種情況 , 因此改寫解法二 .
var canPlaceFlowers = function(flowerbed, n) {
    
    let probe = 0 ; 

    while (probe < flowerbed.length) {

        if ((probe == 0) && (flowerbed[probe]==0)) {
            if  ( (probe+1 < flowerbed.length) && (flowerbed[probe+1] == 0) ) {
                n -= 1 
                flowerbed[probe] = 1 ; 
                }
        }

        else if ((probe == flowerbed.length-1) && flowerbed[probe]==0) {
            if ( (probe-1 >= 0 ) && (flowerbed[probe-1] ==0) ) {
                n -= 1; 
                flowerbed[probe] = 1 ; 
            }
        }

        else {

            if ( (flowerbed[probe]==0) && (flowerbed[probe-1] == 0) && (flowerbed[probe+1]==0)){
                n -= 1 ; 
                flowerbed[probe] = 1 ; 
            }
        }
        probe += 1 ; 
        if (n==0) {return true;}
    } 

    return False 

};

// 解法二 . 實際上就是利用到or短路運算的特性 , 加上對於題目條件更清晰一點的整理 
// 當花在該格為0 , 且要馬probe=0 or probe-1 的格子 0  並且 要馬probe為最後一個值或他的下一個值為0   


var canPlaceFlowers = function(flowerbed, n) {

    let probe = 0 ; 

    while (probe < flowerbed.length){

        if (
            (flowerbed[probe] ==0 ) && 
            ( probe==0 || flowerbed[probe-1] == 0 ) && 
            ( probe==flowerbed.length-1 || flowerbed[probe+1]==0)
            )
            {   
                n-=1 ; 
                flowerbed[probe] = 1 ; 
            }

        probe += 1 ; 
        if (n<=0) {return true;}
    }

    return false ; 
}