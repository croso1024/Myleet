/*
    思路 :  
        此題要反轉一個字串列中的字串符出現的順序 "the sky is blue" -> "blue is sky the" 
        同時題目原始字串的前後可能有一些額外的空白 , 必須要在得到答案的時候一同去除 

        follow-up 要求只有O(1) space complexity去做

        解法一 . 使用一個array保存每個單詞 , 接著反轉array並拼湊成新的字串即可 
        解法二 . 同樣也要先去除左右空白 , 接著反轉整個string , 最後針對個別字串符反轉
*/

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    // 先去除頭尾空白 
    s = s.trim() ; 
    if ( s.length == 0 ) {return ""}


    let solution = [] ; 
    // 接著將字開始加入array
    let word = "" ; 
    for (let char of s ) {

    // 新的字元非空白時就是正常處理 , 加入word暫存
        if (char != " ") {
            word += char ; 
        }

        else {
            if (word != ""){
                solution.push(word);
                word = "" ; 
            }
        }
    }

    // 走完的時候可能還有最後一個word 
    if (word != ""){solution.push(word);} 

    console.log(solution) ; 
    return solution.reverse().join(" ") ; 

};



/**
 * @param {string} s
 * @return {string}
 */

// 解法二   , 先反轉全部字串 , 接著逐字反轉
var reverseWords = function(s) {

    s = s.trim() ; 
    // 切分開字串並存在s內 , 最後反轉
    s = s.split(" ").filter(  (str)=> (str=="")? false:true ).reverse() ; 

    return s.join(" ");

}