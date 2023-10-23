/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */


/*
    思路 : 
        在解完了Word break I 後來看這一題，無非也是透過Top downs的展開 , 並且像backtrack那樣maintain一個目前為止的句子 
        最後是透過消除重疊子問題來處理。
        重疊子問題需要一個hashset , 不過這一題hash set 保存的是  memo[s] : 字串s 可以被wordDict可以構成的子句 , 為list 

        我們就可以使用已符合的單字 , 去和list的內容重組 
*/


/*
    解法一. 帶備忘錄的top-down遞迴 , 這一題我原本的寫法會出現有 for(let word of wordDict) 所有字都無法消除s剩餘部份 , 然後還是返回 result = [] 
    造成說解答有誤 , 這邊做的處理就是多一個 effect 的標籤 , 如果是因為走過所有word沒有辦法消除剩下的 , 那effect為false , 代表這個字無法被組成任何句子回傳 
    換句話說只有真的用消除的 , 走到s.length == 0 , 才算是有效合法的 , 並將這個一路傳上去 , 只有真的是靠消除走到0的軌跡 , 才是effect
*/

var wordBreak = function(s, wordDict) {
    

    let memo = new Map() ; 

    function dp( s, wordDict , memo ){

        // 已經為空字串 , 那就啥也組不出來 
        if (s.length==0){return [true , []];} 
        // 該字串可以拼出的所有句子 , 都已經在memo中了 , 直接返回該list 
        else if (memo.has(s)) {return memo.get(s);}

        // 這個result是用來保存該字串可以構成的句子
        let result = [] ; 
        // 可能發生剩餘s.length != 0 , 但沒有任何字可以批配 , 最後還是回傳 result = [] , 會導致上面一層以為這個可以消除完畢
        let effect = false ; 


        for (let word of wordDict){
            if (s.length >= word.length){
                // 字的前綴和word dict有吻合 -> 就繼續展開 , 然後將結果(可以使用剩餘部份和wordDict構成的句子) 放到sentence
                if (word == s.slice(0 , word.length)){

                    [effect_res , sentence] = dp( s.slice(word.length) , wordDict , memo )

                    if (!effect_res){ continue }

                    if (sentence.length >0){
                        for (let sen of sentence){
                            result.push(  word+" "+sen    )                        
                        }
                    }
                    else {
                        result.push(word) ; 
                    }

                    effect = true ; 
                }
            }
        }
        memo.set(s ,[effect , result]) ; 
        return [ effect , result ]   ; 
    }

    return dp(s , wordDict , memo)[1] ; 
};


/*
    解法二. 
        更接近backtrack , 在進入leaf-node的時候將解放進全局變數 , 這個作法中沒有使用memo , 雖然速度慢但仍然能夠解出來
*/

var wordBreak = function(s, wordDict) {

    let sol = [] ; 

    // 中止條件是s.length == 0 , 將目前為止累積的track加入解中 
    let backtrack = ( s , wordDict ,  track  ) => {

        if (s.length==0){
            sol.push(track.slice(1))
            return 
        }

        for (let word of wordDict){

            if (s.length>=word.length){

                if (word == s.slice(0, word.length)){
                    backtrack( s.slice(word.length) , wordDict ,track+" "+word  ) 
                }
            }
        }
    }

    backtrack( s , wordDict , "") ; 

    return sol ; 

}
