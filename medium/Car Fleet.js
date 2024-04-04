/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */

/*
    題意:   
        給定一個position array與speed array代表每一部車的初始位置與速度, 同時給定int target代表目標的位置.
        所有車輛會一同前進, 但"無法超車" , 題目要求最終分別會有幾團車輛一同通過target . 
        即速度較快的無法超車,會降低到與前方車輛(車隊伍)目前相同的速度 ,但他們會被視為並行

    思路: 

        將圖畫出來,包含所有節點初始位置與速度後, 可以蠻直觀的看出我們能夠計算所有車輛到達終點所需要的秒數,
        由最靠近終點的車輛開始 , 如果前一台車需要的秒數更低 , 他會與最靠近終點的車變成一團, 以此就可以驅動整個算法
        但這麼做的prerequest就是要sort posistion array, 就算題目有給定所有車輛一開始的位置都不一樣
        但這麼做也讓TC變成nlogn
*/


var carFleet = function(target, position, speed) {
    
    let solution = 0 ; 
    let ReverseIndex = Array.from( new Array(position.length) , (v,id)=>id) ; 
    // reverse sort by position 
    ReverseIndex.sort(
        (a,b) => position[b] - position[a]
    )
    
    let curFleetTime =   (target-position[ReverseIndex[0]]) / speed[ReverseIndex[0]]  ; 
    for (let i = 1 ; i < ReverseIndex.length ;i++ ){

        let curVehicleTime =  (target-position[ReverseIndex[i]]) / speed[ReverseIndex[i]]  

        // 變成同一團
        if (curVehicleTime <= curFleetTime){
            null
        }
        // 前一團先到 , 更新curFleetTime
        else {
            solution += 1 ;
            curFleetTime = curVehicleTime ; 
        }
    }
    return solution + 1 
};

console.log(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))