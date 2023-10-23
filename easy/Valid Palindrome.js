/**
 * @param {string} s
 * @return {boolean}
 */

/*
    思路 : 
        這一題要問當我們將字串全部換成小寫 , 並且去除了當中所有的異常符號,逗號等等之後,
        是否正著念和反過來是相等的 

        我不想花時間去看如何檢查字元符合alphanumeric (0-9 + a-z + A-Z) , 
        思路上就是兩個指標一左一右內縮 , 遇到非那些字元的就跳過繼續縮 

*/

// 解法一. 先走O(n) 去處理掉所有不符合規則的字,接著雙指標一左一右比較結束 
var isPalindrome = function(s) {

    let strRegex = new RegExp(/^[a-z0-9]+$/i);
    s = s.toLowerCase().split("").filter( char=>strRegex.test(char) ).join("") ; 
    console.log(s) ; 
    
    let left = 0 ; 
    let right = s.length - 1 ; 

    while (left < right) {

        if (s[left] == s[right]){
            left += 1 ; 
            right -= 1 ; 
        }
        else {
            return false ; 
        }

    }

    return true ; 

};

// 解法二 . 看起來不需要使用regExp , 可以直接用比較符來做  
// 這邊s == s.reverse()有些bug居然還要先轉string讓我有點傻眼 , 如果不轉string就是for-loop比對
var isPalindrome = function(s) {

    // 先轉lowercase並過濾掉非alpha numeric , 同時轉成array
    s = [...s.toLowerCase()].filter(
        (char)=> ( (char >="a" && char <= "z") || (char >= "0" && char <="9") )? true:false 
    ) 
    
    return s.toString() == s.reverse().toString()


}

