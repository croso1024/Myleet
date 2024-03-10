/*
    題意:
        給定一個長度為偶數的string s , 裡面都是 '[' , ']' 兩種括號,且出現次數相等 
        求最少要幾次'交換'才能讓括號變成balanced

        一個balanced的括號條件為 :
        - AB , A和B各自是balanced
        - [C] , C為balanced 
    
    思路:
        我的直覺想法是two pointer從左右兩側開始下手 
        遇到 ] ... [ , 可以做一次swap然後內縮 ,  遇到 ][ ... 
        ][[][[]]

        但也可以用recursion的概念下去做, 
        關鍵在於找到像是 ][[][[]] , 這種的分界點在哪 , 

        ------------------------- 
        去看了neetcode的影片,這一題比較tricky的點在於交換bracket的概念, 
        ]][[ , 實際上只要交換一次 , ]]][[[則是需要交換2次 ,
        從左到右traverse一次string ,紀錄下 ']' 最多比'[' 額外多出現了幾次 , 
        而答案就是 (extra + 1) // 2 


*/

/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function(s) {

    let maxextra = 0 ; 
    let cur = 0 ; 
    for (let i = 0 ; i < s.length ; i++){
        
        if (s[i] === "[") { cur -= 1 }
        else {
            cur += 1 ; 
            maxextra = maxextra > cur? maxextra:cur ; 
        } 

    }

    if (maxextra > 0){

        return Math.floor(   (maxextra+1) /2          )

    }
    else {return 0 }

};