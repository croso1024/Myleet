/**
 * @param {number[]} nums
 * @return {number[][]}
 */


/*
    思路:
        這一題也是排列組合那一類的 , 給定一個具有unique element的array nums 要求列出所有sub-set包含空集合 
        -> 剪枝Backtrack就能解決 

*/



// 解法一 . 看到題目的直覺 - 剪枝backtrack 
// 速度OK , 但空間不太好 
var subsets = function(nums) {
    
    let sol = [] ; 
    let track = [] ; 
    // 中止條件 res_pick為空 , 且在過程中的每一個step都要將當前sub-set存入sol 
    let backtrack = function( res_pick , track ){
        // push the subset into the sol for every step . 
        sol.push(Array.from(track)) ; 
        if ( res_pick.length == 0 ) {
            return ; 
        }

        for (let [idx , pick] of res_pick.entries()) {
            track.push( pick ) ; 
            backtrack(  res_pick.slice(idx+1) , track ); 
            track.pop() ; 
        }

    }

    backtrack(nums , track   ); 

    return sol ; 

};