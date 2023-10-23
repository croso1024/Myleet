/**
 * @param {string} s
 * @return {string}
 */

/*

    思路 :
        此題牽扯到回文 , 可以比較直覺的思考到使用雙指標架構 , 
        我原先的直覺是使用雙指標從兩端開始 , 
        往內收縮的過程中我們期待每一步都相同最後相遇 , 並且相遇後可以更新目前最長的回文串 
        但這麼做的難點在於當要開始收縮區間的時候要怎麼定如何收縮 

        東哥版本的思路解決了這個問題 , 也就是我們從中間向外擴散 ,
        不過會有兩種case :
        1. 最長的回文是奇數長度 , 這樣以s[i]作為中心擴散即可 
        2. 為偶數 , 這樣我們必須要以s[i] , s[i+1]作為中心擴散 

        因此內部就是一個函數 , 使用中心字串 , left , right指標作為參數 ,
        我們要遍瀝兩次 , 一次以奇數回文為目標 , 一次為偶數 
*/

// 解法一. 透過擴散的思路直接解 , 空間結果不好 -> 因為我們在擴散的過程中持續調整string變數 ,但根本不必要

var longestPalindrome = function(s) {

    // diffusion 函數 , 從給定的區間向外擴散 , 擴散到非回文後視情況更新目前最大回文
    let diffusion = ( string , left , right ) => {
        // 向外擴張並持續加長回文
        while ( left >= 0  && right < s.length) {
            if (s[left] == s[right]) {
                string = s[left] + string + s[right]
                left -= 1 ;
                right += 1 ;
            }
            else {
                break 
            }
        }
        // 到此處時檢查目前回文長度是否大於最好的 
        if (string.length > result.length) {result = string ; }

    }

    result = "" ;  

    // 需要找奇數的回文 , 也要找偶數的回文 

    //先找奇數的比較簡單 , 當前中心字串以及開始探訪的左右
    for (let index = 0 ; index < s.length ; index++) {
        diffusion( s[index] , index-1 , index+1  )
    }
    // 再開始找偶數的 , 注意一下偶數的中心必須也要是相同字串
    for (let index = 0 ; index < s.length-1 ; index++ ) {
        
        if (s[index] == s[index+1]) {diffusion( s[index]+s[index+1] , index-1 , index+2)}

    }    

    return result ; 

};


//解法二 , 
//  不必在擴散過程調整string變數 , 因為我們已經有index , 要注意的就是 res.slice()的參數 , 
//  因為在擴散過程中斷時 , 我們是有left-=1 , right+=1的 , slice因為只會走到right-1 , 剛好抵銷 ,但left要補上+1 
//  就算一進來 , 根本沒有回文而沒有進入while , 也會需要+1,因為在外面call function的時候傳入的left是-1的


var longestPalindrome = function(s) {

    // diffusion 函數 , 從給定的區間向外擴散 , 擴散到非回文後視情況更新目前最大回文
    let diffusion = ( string , left , right ) => {
        // 向外擴張並持續加長回文
        while ( left >= 0  && right < s.length) {
            if (s[left] == s[right]) {
                left -= 1 ;
                right += 1 ;
            }
            else {
                break 
            }
        }
        // 到此處時檢查目前回文長度是否大於最好的 
        let res = s.slice(left+1 , right)
        if (res.length > result.length) {result = res; }

    }

    result = "" ;  

    // 需要找奇數的回文 , 也要找偶數的回文 

    //先找奇數的比較簡單 , 當前中心字串以及開始探訪的左右
    for (let index = 0 ; index < s.length ; index++) {
        diffusion( s[index] , index-1 , index+1  )
    }
    // 再開始找偶數的 , 注意一下偶數的中心必須也要是相同字串
    for (let index = 0 ; index < s.length-1 ; index++ ) {
        
        if (s[index] == s[index+1]) {diffusion( s[index]+s[index+1] , index-1 , index+2)}

    }    

    return result ; 

};
