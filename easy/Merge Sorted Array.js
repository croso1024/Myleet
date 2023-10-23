/*
    思路 : 
        這一題看起來要求in-place的操作來合併兩個sorted array , 
        但比較特殊的地方在於arr 1 = [1,2,3,0,0,0] , arr 2 = [2,3,5] , 
        即arr1預留了arr2長度的0 , 要我們inplace的將sorted array保存在nums1中 


*/


/*
    解法一 .  
        既然題目給定了 arr1中有數字的數量  , 我們可以取出有數字的部份作為
        temp , 即temp = arr.slice(0,m)   
        之後使用temp , arr2 做雙噴結束 

        time complexit = O(m+n) 
        space complexity = O(m) 

*/

var merge = function(nums1, m, nums2, n) {
    
    let temp = nums1.slice(0 , m)  ; 
    
    let probe1 = 0 ; 
    let probe2 = 0 ; 

    while (probe1 < temp.length && probe2 < nums2.length) {

        if (temp[probe1] < nums2[probe2]) {
            nums1[probe1+probe2] = temp[probe1] ; 
            probe1 += 1 ; 
        }

        else {
            nums1[probe1+probe2] = nums2[probe2] ; 
            probe2 += 1 ; 
        }
    
    }
    if (probe1<temp.length){
        
        for (let index = probe1 ; index < temp.length ; index ++) {
            nums1[index+probe2] = temp[index]; 
        }

    }
    else {
        for ( let index = probe2 ; index<nums2.length;index++){
            nums1[index+probe1] = nums2[index] ; 
        }
    };
    
    return nums1 ;

};


/*
    解法二 . 在Solution區看到的 , 同樣是two pointer 

        此解法的關鍵在於他是從後面開始比較大小 , 也就是從尾到頭的two pointer , 
        這樣子就可以避開上面那種解法一我還需要特別花空間去保存nums1前m個元素的問題  

        得到O(m+n)的時間和O(1)的空間
*/

var merge = function(nums1, m, nums2, n) {

    let probe1 = m-1 ; 
    let probe2 = n-1 ; 

    // 從最後一個非0值開始比較 , 因此改以比大
    for (let index = m+n-1 ; index >= 0 ; index--){

        // 內部也需要防止index炸裂的措施 
        if (probe1>=0 && probe2>=0){
            if (nums1[probe1] > nums2[probe2])  {
                nums1[index] = nums1[probe1] ; 
                probe1 -= 1 ; 
            }
            else {
                nums1[index] = nums2[probe2] ; 
                probe2 -= 1 ;
            }
        }

        else {
            if (probe1>=0) {
                nums1[index] = nums1[probe1] ; 
                probe1-=1 ; 
            }
            else {
                nums1[index] = nums2[probe2] ; 
                probe2 -= 1 ; 
            }
        }   

    }

    return nums1 ; 

} 