/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */

var merge = function(intervals) {
    
    intervals.sort(
        (a , b)=>{
            if (a[0] > b[0]){return 1}
            else if (a[0] < b[0]){return -1}
            else {
                if (a[1] > b[1]){return 1}
                else if (a[1] < b[1]){return -1}
                else {return 0}
            }
        }
    );
    let answer = [] ;  

    console.log(intervals)
    let [curInterVal_start , curInterVal_end] = intervals[0]  ; 
    for (let i = 1 ; i < intervals.length ; i++){

        if (curInterVal_end >= intervals[i][0] ){
            curInterVal_end = Math.max( curInterVal_end , intervals[i][1] ) ; 
        }
        else {
            answer.push( [curInterVal_start , curInterVal_end] ) ; 
            [curInterVal_start , curInterVal_end] = intervals[i] ; 
        }
    }
    answer.push([curInterVal_start , curInterVal_end] );

    return answer ; 
};

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))