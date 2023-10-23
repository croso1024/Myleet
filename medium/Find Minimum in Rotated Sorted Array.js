/**
 * @param {number[]} nums
 * @return {number}
 */

/*
    思路 :  
        這一題給定了一個原先是sorted array再經過n次 rotate的array , 要求我們找出array中的最小元素 ,  
        每次rotate的定義為   [ nums[0] , nums[1] , nums[2] ] -> [nums[2] , nums[0] , nums[1] ]  ,並且題目沒有說rotate了幾次
        
        題目要我們寫一個Time complexity在O(Log N)的算法, "題目有給定所有的value都是unique"

        切分的思路大致如下，是透過Binary search來做 

        首先切一刀 , 會有幾種狀況 
        1. 對於一個正常的sorted array來說 , mid的值應該大於等於左邊界 , 小於等於右邊界 -> 此時就往左邊繼續收縮直到相遇
        2. 如果mid的值大於右方邊界 , 可以說明mid到右方邊界的範圍就是最小值的所在 , left = mid+1  
        3. 如果mid的值小於左方邊界 , 則反過來說mid到左方邊界的範圍有最小值 , right = mid - 1 

        最後就是如何做收縮 , 此題類似找左方邊界的binary search, 收縮到右方邊界 right = left-1時 , left就指向答案
        
        ---- 改用Divied and conquer 

        這一題寫了很多次 , 如果要用binary search直接切割 , 這一題的細節有點太過複雜 
        ,這邊參考網路上的資源提點 , 才發覺可以用分治法 , 
        對於一個小段的array來說 , 如果array是sorted的 ( 最後一個element > 第一個 ) , 那最小值就是第一個 
        透過不斷分割 , 找到每個子問題的最小值再做聚合
*/


// divied and conquer 
// 這邊特別要注意一下細節 , 我們傳入 left 展開的slice使用 0-> mid+1 , 
// 因為如果nums.length = 2 , mid會等於0 , 造成left_min那邊是拿到空的 
// 因此這邊多加1 , 反正nums.length == 1被我們擋掉了 ( 或著把nums.length == 2也加進去base case 也可)

var findMin = function(nums) {

    if ( nums.length == 1 ){return nums[0]}

    let left = 0; 
    let right = nums.length-1 ; 

    if (nums[left] < nums[right]){ return nums[left] } 

    let mid = Math.floor(  (left+right)/2 ); 

    let left_min = findMin( nums.slice(0 , mid+1) ) ;  
    let right_min = findMin( nums.slice(mid+1)) ; 

    return Math.min(left_min , right_min) ;


};

// 把mid那邊改回我習慣的樣式 , 但就是要多加nums.length == 2 的base case 
var findMin = function(nums) {

    if ( nums.length == 1 ){return nums[0]}
    else if (nums.length ==2){return (nums[0]>nums[1])?  nums[1]:nums[0]  }

    let left = 0; 
    let right = nums.length-1 ; 

    if (nums[left] < nums[right]){ return nums[left] } 

    let mid = Math.floor(  (left+right)/2 ); 


    return Math.min(findMin( nums.slice(0 , mid) ) , findMin( nums.slice(mid))) ;


};