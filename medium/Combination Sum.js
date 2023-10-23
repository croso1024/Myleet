/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */


/*
    思路 : 
        給定一組包含不同整數的數列candidates , 要求可以湊出target的所有組合

        此為排列組合題目 , 因此首先想到BackTrack架構 . 
        但此題接受重複使用一個元素多次 ,困難的點在於要避開所有重複的組合
        
        -1. 一旦累積值大於target就不用展開下去 
        -2. 上一條搭配sorted , 可以更早的捨棄掉後半動作清單 , 但提昇我覺得有限
        -3. 對於避開重複組合 , 無法使用hashset, 因為array對hashset來說是物件 ,內容相同也會被當作不同
            更高效的作法必然還是透過剪枝 , 在每一次往下展開時都縮減動作清單 
            ex. candidate=[1,2,3] 來說 , 最往左的分支可以一直用到1 ,
            換句話說就是從1開始選,"一旦不選1了,那後面不能再選1" , 這個結構在許多不可重複組合的BackTrack問題中出現多次
            
            
*/


var combinationSum = function(candidates, target) {
    
    let result = new Array() ;

    // 因為candidate可以重複取用 ,因此我們就只要保存目前的累積數值和軌跡就好 
    let backTrack = ( actions ,accumulative ,track ) => {

        if (accumulative > target){return}
        else if (accumulative == target) {
            result.push(Array.from(track)) ; 
            return 
        }
        // 繼續展開 
        else {
            for (let [index,action] of actions.entries()) {
                track.push(action) ; 
                backTrack( actions.slice(index) , accumulative+action , track);
                track.pop()
            }
        }
    };

    backTrack( candidates , 0 , []);
    

    return result ; 
};