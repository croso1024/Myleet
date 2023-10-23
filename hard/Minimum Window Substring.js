

/*
    思路 : 
        此題為書本sliding windows的範例，給定兩個字串s (srt) ,t (target) , 
        我們要找出s中最短的子字串去包含t中所有字元(包含重複) . 

        此題使用Sliding Windows求解 , 其基本步驟如下 : 
        1. 初始化兩個指標left,right在字串s開頭 
        2. right指標往前走 , 一直到left -> right的範圍滿足題目要求 ( t的所有字元都已經出現 )
        3. 接著移動left指標 , 每次移動都要更新目前的最佳解 , 
        4. 一旦動了left指標導致視窗內沒有最佳解 , 就要繼續移動right  , 直到right抵達s尾巴 

        以上的步驟2 實際上類似於尋找可行解的過程 , 而步驟3則是在找到可行解後做最佳化 
        因此概念上來說 , 就是兩個指標在維護一個大小增增減減的視窗 

        此框架的幾個核心問題便是 : 

        - 當right指標往右增加視窗範圍時，哪些資料要更新   ?
        - 什麼條件使得right指標暫停擴大，應該開始移動left ? 
        - 移動left縮小視窗時，哪些資料要更新  ?
        - 要在增加還是縮小視窗時更新目前的解 ?

*/

/*
    對於此題來說 , 因為需要的是視窗包含target內所有字元，而不考慮順序 ，
    因此我們可以用一個hashmap去保存視窗內所擁有的字元 , 以及需要的字元 , 
    --> 調整視窗大小時 , 就調整這個hashmap , 同時此hashmap也能快速幫我們判斷是否視窗內滿足target
    --> 輪到更新left時先更新當前解 , 再調整left往右 
*/


// 解法一 . 首次實刻 , 感覺resource hashmap 以及判斷是否valid有許多優化空間.

var minWindow = function(s, t) {
    // 如果s長度小於t就不可能有子字串包含所有t內字元
    if ( s.length < t.length ){return ""}

    let left = 0 ; let right = 0 ; 
    // use hashmap to keep track the windows and the needed resource of target
    let windows = new Map() ; 
    let target = new Map() ; 
    let solution = null ; 
    
    // update target hashmap
    for (let char of t) {
        if (target.has(char)) { target.set( char , target.get(char) + 1 ) } 
        else { target.set(char , 1)  }
    }
    
    // Sliding Windows  實際上是一個開區間 [left,right) 
    // 所以一開始left = 0 , right = 0,視窗內是沒有任何字元的 !!
    while (right < s.length) {

        // 調整windows內的資源
        if (windows.has(s[right])) {  windows.set( s[right] , windows.get(s[right]) +1 ) }
        else {windows.set(s[right],1)}
        right += 1 


        // 一個旗標保存當前windows內的資源是否滿足解 
        let valid = true ; 
        for (let [char,amount] of target.entries()) {
            if ( windows.has(char)  && (windows.get(char) >= amount) ){continue}
            valid = false ; 
        }
        

        // 一旦目前windows滿足了解的需要 , left指標收縮視窗範圍直到不滿足valid或趕上right
        while (valid && (left <= right)) {

            // 先更新目前的解 , 注意前面說到我們使用的right的是開區間 , 也是代表s.slice(left,right)沒有收錄right索引的字
            if ( solution != null ) { 
                solution =  (s.slice(left,right).length < solution.length)?   s.slice(left,right):solution ;
            }
            else {
                solution = s.slice(left,right) ; 
            }
            // 調整left , 並更新資源 , left指標走過得地方right已經走過 , 所以就不再一次判斷windows裡面有沒有這個key了
            windows.set(   s[left]  , windows.get(s[left]) - 1 ) ;

            // 再次判斷是否還符合解 , 只要判斷移出視窗的那個字減一後還有沒有滿足就可以了
            if  (  target.has(s[left]) &&  (windows.get(s[left]) < target.get(s[left]) ) ){ valid = false ;}
            
            // 這個left+=1放在第三個位置 , 主要是因為如果調整完window直接做會導致判斷是否還符合解那邊需要 left-1 
            left += 1 ; 

        }
    }

    return (solution == null)?  "" : solution 

};





