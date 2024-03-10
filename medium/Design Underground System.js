/*
    題意:
        這一題要實做一個地鐵站點計時系統,用來計算兩個station間的通勤平均時間. 
        Implement以下三個界面
        -: checkIn (id , stationName) : 指定id的customer從stationName進入
        -: checkOut (id , stationName) : 指定id的customer從stationName離站
        注意只要至少完成一次進站離站,就可以開始算average的離開時間
        -: getAverageTime(startStation , endStation) : 取得從start到end的平均時間

        p.s
        - start->end != end->start 
        - 在call getAverageTime前一定會travel過
        - 一個id只會同時一個地方被checkin

    思路:

        我的思路是所有站點的交通時間要存在hashmap :
        map[A][B] = (totalTime , travels) , 用來累積總里程數以及旅行時間
        另一部份就是暫存"目前進站但未出站的客人" , 使用id作為key的hashMap , 紀錄他們進站位置就可以了

        依據題目給定,客人數量可以到10^6(但checkin/out只有 10^4 個call ) , 站點數量則<=10. ,
        依照我們以上的算法:
        TC都是O(1) , MC則是 : O(checkIn數) + O(站點數^2) 

        實際跑下來,速度很不錯,但空間蠻差的

*/
var UndergroundSystem = function() {
    
    this.inTravel = new Map() ; 
    this.matrix = new Map() ; 

};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {

    // if (this.inTravel.has(id)){throw "Error"} 
    this.inTravel.set(id , [stationName , t]) ;
    return  ; 
    
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    
    if (!this.inTravel.has(id)){throw "Error"}  

    // get the checkIn time and update the matrix 
    const [srcStation , time] = this.inTravel.get(id) ; 

    if (!this.matrix.has(srcStation)){this.matrix.set(srcStation , new Map())} 
    let record = this.matrix.get(srcStation) ; 

    if (!record.has(stationName)){record.set(stationName , [  t-time  , 1  ])}
    else {

        let [accTime , travels] = record.get(stationName) ; 
        record.set(stationName ,  [accTime + t - time , travels + 1])
    }


};

/** 
 * @param {string} startStation 
 * @param {string} endStation
 * @return {number}
 */
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    
    const [totalTime , travels]  = this.matrix.get(startStation).get(endStation) ; 
    return totalTime / travels


};

/** 
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */