/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */


/*
    思路: 
        這一題蠻有趣的 , 似乎不在目前我已知的一些框架之中 ,要插入一個新的interval 
        必要時透過merge , 最終保持所有interval都不互相重疊
        
        這一題我原先思考了一段時間都不太知道如何解 , 後來爬文看到比較好的解法思路如下 : 
        我們"帶著當下的區間走" ,如果遇到完全沒有重疊且小於的 , 就將其加入sol
        如果遇到完全沒有重疊且大於的 , 反而就是將當前拿著的加入sol , 改拿新發現的 
        遇到重疊的case,就擴增 , 但不用放入sol , 就繼續拿著看有沒有前兩個case , 
        最後走出loop後把手上的加入sol 結束.

        以上解法真的漂亮
*/
var insert = function(intervals, newInterval) {
    
    if (intervals.length ==0){return [newInterval];}
    let sol = [] ; 


    for (let interval of intervals){
        // 如果要插入的interval start完全大於目前interval的end , 這個原本的interval原封不動放進解
        if (interval[1] < newInterval[0]){
            sol.push(interval) ; 
        }
        // 蠻精華的部份 , 如果走到一個interval的start就大於我們要插入的 , 那把newInterval插入解
        // 接著將newInterval換成這個新走到的,繼續完成 
        else if (interval[0] > newInterval[1]){
            sol.push(newInterval) ; 
            newInterval = interval ; 
        }
        // 會需要merge的情況 , 不用考慮什麼走while去確認擴散範圍 , 交給newInterval與for-loop處理就好 
        else{
            newInterval = [ Math.min( interval[0] , newInterval[0] ) , 
            Math.max(interval[1],newInterval[1]) ];
        }
    }

    // 將最後累積的newInterval給插入 
    sol.push(newInterval) ; 
    return sol ; 

};