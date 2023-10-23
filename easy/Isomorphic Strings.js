/*
    思路 :  
        這一題給定兩個字串 s,t  詢問是不是可以依靠替換單字 , 把s轉換成t 
        替換單字的意思就是讓s中的char代表map到不同的char , 但不能有兩個字會map到一樣的char 
        例如 egg : add 可以成功map , 把 e:a , g:d 就可以 
        題目有說要保留順序 , 且一個字可以map到自己

        這一題直觀上看，就是maintain hashtable , 然後同時走訪兩個string 
        只是說是不是可以只要一個hashtable , 紀錄單向的map關係 , 
*/

/*
    解法一. Hashtable + Hashset

    先不考慮簡化hash table , 邏輯上來說 
    初始化兩個指標從第一個字開始 , 如果src的字不存在hashtable  
    則hashtable[src[i]] = dst[i] , 去做map , 不考慮src[i]是否等於dst[i] 

    如果src的字已經在hashtable , 則檢查hashtable[src[i]] 是否是 dst[i] 是的話就ok , 不是就false了
    但以上沒有考慮到避免不同的字map到一樣的字的情況 , 會需要另一個hashtable或hashset 
    這邊以hashset來說 , "hashset保存我們可以map到的字"
    因此需要變成 , 如果src的字不在hashtable , 且對應dst也不存在hashset才合法
*/


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    
    if (s.length != t.length){return false ; }

    // hash table , 保存映射關係
    let hashtable = new Map(); 

    // hashset , 保存我們可以map到的值(即他的key必定在hashtable)
    let hashset = new Set(); 

    
    let i = 0 ; 

    while(i < s.length){

        // step.1 檢查src有沒有在hash table 
        if (hashtable.has(s[i])){
            // 如果有就檢查對應dst是否一樣 , 否則false 
            if (hashtable.get(s[i])  != t[i]  ){ return false ; }
        }
        // step.2 如果這個字不在hashtable , 說明我們第一次遇見 , 為了合法 , 
        // 他要map的對象一定不是先前hashtable裡面元素可以map的對象 , 意思就是不在hashset中 
        else {
            if (hashset.has(t[i])) {return false;}
            hashtable.set(s[i] , t[i]);
            hashset.add(t[i])
        }

        i ++ ; 
    }

    return true;
};