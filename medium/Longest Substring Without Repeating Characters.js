/*
    思路 : 
        最長的不重複子字串 , 又是一題需要在字串中滑動的 -> 想到sliding window algorithms 
        這一題先前在自己玩leetcode的時候用python寫過 ,現在學了框架 , 改用JS來寫個

        這一題要找的是不重複的最長子字串 , 因此在window的maintain上比較特別 , 
        不需要其他sliding window可能會看到的target,valid-digits什麼的 , 
        但是一旦找到重複的部份 , **left就要一路砍到移除重複的部份** 

*/

/* 
    解法一 . 直接框架秒殺 , 
        window的解是否有效 -->  window.lenght (right-left) == obj內key的數量
        這一題是否要進入收縮反而是等window的解為無效 ,才要進入收縮 

        但以下的解法其實有蠻多不必要的部份 , 因為會無效一定是新加入的字元和目前的window內有的字元出現重複
        --> 換句話說我們只需要縮小window直到把和當前新增字元相同的部份給丟出去 
*/
var lengthOfLongestSubstring = function(s) {
    
    let left = 0 ; 
    let right = 0 ; 
    let table = {} ; 
    let best = 0 ; 

    while (right < s.length) {

        add = s[right] ; 
        if (table.hasOwnProperty(add)){table[add] +=1}
        else {table[add] = 1}   
        right += 1 

        let valid = (right-left) == Object.keys(table).length ; 

        while (!valid  && left < right) {

            remove = s[left] ; 
            table[remove] -=1 ; 
            if (table[remove] == 0) { delete table[remove] ;  }  
            left += 1

            valid = (right-left) == Object.keys(table).length ; 
        } 

        best = ((right-left)>best)? right-left : best ; 
   
    }
    return best ;
}


// 解法二. 不按照標準框架 , 但實際上還是雙指標 , 只是整合了 valid和內部while

var lengthOfLongestSubstring = function(s) {

    let left = 0 ; 
    let right = 0 ; 
    let best = 0 ; 
    let temp = new Set() ; 

    while (right < s.length){

        add = s[right] ; 
        if (!temp.has(add)){temp.add(add); }
        // 出現重複字元 , 移動left指標直到跳過該重複字元 
        else{
            // 移動left指標,並且砍掉路上的字元 
            while (left<right && s[left] != add){
                temp.delete(s[left]);
                left+=1 ; 
            } 
            // 手動再加1跳過當下位置 , 因為外層我們已經增加了那個重複的字元
            left+=1 ;
        } 
        right += 1 ;
        best = ((right-left)>best)? right-left : best ; 

    }
    return best ; 

}