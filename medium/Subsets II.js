/**
 * @param {number[]} nums
 * @return {number[][]}
 */



/*
    思路 : 
        這一題和SubSet I的差別在於這邊給定的集合是可能有重複元素的 , 例如[1,2,2] 
        其排列可能是 : [[],[1],[1,2],[1,2,2],[2],[2,2]] 
        題目要求 "不能有重複的subset出現" , 而如果直接帶入SubSet I的剪枝backtrack會有一樣的元素出現

        這一題我的解法是這樣 , 先通過sorted , 把元素先排順序 , 這件事情在最外做 , 裡面就不用做了 
        然後在內部迴圈展開的時候多一個variable去存前一個元素(action) , 如果下一個還是一樣就跳過不往下展開
*/


// 解法一. 如同上面所說的 , 就是先sorted , 然後去紀錄前一個元素 , 注意變數prev是用let定義在函數內部 , 
// 相當於在"每一個展開分支部份去紀錄prev" .

// 速度和空間都不太優 , 但我覺得time/space complexity應該沒有太多進步空間 

var subsetsWithDup = function(nums) {

    let sol = [] ; 

    // sorted by non-decreasing order . 
    nums.sort( (a,b)=>a-b ); 
    
    let backtrack = function(res_action , track){

        sol.push(Array.from(track)) ; 

        if (res_action.length == 0){
            return ; 
        }

        let i = 0 ; 
        let prev = null ; 

        // Replace the for-loop by while , and control the index & previous element in res-action 
        while (i < res_action.length) {
            
            if ((prev != null) && ( res_action[i] == prev  )){
                i += 1 ; 
                continue ; 
            }

            // this action is ok , then go through backtrack process and record the index and prev element 
            track.push( res_action[i] ) ; 
            backtrack( res_action.slice(i+1) , track  ) ; 
            track.pop() ; 
            prev = res_action[i] ; 
            i += 1 ; 
        }

    }

    backtrack( nums , [] ); 
    return sol ; 
};