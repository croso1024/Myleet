/**
 * @param {number[]} citations
 * @return {number}
 */


/*
    思路 :  
        這一題的題目蠻有意思的 , 給定一個array叫做citations , 裡面的元素array[i]代表這個研究者第i篇論文的被引用數 
        我們要求該作者的最大h-index 

        h-index的定義是該作者至少要有h篇論文的被引用數在h以上 , 
        例如[3,0,6,1,5] , 則h-index為3 , 因為他至少有3篇paper在3引用

        ---- 我的直觀想法 

        我第一個想法是先走一個O(N) , 找出引用數最大值 , 接下來就建立一個等同引用數最大值得array ,用來統計每一個引用數的各自有幾篇
        第二個O(N) , 就是去歸位每一篇的引用數放到對應格子 
        第三個O(N) , 從後往前 , 就可以歸納 引用數大於i篇的一共有多少個 , 由後往前遇到滿足的就直接return 

        這樣 Time O(N) , Space O(最大引用數) 
        
        第二個作法則是先sort , 然後直接用一個右開始的指標往迴走 , 一邊累積個數一邊看當前值就結束 

        Time O(N log N) , Space constant 
        
        
*/


/*
    解法一. 多次O(N)走訪歸納所有論文的被引用次數 
    速度極優 , 空間不優 
*/

var hIndex = function(citations) {
    
    // create an array to record amount of  0 ~ maximum citation 
    let amount_of_citations = Array.from( new Array(Math.max(...citations) + 1) , (v)=>0  ); 

    // 去把每一個著作的引用數歸納進我們的array
    for (let cite  of citations) {
        amount_of_citations[cite] += 1 ; 
    }
    console.log(amount_of_citations) ; 
    // 由後往前 , 去找當前cite數與目前大於這個cite數的著作數量 
    let temp = 0 ; 

    // 注意這邊 , let index = amount_of_citations.length - 1 
    // 我一開始沒寫-1 , 因為我認為前面在建立array時用的是+1的 , 但實際這個amount_of_citations就是用+1建出來的 
    // 這樣造成了我amount_of_citations index out of range , 使得temp 變為 NaN
    for (let index = amount_of_citations.length - 1 ; index >= 0 ; index--) {
        console.log(temp , index) ; 
        temp += amount_of_citations[index] ; 
        if ( temp >= index ){return index;}
    }

};

/*
    解法二 . 做sort , 然後單一指標由右往左結束 
    最大的h-index發生在累積過程中遇到某一篇cite小於當下累計的數值 ,
    那代表當下累積的數值即至少有這麼多論文cite大於等於當下累積值 , 即最大h-index
*/


// [0,0,4,4]
// [1,1,3]
// [0,1,3,5,6]
// [100]
var hIndex = function(citations) {

    // non-decreasing order 
    citations.sort( (a,b)=> a-b  )

    
    let probe = citations.length - 1 
    // use to record the accumulative number
    let temp = 0 ; 

    while (probe >= 0) {
        // 至今累積的篇數大於等於目前遇到的citations , 那就是有效的h-index
        // 我們數的是 "一共有多少篇的paper大於一個特定citations"
        if ( temp >= citations[probe] ){return temp }
        // 如果遇到的citations數比當前還大 , 就繼續累加
        temp += 1 ; 
        probe -= 1 ; 

    }

    // maybe 每一篇cite都很高 , [8,9,10] 這樣temp不會超越citations的任何元素
    // 真的走完while迴圈表示所有paper的引用數都大於發表總數 
    return temp ; 
}
