/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */


/*
    思路 :  
        給定一組array,裡面可能有重複的值 , 題目要問是否存在 :
        ( nums[i] == nums[j] ) and ( i != j )and  ( abs(i-j) <= k )
        我的理解是這一題的作法 , 就是依據k的值做一個window , 然後掃蕩整個array就可以了
        
        我想到的方法
        1. 為了方便操作 , 先走一次O(N) ,把所有的值都建立在hashtable裡面 , 再來maintain window內的元素數量
        2. 其實好像可以直接用set , set內的個數應該要等於window內的元素數量 , 如果發生set.size < window.size
           則此題就是有解
*/


/* 
    解法一. 
        直接使用set來maintain , 確保set的元素數量等於window內的元素數量 
        window.size 理論上要等於 k+1  

        另外根據題目給的條件，是有可能 k > nums.length的 , 這種情況下就變成單純是找有沒有duplicate
        window的大小等於  min(k+1 , nums.length)

        寫sliding window的framework
*/         

var containsNearbyDuplicate = function(nums, k) {
    
    let window_size = Math.min( nums.length , k+1 ); 
    // 要確保window內的元素放入集合後的大小等於window_size 

    let hashset = new Set() ; 
    let left = 0 ; 
    let right = 0 ; 
    // 注意區間 , 左閉右開 
    while ( right < nums.length) {

        hashset.add( nums[right] ) ; 
        right += 1 ;

        // 內迴圈就是滿足條件 , windows_size到達k所要的才進來 
        // 我們在內迴圈再來檢查是否有異常 
        while ((right - left) == window_size ){
            // hashset的大小如果不等於window , 代表說有duplicate,滿足題目條件了
            if (hashset.size != window_size){ return true }
            hashset.delete( nums[left] ) ; 
            left += 1 
        } 
    }

    return false ; 

};

/*
    解法二 . 
        就原本想的 , 滑動固定視窗的方法 , 反而這個作法比較多細節小bug
        主要反應在right = window_size ,以及判斷hashset.size != window_size的時機 

        記住我們的window還是左閉右開 , 在一開始for loop把元素填充到window_size後
        進入while-loop , 我們先判斷當前window內是否合理(因為已經達到判斷條件)
        接著才調整left , right , 但有可能最後一次調整沒有觸發到比較 , 這邊要再手動補

        下面的解法是在剛進入while loop的時候做一次檢查 ,
        然後最後一波調window後因為進不了loop , 所以手動補, 
        可以替換成剛把元素放入window後檢查一次 , 然後在hashset和指標操作完再檢查

*/

var containsNearbyDuplicate = function(nums, k) {

    let window_size = Math.min( nums.length , k+1) ; 
    let hashset = new Set() ; 
    // 在固定視窗的情況下 , 還是用一個left , right 方便控制進出hashset的值 
    let left  = 0 ; 
    let right = window_size ; 

    // 先將元素加入window 
    for (let i = 0 ; i < window_size ; i++){
        hashset.add( nums[i] );
    }

    while ( right < nums.length ){
        
        if (hashset.size != window_size) {return true}

        hashset.delete(nums[left]) ; 
        left += 1 ;
        hashset.add(nums[right]) ; 
        right += 1 ;
    }

    if (hashset.size != window_size) {return true}

    return false ; 
}