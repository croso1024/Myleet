/**
 * @param {string} s
 * @return {number}
 */

/*
    思路 : 
        這一題要我們找到字串s中 , 如果可以刪除任意元素,但不能更改元素順序的情況下可以找到的最大回文長度 
        在base case來說 , 當字串只有一個char , 那回文長度為1 

        這一題的test_case : s的範圍最大到一千個char ,如果想用展開爆搜的方法一定會無法滿足時間複雜度 
        因此要想辦法用dp , 這一題的dp定義比較複雜 , 需要用到2D的Dp-table  

        去思考需要怎樣的資料才能知道字串s的最大回文長度 , 或著說 "如何從數學歸納法中推得一個字串s在可刪除字元情況下的最大回文長度" ?

        -> 字串 s[i:j]的最大回文長度 = 
                                case.1 s[i]==s[j] : 則為 2 + dp[i+1][j-1]
                                case.2 s[i] != s[j] : 則為  max(  dp[i+1][j] , dp[i][j-1]   )
        

        在知曉這個思路後 , 第二個困難點在於這樣的DP要怎麼traverse , 無論是top-down或是bottom-up 
        先來看base case : dp[i][i] , 即空字串 , 代表對角線的值都是 0  , 
        接著開始擴散 ,緊鄰對角線的元素 , 最大回文長度都是1 , 
        我們的目標是要求整串的最大回文長度 , 亦即 dp[0][ s.length-1  ] , 在二維dp table的右上角


*/


/*
    解法一. 帶有備忘錄的top-down遞迴 , 使用top-down 的DFS加備忘錄的好處在於基本上不用處理traverse順序,方向的問題 
    用備忘錄來存 , 這個解法是可行的 , 但就是速度有點慢 , 且因為遞迴樹還會造成額外的空間損耗
*/

var longestPalindromeSubseq = function(s) {
    
    let memo = new Map() ;
    
    
    // dp(i,j) 計算s[i:j]的最長回文子序列(包含j)
    let dp = (i , j , memo) => { 
        
        if ( i==j ){return 1;}
        else if (i>j){return 0;} 
        // 在dp table中有了
        else if (memo.has( [i,j].toString() )){ return memo.get([i,j].toString()) ; }

        let result = 0 ; 
        if (s[i] == s[j]){
            result = 2 + dp(i+1 , j-1 ,memo) 
            memo.set(  [i,j].toString()  , result  )
        }
        else {

            result =  Math.max(  dp(i+1 ,j , memo) , dp(i ,j-1 , memo ) )
            memo.set(  [i,j].toString()  , result  )
        }

        return result ;
    }

    return dp( 0 , s.length-1  , memo) ; 

};

let test_case = "bbbab" ; 
longestPalindromeSubseq(test_case); 

/*
    解法二. bottom-up的填滿DP-table (遞推) 

    改寫bottom-up的難處在於如何去決定2D的table是如何擴散 , 這點從狀態轉移方程式可以分析 
    為了求dp[i][j] , 我們會用到的有 dp[i+1][j-1] , dp[i+1][j] , dp[i][j-1] , 即左下角 , 正下 , 左邊 ,
    
    而base-case是對角線全部為1 , 而那些 j>i的部份就是空字串 , 即預設值為0 , 所以初始值為一個左下三角全為0 , 對角線全為1的2D-table 

    因為要使用左下,左,正下 , 因此我們的推進方式很特殊 , "斜的一排一排往右上推進" 
    
    以5x5的grid來說 , 在填滿對角線和左下後 , 實際的遍瀝順序(index) :
    0,1 -> 1,2 -> 2,3 -> 3,4
    0,2 -> 1,3 -> 2,4 
    0,3 -> 1,4
    0,4

    這個解法在速度上海放解法一 , 空間也好了很多
*/

var longestPalindromeSubseq = function(s) {

    let size = s.length ; 
    if (size==1){return 1;}

    let dp = Array.from(
        new Array(size) , (v)=>{  return new Array(size).fill(0) }
    ); 

    // 初始化對角線為1 
    for (let i = 0 ; i < size ; i++){
        dp[i][i] = 1 ; 
    }

    // 開始走斜角方向遍瀝 , 注意看這樣的遍瀝方式 , 取出index的方式為 dp[i][i+index]
    // 我們的走法已經確保了不會index out of range , 只要先確保size=1的情況不會有就好
    for (let index = 1 ; index < size ; index++){

        for (let i = 0 ; i+index < size ; i++){

            if (s[i] == s[i+index]){
                // 兩側相等 , 則等於 2+左下
                dp[i][i+index] = 2 + dp[i+1][i+index-1] 
            }
            else {
                // 比較正下,左邊
                dp[i][i+index] = Math.max(  dp[i+1][i+index] , dp[i][i+index-1] ) 
            }

        }

    }

    return dp[0][size-1];

}