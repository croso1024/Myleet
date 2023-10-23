/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

/*
    思路 :  
        這一題比較直觀的想法透過loop去走, 就是只要 s.length >= 0 , 就用wordDict的內容去掃描
        在wordDict[i].length >= s.length 的情況下去比對s的前 wordDict[i].length 的字串是否一樣
        一樣就消除 , 如果沒有滿足的就代表無法 

        --> 此直觀的想法不能處理如 s = cars , wordDict = ["car","ca","rs"] 的狀況
*/
var wordBreak = function(s, wordDict) {

    
    while ( s.length > 0 ) {

        let find = false ; 

        for (let word of wordDict){
            // 只要找到了一個字滿足 , 就跳出這個for , 到外層while 
            // 如果沒有就不做什麼
            if (s.length >= word.length){
                if (word == s.slice(0,word.length)) {
                    s = s.slice(word.length) ; 
                    find = true ; 
                    break ; 
                }
            }
        }
        
        // 走到這裡後如果是沒有找到字,代表無法拼出來了 
        if (!find){ return false ; }

    } 
    
    // 如果消除完後break使得s.length == 0 ; 則代表消除成功
    return true  ; 

};

/*
    東哥版的文章 ，說明了這一題從 '遍瀝' -> 使用backtrack 以及 '分解問題' -> 使用DP 兩種角度
    然而這一題使用Backtrack雖然可行，但會因為時間複雜度的關係而無法通過所有test-case , 
    這邊從DP角度出發。  

    這一題的 "狀態" 是指可以進行分解的字串符 s , 我們從wordDict中取值，
    如果 word可以和s的前半段匹配, 即 word = s.slice(0 , word.length) , 則只要 s.slice(word.length)能夠被分解那就有解 

    "這一題一樣要使用 遞迴Tree展開的角度來看 ，會比Bottom up的思路更加直觀" , 透過memo去消除重疊子問題

*/


/*
    解法二 . top down 遞迴+memo , 實際上看起來框架和backtrack超像 , 只不過說我是使用result去紀錄這個分支之下是否有可能有解
    這個作法蠻類似一般求極值問題使用float('inf')之類的 , 這部份應該有可以些微優化之處。
*/
var wordBreak = function(s, wordDict) {

    // memo 所保存的值就是當前剩餘的子字串是否可以被拼湊出來 , 換句話說我們的解就是memo[s] ; 
    let memo =  new Map() ; 


    // dp函數 , 給定當前的字串 , wordDict , memo  ,返回這個字串是否能夠被wordDict給拼湊出來 
    let dp = function( s , wordDict , memo  ){

        // base case : 
        // 1.如果s為空字串 , return True 
        if (s.length == 0) {return true; }

        else if ( memo.has(s) ){ return memo.get(s) ; }

        // 將結果設置為false , 除非下面迴圈中遇到可以拆分的 , 且其拆分後的分支也確實可以被分解 
        let result = false ; 


        for (let word of wordDict){
            // 展開遞迴樹
            if (s.length >= word.length && s.slice(0,word.length) == word){
                let temp = dp( s.slice(word.length) , wordDict , memo  );
                if (temp) {result = true;}
            }
        }

        memo.set(  s , result ) ; 

        return result ; 
    }


    return dp(s , wordDict , memo) ; 

}