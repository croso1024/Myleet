/**
 * @param {number[]} nums
 * @return {string[]}
 */

/*
    思路 :
        這一題的概念簡單 , 麻煩的是在於處理一些細節情況 , 
        我的作法是probe一直往前走 , 遇到和前一個值連續的就修改prev  
        不一樣後再依據狀況加入sol 

        不過在別人的答案中有看到 , 遇到一個值後用while loop繼續去擴展 , 擴展到邊界再一口氣加入的方式 
        在巨觀的時間與空間是一樣的 , 不過他那個作法應該更快沒問題 , 修改prev次數少很多
*/


/*
    解法一 ,
         線性時間 , 但速度表現還是挺差的 ,或許是誤差的問題
         空間上非常優 , 基本只有存sol , 其他都是靠指標


*/
var summaryRanges = function(nums) {
    
    const sol = [] ; 
    let probe = 0 ; 
    let start = null ; 
    let prev = null ; 

    while (probe < nums.length){

        if (start == null){
            start = nums[probe] ; 
            prev = nums[probe] ; 
        }
        else if (prev+1 == nums[probe]){
            prev = prev+1 
        }
        else {

            if (start == prev){
                sol.push(start.toString()) ; 
            }
            else {
                sol.push(start.toString() +"->"+prev)
            }
            
            start = nums[probe]; 
            prev = nums[probe] ; 

        }

        probe += 1 ; 
    }

    if (start != null){  
        if (start == prev){sol.push(start.toString())}
        else {sol.push(start.toString()+"->"+prev.toString())} 
    }

    return sol ; 

};