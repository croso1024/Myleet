/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */

// sliding window
var characterReplacement = function(s, k) {
    
    // 檢查 , window內最多的值必須 >= window長度(right-left) - k
    const validTest = function(left,right , window){

        let most_freq = Number.MIN_SAFE_INTEGER ; 
        for (let c of Object.values(window)){
            most_freq = Math.max(most_freq , c) ;
        }
        return  ( (right-left) - most_freq <= k )? true : false
    }

    let left = 0 ; 
    let right = 0 ; 

    let sol = Number.MIN_SAFE_INTEGER ; 

    // 開放區間的sliding window [left , right) ; 
    // window內放的是每一個字母的出現次數 , 我們只接受k個不一樣的值
    let window = {} ; 

    while (right < s.length) {

        const add_element = s[right] ;  
        if (window.hasOwnProperty(add_element)) {window[add_element] += 1} 
        else {
            window[add_element] = 1 ; 
        }
        right += 1 ; 


        // 驗證window內的解合理 , 即相異元素最多只能有k個 
        let valid = validTest(left , right , window)

        // 不合理的狀況才要進來縮減window
        while (left < right && !valid){
            
            const remove_element = s[left] ; 
            window[remove_element] -= 1 ; 
            left += 1 ; 

            valid = validTest(left , right , window) ;
        }

        // 更新解 , 只有外擴的時候有可能刷新best ,
        sol = Math.max(sol , right-left) ; 

    }

    return sol 

};





var characterReplacement = function(s, k) {
 
    let left = 0 ; 
    let right = 0 ; 

    let sol = Number.MIN_SAFE_INTEGER ; 

    // 開放區間的sliding window [left , right) ; 
    // window內放的是每一個字母的出現次數 , 我們只接受k個不一樣的值
    let window = {} ; 

    while (right < s.length) {

        const add_element = s[right] ;  
        if (window.hasOwnProperty(add_element)) {window[add_element] += 1} 
        else {
            window[add_element] = 1 ; 
        }
        right += 1 ; 


        // 驗證window內的解合理 , 即相異元素最多只能有k個 
        let valid = validTest(left , right , window)

        // 不合理的狀況才要進來縮減window
        while (left < right && !valid){
            
            const remove_element = s[left] ; 
            window[remove_element] -= 1 ; 
            left += 1 ; 

            valid = validTest(left , right , window) ;
        }

        // 更新解 , 只有外擴的時候有可能刷新best ,
        sol = Math.max(sol , right-left) ; 

    }

    return sol 

};