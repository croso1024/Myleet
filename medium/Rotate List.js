/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */

/*
    思路 :  
        這一題優先考慮雙指標來解 , 我稍微思考的解法是這樣 ,
        透過快慢指標先定位到倒數第k個節點 
        這樣我們一共有三個pointer :
        head : 指向頭 
        slow : 指向倒數第k個 , rotate完成會變成最後一個 
        fast : 指向最後一個節點 , rotate後要接在原先head上  

        實際上rotate完成的新head就是slow所指向的那一個 

        現在最後一個問題就是 , k 有可能大於節點數 , 因此直覺最簡單的作法是先跑一個O(N)算節點數 
        
*/

/* 
    解法一. 先老實的算節點數 , 測試一下我上面的概念是否ok
    實際上這個解的速度就超級優秀 , 反而空間很差 
*/

var rotateRight = function(head, k) {
    
    if (k==0 || head == null){return head;}
    // 計算一下節點數
    let count = 0 ; 
    let temp = head ; 
    while ( temp != null ){
        count += 1 ; 
        temp = temp.next ; 
    }

    // 計算實際要rotate的次數 , 
    k = k % count ;   
    if (k==0){return head;} 

    // 快慢指標 , 現在k一定 <= count 
    count = 0 ; 
    let slow = head ; 
    let fast = head ; 
    // 快指標先走k步
    for (let i = 0 ; i < k ; i++){fast = fast.next;}
    // 接下來走到底
    while (fast.next != null){
        fast = fast.next ;
        slow = slow.next ; 
    }

    // 此時開始走我原訂計畫的邏輯 , 我們現在有head , slow , fast 
    
    // 新的head就會變成slow的下一個值 , 而slow則是新的最後一個值 
    // slow.next一定會指向一個節點 , 否則代表k=0 ,根本沒有轉
    let newHead = slow.next ;  
    slow.next = null ; 
    // 將fast的值接在head上 
    fast.next = head ; 

    return newHead ; 

};