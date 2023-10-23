/*
    思路:   
        給定兩個字串s1,s2 , 我們要找出s2中是否存在一個經過排列組合可得s1的子字串 ,
        注意這個子字串是要連續的在s2中出現 , 而不是包含在s2的某個子字串 

        雖然這一題是在sliding windows看到的例題 , 但直覺上來看可以用兩個指標 ,
        兩個指標maintain一個寬度和s1相同的window , 然後掃略整個s2結束 

        這一題只問有沒有存在 , 因此只要找到就結束 , 比較關鍵點在於->如何判斷valid 

        - 判斷valid法一 . maintain一個dict 紀錄target和window的字元數 , 檢查時就遍歷 O(len(s1)) 
        - 判斷valid法二 . 在進出的時候maintain一個valid_digits 基本上O(1) 
*/ 


/*
    節省時間直接實做法二 , 實際上法一就是我第一次接次sliding windows的minimum window substring的作法

    另外這題因為window的大小基本上就是固定的 , 所以結構和標準雙while不太一樣
*/

var checkInclusion = function(s1, s2) {
    
    if (s2.length < s1.length) {return  false;} 
    // 初始化必要資源 , 這一題window和target我直接用JS物件來存 , 操作上比map簡單些
    left = 0 
    right = s1.length  
    window = {}; 
    target = {};
    valid_digits = 0 ; 

    // 將target存入map 
    for (let char of s1) {
        if (char in target) { target[char] += 1 } 
        else {target[char] = 1 }
    } 

    // 因為此題window size是固定的,所以直接先把window塞入預設大小 , 順便也更新valid digits
    for (let index = 0 ; index < s1.length ; index++ ){
        if (s2[index] in window) {window[s2[index]]+=1} 
        else { window[s2[index]] = 1 }

        // 如果新增進入window的字元有在target內 , 並且該字元的加入使得windows內的出現次數等於target ,
        // 就代表某個字元條件符合了
        if ( (s2[index] in target)  &&  window[s2[index]] == target[s2[index]] ){
            valid_digits += 1 ;
        }

    }
    
    // 在開始走loop前先看,說不定一開始的window就包含答案了
    if (valid_digits == Object.keys(target).length) {return true} 

    // 接著只要雙指標同步走 , 走到right抵達s2底即可 
    // right往右 , 並更新window以及valid-digits 
    // left往右 , 並更新window以及valid-digits 
    // 判斷當前window是否有解 
    while ( right < s2.length ) {

        // right往右 , 並更新window以及valid-digits 
        let add = s2[right] ;  
        if (add in window){window[add] +=1}  
        else {window[add]=1} 
        if (add in target && target[add] == window[add]) {valid_digits+=1;}
        right += 1 ;

        // left往右 , 並更新window以及valid-digits 
        // 注意此處的順序和add比較不同 , 如果window內元素數量等於target所需 , 則在我們移除後valid-digits要少一
        // 另外因為有先增加過 , 這邊window[remove]-=1 就不檢查key in
        let remove = s2[left] ; 
        if ((remove in target) && target[remove] == window[remove]){valid_digits-=1;}
        window[remove] -= 1 ; 
        left += 1 ;  


        // 判斷當前是否有解 
        if (valid_digits == Object.keys(target).length) {return true} 

    }

    return false ;

};