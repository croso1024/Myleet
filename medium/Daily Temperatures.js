/*
    思路:   
        這一題蠻有趣的 , 給定一個temperature , 裡面的值代表溫度
        要返回另一個array , 裡面的內容是 temperature[i] 需要等待幾天才會遇到下一個溫度更高的日子
        如果沒有這樣的日子 , 返回0 

        暴力解法就是雙迴圈去數 , 但鐵定不會過完全測資 
*/


/**
 * @param {number[]} temperatures
 * @return {number[]}
 */


// 暴力雙迴圈 
var dailyTemperatures = function(temperatures) {
    
    let solution = new Array(temperatures.length).fill(0) ; 

    for (let i = 0 ; i < temperatures.length ; i++){

        const base = temperatures[i] ; 

        for (let j = i+1 ; j < temperatures.length ; j++){

            if (temperatures[j] > base){
                solution[i] = j-i ; 
                break ; 
            }

        }
    }

    return solution ; 

};


// DP 
var dailyTemperatures = function(temperatures) {


}