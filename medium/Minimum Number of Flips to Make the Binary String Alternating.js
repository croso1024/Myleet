/*
    題意 : 
        給定一個binary string s (只有0,1) 我們可以執行以下兩類操作
        -type1. 將字串中的第一個字移動到最後
        -type2. 從字串中選擇任一個字母反轉他, 
        這一題要我們返回'最少需要進行幾次type2的操作', 才可以讓整個字串變成交錯 010101 , 10101 ...

    思路 :   

        這一題要我們最小化的是對於type2操作的次數,代表我們可以無限次使用type1操作 ,
        但如果想要在一般的比較解法中加入type1操作會非常複雜 (而且type1操作後也有可能移動到後面的字串仍需要用type2改變),
        因此我們可以建立一個template , 因為長度為n的交錯字串只有兩種可能,
        通過比對這兩種template, 我們就可以知道最少需要花多少個type2的操作,
        接著考慮type1 , 我們進行一次type1操作後再次比對.

        每次比對整個字串take O(N) , 而我們又最多可以做N次type1操作 , so overall time complexity : O(N square)


        --> 然而這一題在比對上可以採用prefix的方式, 我打算把比對字串也加長兩倍 ,
        這樣當我們算出第一個diff1,diff2以後,我們只需要動最前面的元素 , 去算拿掉第一個元素對diff的影響,加在後面對diff的影響...

*/

/**
 * @param {string} s
 * @return {number}
 */

// 這個作法就是O(N^2)的版本,結構清晰易懂,但就是性能太差 
var minFlips = function(s) {

    
    const size = s.length ; 
    const expandString = s + s ; 
    let solution = Number.MAX_SAFE_INTEGER ; 
    // create reference binary string 
    let ref1 = "" ;
    let ref2 = "" ;
    for (let i = 0 ; i < size ; i++){
        ref1 += (i%2)? "0" : "1" 
        ref2 += (i%2)? "1" : "0" 
    }

    // check & update the minimum step to make the string alternate begin from startIndex
    const check = (startIndex) => {
        // diff with ref1 & ref2 
        let diff1 = 0 , diff2 = 0
        
        for (let i = 0 ; i < +size ; i++){

            if (expandString[i+startIndex] !== ref1[i] ){diff1+=1}
            if (expandString[i+startIndex] !== ref2[i] ){diff2+=1} 
            
        }

        solution = Math.min(solution , diff1 , diff2) ; 
    }

    for (let i = 0 ; i < size ; i++){
        check(i)
    }

    return solution 
    
};

// 加入prefix O(N)的版本,但有許多冗餘
var minFlips = function(s) {

    
    const size = s.length ; 
    const expandString = s + s ; 
    // create reference binary string 
    let ref1 = "" ;
    let ref2 = "" ;
    // 加長的ref string
    for (let i = 0 ; i < size*2 ; i++){
        ref1 += (i%2)? "0" : "1" 
        ref2 += (i%2)? "1" : "0" 
    }


    // only use for the first check 
    const check = (startIndex) => {
        // diff with ref1 & ref2 
        let diff1 = 0 , diff2 = 0
        
        for (let i = 0 ; i < +size ; i++){

            if (expandString[i+startIndex] !== ref1[i] ){diff1+=1}
            if (expandString[i+startIndex] !== ref2[i] ){diff2+=1} 
            
        }

        return [diff1 , diff2]
    }

    let [diff1,diff2] = check(0) ; 

    let solution = Math.min(diff1 , diff2) ; 

    for (let i = 0 ; i < size ; i++){

        // 移除第i個元素, 將其加在尾巴上
        if (expandString[i] !== ref1[i]){diff1 -= 1} 
        if (expandString[i+size] !== ref1[i+size]){diff1 += 1} 
        if (expandString[i] !== ref2[i]){diff2 -= 1} 
        if (expandString[i+size] !== ref2[i+size]){diff2 += 1} 
        solution = Math.min(solution , diff1 , diff2) ; 
    }

    return solution 
    
};

// 清理冗餘 , 實際上把一個值移動到尾端後diff的變化只和原始s的長度為奇數偶數有關而已
// -> 時間空間都很不錯
var minFlips = function(s) {

    
    const size = s.length ; 
    // create reference binary string 
    let ref= "" ;
    // 加長的ref string
    for (let i = 0 ; i < size ; i++){
        ref += (i%2)? "0" : "1" 
    }

    // only use for the first check 
    // diff with ref1 & ref2 
    let diff1 = 0 , diff2 = 0
    
    for (let i = 0 ; i < +size ; i++){

        if (s[i] !== ref[i] ){
            diff1+=1
        }
        else {diff2+=1}
        
    }
    let solution = Math.min(diff1 , diff2)

    if (size%2 !== 0){
        for (let i = 0 ; i<size ; i++){

            if (s[i] !== ref[i]){
                diff1 -= 1 
                diff2 += 1 
            }
            else {
                diff1 += 1 
                diff2 -= 1 
            }

            solution = Math.min(solution ,diff1 , diff2)

        }

    }
    return solution 
    
};